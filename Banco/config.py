from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

def connection():
    uri = "mongodb+srv://joyceaparecida20152:ZvZy9BCbSWMPPphA@cluster.ox6qa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster"
    client = MongoClient(uri, server_api=ServerApi('1'))
    try:
        client.admin.command('ping')  
        print("Banco conectado!")
        return client  
    except Exception as e:
        print(f"Erro ao conectar ao banco: {e}")
        return None  
