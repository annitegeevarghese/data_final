#!/usr/bin/env python
# coding: utf-8

# In[23]:


import sys
get_ipython().system('{sys.executable} -m pip install pymongo[srv]')


# In[24]:


from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://annitegeevarghese:AaBbCcDd@cluster0.juqmj6m.mongodb.net/dataprogrammingretryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


# In[25]:


pip install motor


# In[26]:


url = "https://rapidapi.com/KanjiAlive/api/learn-to-read-and-write-japanese-kanji/"


# In[27]:


import aiohttp
from motor.motor_asyncio import AsyncIOMotorClient
from urllib.parse import quote_plus

# Replace <password> with your MongoDB Atlas password
# Replace your_username with your MongoDB Atlas username
# Replace your_database with your MongoDB Atlas database name
username = "annitegeevarghese"
password = "AaBbCcDd"
database = "dataprogramming"

# URL-encode the username and password
encoded_username = quote_plus(username)
encoded_password = quote_plus(password)

# Create the MongoDB connection string
uri = f"mongodb+srv://{encoded_username}:{encoded_password}@cluster0.juqmj6m.mongodb.net/{database}?retryWrites=true&w=majority"

# Create an AsyncIOMotorClient
client = AsyncIOMotorClient(uri)
db = client[database]

async def fetch_and_insert_data():
    rapidapi_url = "https://learn-to-read-and-write-japanese-kanji.p.rapidapi.com/kanji"

    headers = {
        'X-RapidAPI-Host': 'learn-to-read-and-write-japanese-kanji.p.rapidapi.com',
        'X-RapidAPI-Key': 'b4b32015a4mshc8bb8e844d530e6p19e085jsnc6e247e02d4d',  # Replace with your RapidAPI key
        'Content-Type': 'application/json',
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(rapidapi_url, headers=headers) as response:
                data = await response.json()

        print(f"Fetched data: {data}")

        # Check if API response contains an error message
        if 'message' in data:
            if "API doesn't exist" in data['message']:
                print("Error: The API doesn't exist.")
                return

        # Check if data retrieval was successful
        if 'your_expected_data_field' in data:
            # Process the data as needed
            processed_data = process_data(data['your_expected_data_field'])

            # Insert processed data into MongoDB in the 'kanji_data' collection
            result = await db.kanji_data.insert_many(processed_data)
            print(f"Inserted {len(processed_data)} documents into 'kanji_data' collection. Inserted IDs: {result.inserted_ids}")
        else:
            print("Error: 'your_expected_data_field' not found in the fetched data.")
    except Exception as e:
        print(f"Error during data retrieval: {e}")

def process_data(kanji_data):
    processed_data = []
    for entry in kanji_data:
        # Extract relevant fields and perform any additional processing
        processed_entry = {
            'field1': entry['field1'],
            'field2': entry['field2'],
            # Add more fields as needed
        }
        processed_data.append(processed_entry)
    return processed_data

# Run the fetch_and_insert_data function
await fetch_and_insert_data()


# In[ ]:





# In[ ]:




