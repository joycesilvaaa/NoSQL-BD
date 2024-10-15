from utils.utils import list_products, find_product

def add_favorite(product_col, db_redis, user):
    list_products(product_col)
    favorites = []

    while True:
        product_id = input('Digite o Id do produto que deseja favoritar: ').strip()
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
            favorites.append(product_info)
        else:
            print('Produto não encontrado!')

        proceed = input('Deseja favoritar mais algum? (S/N) ').lower()
        if proceed == 'n':
            break
    
    for fav in favorites:
        redis_key = f"user:{user['_id']}:favorites"
        db_redis.sadd(redis_key, str(fav))
        
    print("-="*20)
    print("Favorito adicionados com sucesso.")


