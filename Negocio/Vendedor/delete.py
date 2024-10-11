from helpers.utils import find_seller

def delete_seller(cnpj, sellerCol):
    seller = find_seller(cnpj, sellerCol)
    if seller:
        sellerCol.delete_one({"_id": seller["_id"]})
        print("-="*20)
        return print("Vendedor deletado com sucesso!")
    return print("Vendedor não encontrado!")