import random
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

user = os.getenv("Mongo_User")
password = os.getenv("Mongo_Password")
cluster = os.getenv("Mongo_cluster")
db_name = os.getenv("Mongo_DB")
collection_name = os.getenv("Mongo_coleccion")

mongo_uri = f"mongodb+srv://{user}:{password}@{cluster}/{db_name}?retryWrites=true&w=majority"

client = MongoClient(mongo_uri)
db = client[db_name]
collection = db[collection_name]

print(f"Conectado a {db_name} -> {collection_name}")
 
productos = ["laptop", "celular", "tablet"]

lista = []
for _ in range(100):
    lista.append({
        "producto": random.choice(productos),
        "cantidad": random.randint(1, 20),
        "precio": random.randint(1000, 15000)
    })

collection.delete_many({})
collection.insert_many(lista)
print("100 productos guardados")