from config.connection_cassandra import connection_cassandra

def main():
    data_base = connection_cassandra()
    if data_base is None:
        print('Erro ao conectar ao Banco de Dados')
        return
    j