import re
from commands import Bunny

import flask

DEFAULT_URL = "https://www.google.com/"

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
        if re.match(key, arg):
            return flask.redirect(bunnyAliases[key].run(arg, flask.request))

    # Otherwise we fall back to redirecting to wherever...
    return flask.redirect(flask.url_for("default"))


if __name__ == "__main__":
    app.run()
