from typing import Any, Optional
import os
import pandas as pd
import json
from pymongo.mongo_client import MongoClient
from ensure import ensure_annotations


class MongoOperation:
    __collection = None  # Private class-level variable for collection tracking
    __database = None    # Private class-level variable for database tracking

    def __init__(self, client_url: str, database_name: str, collection_name: Optional[str] = None):
        self.client_url = client_url
        self.database_name = database_name
        self.collection_name = collection_name

    def create_mongo_client(self):
        """Create and return a MongoDB client."""
        return MongoClient(self.client_url)

    def create_database(self):
        """Create and return the MongoDB database."""
        if MongoOperation.__database is None:
            client = self.create_mongo_client()
            self.database = client[self.database_name]
            MongoOperation.__database = self.database
        return MongoOperation.__database

    def create_collection(self, collection: Optional[str] = None):
        """Create and return a MongoDB collection."""
        if collection is None:
            collection = self.collection_name
        if not collection:
            raise ValueError("Collection name must be provided either during initialization or in this method.")

        if MongoOperation.__collection != collection:
            database = self.create_database()
            self.collection = database[collection]
            MongoOperation.__collection = collection

        return self.collection

    def insert_record(self, record: Any, collection_name: Optional[str] = None) -> None:
        """Insert a single record or a list of records into the collection."""
        collection = self.create_collection(collection_name)

        if isinstance(record, list):
            if not all(isinstance(data, dict) for data in record):
                raise TypeError("All items in the record list must be dictionaries.")
            collection.insert_many(record)
        elif isinstance(record, dict):
            collection.insert_one(record)
        else:
            raise TypeError("Record must be a dictionary or a list of dictionaries.")

    def bulk_insert(self, datafile: str, collection_name: Optional[str] = None) -> None:
        """Insert bulk data from CSV or Excel into the collection."""
        if not os.path.exists(datafile):
            raise FileNotFoundError(f"The file '{datafile}' does not exist.")

        if datafile.endswith(".csv"):
            dataframe = pd.read_csv(datafile, encoding="utf-8")
        elif datafile.endswith(".xlsx"):
            dataframe = pd.read_excel(datafile)  # No encoding param for read_excel
        else:
            raise ValueError("File must be a CSV or XLSX.")

        datajson = json.loads(dataframe.to_json(orient="records"))
        collection = self.create_collection(collection_name)
        collection.insert_many(datajson)
