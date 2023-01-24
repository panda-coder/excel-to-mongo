import logging

from pymongo import MongoClient
from consts import DATABASE_URI, DATABASE_PORT

logging.info("Creating database client")
database = MongoClient(host=DATABASE_URI, port=DATABASE_PORT)