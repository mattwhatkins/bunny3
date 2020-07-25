class BunnyCommand(object):
    """Parent class for each bunnyCommand"""

    def __init__(self):
        self.aliases = []
        self.aliasRegexes = []
        self.description = ""
        self.name = ""
        self.runCount = 0
        self.url = ""

    def run(self, args, request=None):
        raise NotImplementedError
