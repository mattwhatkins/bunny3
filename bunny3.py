import pkgutil
import re
from inspect import getmembers, isclass

import flask

from command import BunnyCommand

DEFAULT_URL = "https://www.google.com/"


class Bunny(object):
    def __init__(self):
        self.load_commands()

    def load_commands(self):
        self.aliasDict = {}
        self.commandDict = {}
        self.commandDir = "commands"

        for _, commandname, _ in pkgutil.iter_modules([self.commandDir]):
            full_commandname = "%s.%s" % (self.commandDir, commandname)
            command = __import__(full_commandname, fromlist=[full_commandname])
            for _, obj in getmembers(command, isclass):
                if issubclass(obj, BunnyCommand):
                    if obj is not BunnyCommand:
                        o = obj()
                        self.commandDict[", ".join(o.aliases)] = o
                        for a in o.aliases:
                            self.aliasDict[a] = o


app = flask.Flask(__name__)
app.config["DEBUG"] = True
bunny = Bunny()
bunnyAliases = bunny.aliasDict
bunnyCommands = bunny.commandDict


@app.route("/default")
def default():
    return flask.redirect(DEFAULT_URL)


@app.route("/list")
def helpPage():
    return flask.render_template("help.html", table=bunnyCommands)


@app.route("/search")
def route():
    # Example syntax: /search?q=%s
    arg = flask.request.args.get("q")
    if len(arg) == 0:
        return flask.redirect(flask.url_for("default"))

    # First we try to perform an exact match on the alias
    command = bunnyAliases.get(arg.split()[0])
    if command:
        commandArgs = " ".join(arg.split()[1:])
        return flask.redirect(command.run(commandArgs, flask.request))

    # Then we check for any regex aliases
    for key in bunnyAliases.keys():
        if re.match(key, arg, re.IGNORECASE):
            return flask.redirect(bunnyAliases[key].run(arg, flask.request))

    # Otherwise we fall back to redirecting to the default...
    # TODO: Make this configurable with default fallback options
    return flask.redirect(bunnyAliases.get("g").run(arg, flask.request))


if __name__ == "__main__":
    app.run()
