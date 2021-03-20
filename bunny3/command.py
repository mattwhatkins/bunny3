import logging
from tinydb.operations import increment
from tinydb import Query


class BunnyCommand(object):
    """Parent class for each bunnyCommand"""

    def __init__(self):
        self.aliases = []
        self.aliasRegexes = []
        self.description = ""
        self.name = ""
        self.query = Query()
        self.runCount = 0
        self.url = ""

    def bumpCount(self, db):
        self.runCount += 1
        if len(db.update(increment("count"), self.query.command == self.name)) == 0:
            logging.error(f"Error incrementing count for {self.name}")

    def getName(self):
        return self.name

    def run(self, args, request=None):
        raise NotImplementedError

    def setCount(self, count):
        self.runCount = count
