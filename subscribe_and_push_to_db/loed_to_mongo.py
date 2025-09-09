from venv import logger

from pymongo import MongoClient
from logger import Logger
import gridfs

import config


class Loed_to_mongo:
    def __init__(self):
        logger = Logger.get_logger()
        self.uri=f"mongodb://{config.MONGO_HOST}:{config.MONGO_PORT}"
        self.client = MongoClient(self.uri )
        self.db = self.client[config.DB_NAME]
        self.collection = self.db[config.COLLECTION_NAME]
        self.fs = gridfs.GridFS(self.db)
        logger.info("connect to nmongo")
        # logger.error("faild to connect to mongo")


    def insert_one(self,path, data: dict):
        """Insert a single document into the collection"""
        try:
            with open(f"{path}", "rb") as f:
                pdf_file_id = self.fs.put(f, filename=data["unique_id"],content_type="application/wev")
        except Exception as e:
            logger.error("not pushed_to_mongo")
            

