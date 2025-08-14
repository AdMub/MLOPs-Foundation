import pymongo

# Provide the mongodb localhost url to connect python to mongodb
client = pymongo.MongoClient("mongodb://localhost:27017/..")

# Database Name
dataBase = client["admub465"]

# Collection NAme
collection = dataBase["Products"]

# Sample data
d ={"companyName": "SRDA",
    "product": "Affordable Analytics",
    "courseoffered": "R-Studio & SPSS for Data Analytics"}

# Insert above records in the collection
rec = collection.insert_one(d)

# Let's vrify all the record at once present in the record with all the fields
all_record = collection.find()

# Printing all records present in the collection
for idx, record in enumerate(all_record):
    print(f"{idx}: {record}")