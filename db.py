from pymongo import MongoClient

class Database:
    def __init__(self, db_uri: str, db_name: str):
        self.client = MongoClient(db_uri)
        self.db = self.client[db_name]
    
    def get_collection(self, collection_name: str):
        return self.db[collection_name]

db = Database("mongodb://localhost:27017/", "blog")
