from Negocio.Produto.read import list_products
from helpers.utils import find_product

def add_favorite(user, userCol, productCol):
    list_products(productCol)
    favorites_list = []
    
    while True:
        product_id = input("Digite o ID do produto que deseja favoritar: ")
        product = find_product(product_id, productCol)
        
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
            favorites_list.append(product_info)
        else:
            print("Produto não encontrado.")
        
        continuar = input("Deseja favoritar mais algum? (S/N): ").lower()
        if continuar == "n":
            break
    
    for fav in favorites_list:
        userCol.update_one(
            {"cpf": user["cpf"]},
            {"$push": {"favoritos": fav}}
        )
    print("-="*20)
    print("Favorito adicionados com sucesso.")



