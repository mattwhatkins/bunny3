import sys
from inspect import getmembers, isclass
from urllib.parse import quote_plus as qp


class Bunny(object):
    def __init__(self):
        self.load_commands()

    def load_commands(self):
        self.aliasDict = {}
        self.commandDict = {}
        for _, obj in getmembers(sys.modules[__name__], isclass):
            if issubclass(obj, BunnyCommand):
                if obj is not BunnyCommand:
                    o = obj()
                    self.commandDict[", ".join(o.aliases)] = o
                    for a in o.aliases:
                        self.aliasDict[a] = o


class BunnyCommand(object):
    """Parent class for each bunnyCommand"""

    def __init__(self):
        self.aliases = []
        self.description = ""
        self.name = ""
        self.runCount = 0

    def run(self, args, request=None):
        raise NotImplementedError


class google(BunnyCommand):
    def __init__(self):
        super().__init__()
        self.aliases = ["g", "google", "g.*"]
        self.description = "Google Search"
        self.name = "Google"

    def run(self, args, request):
        self.runCount += 1
        print(self.runCount)
        if args:
            return "https://www.google.com/search?q=%s" % qp(args)
        else:
            return "https://www.google.com/"


class list(BunnyCommand):
    def __init__(self):
        super().__init__()
        self.aliases = ["help", "list"]
        self.description = "Lists all available commands"
        self.name = "List"

    def run(self, args, request):
        self.runCount += 1
        print(self.name + ": " + str(self.runCount))
        return request.url_root + "list"


class youtube(BunnyCommand):
    def __init__(self):
        super().__init__()
        self.aliases = ["youtube"]
        self.description = "Youtube Search"
        self.name = "Youtube"

    def run(self, args, request):
        if args:
            return "https://www.youtube.com/results?search_query=%s" % qp(args)
        else:
            return "https://www.youtube.com/"
