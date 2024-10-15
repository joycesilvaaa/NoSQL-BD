from bson import ObjectId

def list_favorites(db_redis, user):
    redis_key = f"user:{user['_id']}:favorites"
    favorites = db_redis.smembers(redis_key)

    favorite_list = [eval(fav.decode('utf-8'), {"ObjectId": ObjectId}) for fav in favorites]

    if favorite_list:
        print("-" * 40)
        print("Favoritos armazenados:")
        print("-" * 40)
        for fav in favorite_list:
            print(f"Produto ID: {fav['_id']}, \nNome: {fav['nome']}, Marca: {fav['marca']}, Valor: {fav['valor']}")
            print(f"Vendedor: {fav['vendedor']['nome']}, Avaliação: {fav['vendedor']['avaliacao']}")
            print("-" * 40)
    else:
        print("Nenhum favorito encontrado.")
