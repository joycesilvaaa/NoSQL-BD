from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from config.create_collections import create_collection

def connection_cassandra():
    try:
        cloud_config = {
            'secure_connect_bundle': 'config/nome_do_seu_arquivo_zip'
        }
        auth_provider = PlainTextAuthProvider(username='token', password='')
        cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
        session = cluster.connect()
        print('Cluster conectado :)')
        create_collection(session)
        return session
    except Exception as e:
        print(f'Erro ao conectar ao canssandra ${e}')
        return None
