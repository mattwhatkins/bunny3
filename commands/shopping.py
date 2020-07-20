from urllib.parse import quote_plus as qp

from command import BunnyCommand


class amazon(BunnyCommand):
    def __init__(self):
        super().__init__()
        self.aliases = ["amazon"]
        self.description = "Amazon search"
        self.name = "Amazon"
        self.url = "https://www.amazon.co.uk/"

    def run(self, args, request):
        if args:
            return f"{self.url}s?k={qp(args)}&ref=nb_sb_noss"
        else:
            return self.url


class hukd(BunnyCommand):
    def __init__(self):
        super().__init__()
        self.aliases = ["hukd"]
        self.description = "Hotukdeals search"
        self.name = "Hotukdeals"
        self.url = "https://www.hotukdeals.com/"

    def run(self, args, request):
        if args:
            return f"{self.url}search?q={qp(args)}"
        else:
            return self.url
