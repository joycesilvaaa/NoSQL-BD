from helpers.utils import find_product

def delete_product(productId, productCol,sellerCol):
    product = find_product(productId, productCol)
    if product:
        productCol.delete_one({"_id": product["_id"]})

        sellerCnpj = product["vendedor"]["cnpj"]  
        
        sellerCol.update_one({"cnpj": sellerCnpj},{"$pull": {"produtos": {"nome": product["nome"]}}})
        return print("Produto deletado com sucesso!")
    else:
        return print("Produto não encontrado!")
