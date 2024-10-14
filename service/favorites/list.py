import json

def list_favorites(db_redis, user):
    redis_key = f"user:{user['_id']}:favorites"
    #Recupera todos os membros de um conjunto
    favorites = db_redis.smembers(redis_key)
    #Converte para dicionarios
    favorite_list = [json.loads(fav) for fav in favorites]

    if favorite_list:
        print("Favoritos armazenados:")
        for fav in favorite_list:
            print(f"Produto ID: {fav['_id']}, Nome: {fav['nome']}, Marca: {fav['marca']}, Valor: {fav['valor']}")
            print(f"Vendedor: {fav['vendedor']['nome']}, Avaliação: {fav['vendedor']['avaliacao']}")
            print("-" * 40)
    else:
        print("Nenhum favorito encontrado.")
