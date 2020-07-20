from urllib.parse import quote_plus as qp

from command import BunnyCommand


class hukd(BunnyCommand):
    def __init__(self):
        super().__init__()
        self.aliases = ["hukd"]
        self.description = "Hotukdeals search"
        self.name = "Hotukdeals"

    def run(self, args, request):
        self.runCount += 1
        print(self.name + ": " + str(self.runCount))
        if args:
            return "https://www.hotukdeals.com/search?q=%s" % qp(args)
        else:
            return "https://www.hotukdeals.com/"
