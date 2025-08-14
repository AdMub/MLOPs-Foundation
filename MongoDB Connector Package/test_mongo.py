from pymongo import MongoClient

# Your MongoDB connection string
uri = "mongodb+srv://admub465:Original465@dbpractice.7uz5kjl.mongodb.net/test?retryWrites=true&w=majority"

try:
    client = MongoClient(uri)
    # List databases to confirm connection
    print("Databases:", client.list_database_names())
    print("✅ Connected successfully!")
except Exception as e:
    print("❌ Connection failed!")
    print(e)