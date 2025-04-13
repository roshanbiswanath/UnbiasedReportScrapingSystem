from pymongo.server_api import ServerApi
from pymongo.mongo_client import MongoClient

import os
from dotenv import load_dotenv
load_dotenv()

def getClient():
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = os.getenv('MONGO_URL')  
    client = MongoClient(CONNECTION_STRING, server_api=ServerApi('1'))
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
    return client
  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
   # Get the database
    dbname = getClient()