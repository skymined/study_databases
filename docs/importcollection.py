
def importcollection (collection):
    from pymongo import MongoClient
    mongoclient = MongoClient("mongodb://localhost:27017")
    database = mongoclient["local"]
    collection = database[collection]