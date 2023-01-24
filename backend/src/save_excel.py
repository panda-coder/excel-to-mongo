import logging
from database import database
from excel_file import ExcelFile

class SaveExcel:
    __excel_file: ExcelFile = None
    __db = None

    def __init__(self, excel_file: ExcelFile):
        client = database
        self.__db = client["excel-database"]
        self.__excel_file = excel_file

    def save(self):
        collection = self.__db['excel']
        collection.insert_one(self.__excel_file.to_dict())