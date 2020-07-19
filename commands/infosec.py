from urllib.parse import quote_plus as qp

from command import BunnyCommand


class vt(BunnyCommand):
    def __init__(self):
        super().__init__()
        self.aliases = ["vt"]
        self.description = "Searches VirusTotal"
        self.name = "VirusTotal"

    def run(self, args, request):
        self.runCount += 1
        print(self.name + ": " + str(self.runCount))
        return "https://www.virustotal.com"


class shodan(BunnyCommand):
    def __init__(self):
        super().__init__()
        self.aliases = ["shodan"]
        self.description = "Searches Shodan"
        self.name = "Shodan"

    def run(self, args, request):
        self.runCount += 1
        print(self.name + ": " + str(self.runCount))
        if args:
            return "https://www.shodan.io/search?query=%s" % qp(args)
        else:
            return "https://www.shodan.io"
