from pymongo import MongoClient
from dotenv import load_dotenv
import os
from urllib.parse import quote_plus

# Carga tu archivo .env
load_dotenv()

usuario = os.getenv("Mongo_User")
password= quote_plus(os.getenv("Mongo_Password"))
cluster = os.getenv("Mongo_cluster")
base_datos = os.getenv("Mongo_DB")
coleccion_nombre = os.getenv("Mongo_coleccion")

mongo_uri = f"mongodb+srv://{usuario}:{password}@{cluster}/{base_datos}?retryWrites=true&w=majority"

 