from urllib.parse import quote_plus as qp

from command import BunnyCommand


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
        return "%slist" % request.url_root


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
