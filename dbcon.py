from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["api_blog"]
posts_collection = db["posts"]
comments_collection = db["comments"]

#  check if the connection is established
connected = client.is_primary
if connected:
    print("Connected to MongoDB")
else:
    print("Failed to connect to MongoDB")

