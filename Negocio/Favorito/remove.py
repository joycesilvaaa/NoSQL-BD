from Negocio.Favorito.list import list_favorite

def remove_favorite(user, userCol, productCol):
    list_favorite(user)
    product_name = input("Digite o nome do produto que deseja remover do favorito: ")
    products = list(productCol.find({"nome": product_name}))
    if not products:
        return print("Produto não encontrado")
    if len(products) > 1:
        product_marca = input("Digite a marca do produto: ")
        product = productCol.find({"nome": product_name, "marca": product_marca})
        if not product:
            return print("Produto não encontrado com essa marca")
    else:
        product = products[0]

    result = userCol.update_one(
        {"cpf": user["cpf"]},
        {"$pull": {"favoritos": {"nome": product["nome"], "marca": product["marca"]}}}
    )

    print("Produto removido!")


