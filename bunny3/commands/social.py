from urllib.parse import quote_plus as qp

from bunny3.command import BunnyCommand


class youtube(BunnyCommand):
    def __init__(self):
        super().__init__()
        self.aliases = ["youtube"]
        self.description = "Youtube Search"
        self.name = "Youtube"
        self.url = "https://www.youtube.com/"

    def run(self, args, request):
        if args:
            return f"{self.url}results?search_query={qp(args)}"
        else:
            return self.url
