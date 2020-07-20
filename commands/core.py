from urllib.parse import quote_plus as qp

from command import BunnyCommand


class google(BunnyCommand):
    def __init__(self):
        super().__init__()
        self.aliases = ["g", "google"]
        self.description = "Google Search"
        self.name = "Google"
        self.url = "https://www.google.com/"

    def run(self, args, request):
        if args:
            return f"{self.url}search?q={qp(args)}"
        else:
            return self.url


class list(BunnyCommand):
    def __init__(self):
        super().__init__()
        self.aliases = ["help", "list"]
        self.description = "Lists all available commands"
        self.name = "List"

    def run(self, args, request):
        # TODO: url_root - It would be good to have this configured somewhere
        if self.url == "":
            self.url = f"{request.url_root}list"
        return self.url
