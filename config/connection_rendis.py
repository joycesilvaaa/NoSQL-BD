import redis

def connection_rendis():
    try:
        r = redis.Redis(
        host='redis-17047.c308.sa-east-1-1.ec2.redns.redis-cloud.com',
        port=17047,
        password='password')
        r.ping()
        print('Redis conectado!')
        return r 
    except redis.ConnectionError:
        print('Erro ao conectar ao Redis')
        return None
    except Exception as e:
        print(f'Ocorreu um erro: {e}')  
        return None