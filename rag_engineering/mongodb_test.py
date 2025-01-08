from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient("mongodb://localhost:27017/")

# Access a database
db = client["my_database"]

# Access a collection
collection = db["my_collection"]

# Insert a document
# collection.insert_one({"name": "Tom", "age": 40})

# Retrieve a document
documents = collection.find_one({"name": "Tom"})
# documents = collection.find({"name": "John"})
# Print each document
# for doc in documents:
#     print(doc)
print(documents)
