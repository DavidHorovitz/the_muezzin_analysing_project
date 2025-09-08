from pymongo import MongoClient
import gridfs

import config


class Loed_to_mongo:
    def __init__(self):
        self.uri=f"mongodb://{config.MONGO_HOST}:{config.MONGO_PORT}"
        self.client = MongoClient(self.uri )
        self.db = self.client[config.DB_NAME]
        self.collection = self.db[config.COLLECTION_NAME]
        self.fs = gridfs.GridFS(self.db)


    def insert_one(self,path, data: dict):
        """Insert a single document into the collection"""
        with open(f"{path}", "rb") as f:
            pdf_file_id = self.fs.put(f, filename=data["unique_id"],content_type="application/wev")

        # result = self.collection.insert_one(data)
        # return str(result.inserted_id)

    # def insert_many(self, data_list: list):
    #     """Insert multiple documents"""
    #     result = self.collection.insert_many(data_list)
    #     return [str(_id) for _id in result.inserted_ids]
    #
    # def find_one(self, query: dict):
    #     """Find a single document matching the query"""
    #     return self.collection.find_one(query)
    #
    # def find_many(self, query: dict, skip=0, limit=100):
    #     """Find multiple documents with pagination"""
    #     cursor = self.collection.find(query).skip(skip).limit(limit)
    #     return list(cursor)
    #
    # def update_one(self, query: dict, update_data: dict):
    #     """Update a single document"""
    #     result = self.collection.update_one(query, {"$set": update_data})
    #     return result.modified_count
    #
    # def delete_one(self, query: dict):
    #     """Delete a single document"""
    #     result = self.collection.delete_one(query)
    #     return result.deleted_count
    #
    # def count_documents(self, query: dict = {}):
    #     """Count documents matching query"""
    #     return self.collection.count_documents(query)
