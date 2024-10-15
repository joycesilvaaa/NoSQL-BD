from utils.utils import find_product
from .list import list_favorites

def remove_favorite(product_col, db_redis, user):
    list_favorites(db_redis, user)
    favorites_removed = []

    while True:
        product_id = input('Digite o Id do produto que deseja remover do favorito: ')
        product = find_product(product_id, product_col)

        if product:
            product_info = {
                "_id":product["_id"],
                "nome": product["nome"],
                "marca": product["marca"],
                "valor": product["valor"],
                "vendedor": {
                    "_id":product["vendedor"]["_id"],
                    "cnpj": product["vendedor"]["cnpj"], 
                    "nome": product["vendedor"]["nome"],
                    "avaliacao": product["vendedor"]["avaliacao"]
                }
            }
            favorites_removed.append(product_info) 
        else:
            print('Produto não encontrado!')

        proceed = input('Deseja remover mais algum? (S/N) ').lower()
        if proceed == 'n':
            break

    redis_key = f"user:{user['_id']}:favorites"

    for fav in favorites_removed:
        result = db_redis.srem(redis_key, str(fav))
        
        if result > 0:
            print(f"Produto removido dos favoritos com sucesso.")
        else:
            print(f"Produto {fav} não encontrado nos favoritos.")

    print("-=" * 20)

