import logging
from bson.regex import Regex
from database import database
from pymongo import MongoClient, database as pydb
import re

class LookupExcel:
    __db: pydb.Database = None

    def __init__(self) -> None:
        client = database
        self.__db = client["excel-database"]

    def lookup(self, text):
        collection = self.__db['excel']
        cursor = collection.find({"content.content": {"$elemMatch": {"$elemMatch": {"$in": [Regex(text, "im")]}}}})
        result = []
        for doc in cursor:
            result.append(doc)
        return result

    def lookup_line(self, text):
        collection = self.__db['excel']
        cursor = collection.find({"content.content": {"$elemMatch": {"$elemMatch": {"$in": [Regex(text, "im")]}}}})
        result = []
        for doc in cursor:
            for ws in doc["content"]:
                line_number = 1
                for line in ws["content"]:
                    found = False
                    for item in line:
                        if re.search(r"{}".format(text), str(item)):
                            found = True
                    if found:
                        result.append(dict(file=doc["name"],ws_title=ws["title"],
                        hash=doc["hash"],
                        content=line, line_number=line_number))
                    line_number = line_number + 1
        return result