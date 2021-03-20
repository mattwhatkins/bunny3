import logging
import pkgutil
import re
from inspect import getmembers, isclass
from pathlib import Path
from tinydb import TinyDB, Query

import flask

from bunny3.command import BunnyCommand

DEFAULT_SEARCH_ENGINE = "https://www.google.com/"

logging.basicConfig(level=logging.WARNING)


class Bunny3(object):
    def __init__(self):
        self.load_commands()
        self.stats()
        self.hashAliases()

    def load_commands(self):
        """ Iteratates through commands directory and loads all commands """
        self.aliasDict = {}
        self.aliasRegexDict = {}
        self.commandDict = {}  # TODO: Depricate! (Used in list)
        self.commands = {}
        self.query = Query()

        for _, commandname, _ in pkgutil.iter_modules(["bunny3/commands"]):
            full_commandname = "%s.%s" % ("bunny3.commands", commandname)
            command = __import__(full_commandname, fromlist=[full_commandname])
            for _, obj in getmembers(command, isclass):
                if issubclass(obj, BunnyCommand):
                    if obj is not BunnyCommand:
                        o = obj()
                        self.commands[o.name] = {}
                        self.commands[o.name]["aliases"] = o.aliases
                        self.commands[o.name]["aliasRegexes"] = o.aliasRegexes
                        self.commands[o.name]["func"] = o
                        self.commandDict[", ".join(o.aliases)] = o

    def hashAliases(self):
        """ Builds a hashMap for the aliases and aliasRegexes for performance """
        for cmd in self.commands:
            for a in self.commands[cmd]["aliases"]:
                self.aliasDict[a] = self.commands[cmd]["func"]
            for a in self.commands[cmd]["aliasRegexes"]:
                self.aliasRegexDict[a] = self.commands[cmd]["func"]

    def stats(self):
        """ Initiates TinyDB for command stats """
        self.path = Path(__file__).resolve().parent
        self.dbpath = Path(self.path / "db.json")
        self.db = TinyDB(self.dbpath)

        if (self.dbpath).is_file():
            # Load all existing commands and set counts
            for cmd in self.db:
                if self.commands.get(cmd["command"]):
                    self.commands.get(cmd["command"])["func"].setCount(cmd["count"])
                else:
                    logging.warning(
                        "Unknown command in Logfile: {0}".format(cmd["command"])
                    )

        # Insert any missing (new) commands into the DB
        for cmd in self.commands:
            if len(self.db.search(self.query.command == cmd)) == 0:
                self.db.insert({"command": cmd, "count": 0})


def create_app(bunny):
    app = flask.Flask(__name__)
    app.config["DEBUG"] = True

    @app.route("/default")
    def default():
        return flask.redirect(DEFAULT_SEARCH_ENGINE)

    @app.route("/list")
    def helpPage():
        return flask.render_template("help.html", table=bunny.commandDict)

    @app.route("/search")
    def route():
        # Example syntax: /search?q=%s
        arg = flask.request.args.get("q")
        if len(arg) == 0:
            return flask.redirect(flask.url_for("default"))

        # First we try to perform an exact match on the alias
        command = bunny.aliasDict.get(arg.split()[0])
        if command:
            commandArgs = " ".join(arg.split()[1:])
            command.bumpCount(bunny.db)
            return flask.redirect(command.run(commandArgs, flask.request))

        # Then we check for any regex aliases
        for key in bunny.aliasRegexDict.keys():
            if re.match(key, arg, re.IGNORECASE):
                bunny.aliasRegexDict[key].bumpCount(bunny.db)
                return flask.redirect(bunny.aliasRegexDict[key].run(arg, flask.request))

        # Otherwise we fall back to redirecting to the default...
        # TODO: Make this configurable with default fallback options
        return flask.redirect(bunny.aliasDict.get("g").run(arg, flask.request))

    return app


if __name__ == "__main__":
    bunny = Bunny3()
    app = create_app(bunny)
    app.run()
