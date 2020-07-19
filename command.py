class BunnyCommand(object):
    """Parent class for each bunnyCommand"""

    def __init__(self):
        self.aliases = []
        self.description = ""
        self.name = ""
        self.runCount = 0

    def run(self, args, request=None):
        raise NotImplementedError
