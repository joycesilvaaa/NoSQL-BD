from utils.utils import find_product
from list import list_favorites

def remove_favorite(product_col, db_redis, user):
    list_favorites(db_redis, user)
    favorites_removed = []

    while True:
        product_id = input('Digite o Id do produto que deseja remover do favorito: ')
        product = find_product(product_id, product_col)

        if product:
            favorites_removed.append(product["_id"]) 
        else:
            print('Produto não encontrado!')

        proceed = input('Deseja remover mais algum? (S/N) ').lower()
        if proceed == 'n':
            break

    redis_key = f"user:{user['_id']}:favorites"

    for fav_id in favorites_removed:
        result = db_redis.srem(redis_key, fav_id) 
        
        if result > 0:
            print(f"Produto {fav_id} removido dos favoritos com sucesso.")
        else:
            print(f"Produto {fav_id} não encontrado nos favoritos.")

    print("-=" * 20)

