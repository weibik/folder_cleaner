import json
from pymongo import MongoClient


def connect_to_database():
    # Connect to MongoDB (adjust the connection string as needed)
    client = MongoClient("mongodb://localhost:27017/")
    database = client["folder_cleaner"]
    return database


def create_or_update_rules(database, user_id, rules):
    rule_collection = database["user_rules"]
    rule_collection.update_one(
        {"user_id": user_id},
        {"$set": {"rules": json.dumps(rules)}},
        upsert=True
    )


def get_rules(database, user_id):
    # Retrieve rules for a specific user from MongoDB
    rule_collection = database["user_rules"]
    result = rule_collection.find_one({"user_id": user_id})
    return json.loads(result["rules"]) if result else None
