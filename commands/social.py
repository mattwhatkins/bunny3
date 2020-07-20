from urllib.parse import quote_plus as qp

from command import BunnyCommand


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
