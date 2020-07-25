from urllib.parse import quote_plus as qp

from command import BunnyCommand


class vt(BunnyCommand):
    def __init__(self):
        super().__init__()
        self.aliases = ["vt"]
        self.description = "Searches VirusTotal"
        self.name = "VirusTotal"
        self.url = "https://www.virustotal.com/gui/"

    def run(self, args, request):
        if args:
            return f"{self.url}search/{qp(args)}"
        else:
            return self.url


class shodan(BunnyCommand):
    def __init__(self):
        super().__init__()
        self.aliases = ["shodan"]
        self.description = "Searches Shodan"
        self.name = "Shodan"
        self.url = "https://www.shodan.io/"

    def run(self, args, request):
        if args:
            return f"{self.url}search?query={qp(args)}"
        else:
            return self.url


class domaintools(BunnyCommand):
    def __init__(self):
        super().__init__()
        self.aliases = ["whois", "domaintools", "dt"]
        self.description = "Searches DomainTools"
        self.name = "DomainTools"
        self.url = "https://whois.domaintools.com/"

    def run(self, args, request):
        if args:
            return f"{self.url}{qp(args)}"
        else:
            return self.url


class riskiq(BunnyCommand):
    def __init__(self):
        super().__init__()
        self.aliases = ["riq", "riskiq"]
        self.description = "Searches RiskIQ"
        self.name = "Searches RiskIQ"
        self.url = "https://community.riskiq.com/"

    def run(self, args, request):
        if args:
            return f"{self.url}search/{qp(args)}"
        else:
            return self.url
