import logging
import pymongo

from pymongo import MongoClient




class SaveExcel:
    __excel_file = None
    __db = None

    def __init__(self, excel_file):
        client = MongoClient(host="mongodb://localhost:27017", port=27017)
        self.__db = client["excel-database"]
        self.__excel_file = excel_file

    def save(self):
        collection = self.__db['excel']
        collection.insert_one(self.__excel_file.to_dict())