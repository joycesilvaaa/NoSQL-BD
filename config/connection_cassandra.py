from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

def connection_cassandra():
    try:
        cloud_config = {
            'secure_connect_bundle': './connection_cassandra.py'
        }
        auth_provider = PlainTextAuthProvider(username='token', password='AstraCS:JRArHfnZKfKfeIzjXeweuqpI:184ab001e96db0dd0477870aa789c2cc21dcc9fd6c0e9fe53f855270bcb697c5')
        cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
        session = cluster.connect()
        print('Banco de Dados.')
        return session
    except Exception as e:
        print(f'Erro ao conectar ao canssandra ${e}')
        return None
