from helpers.utils import find_product

def update_product(productId, productCol,sellerCol):
    print("-="*20)
    print("     Edição de Produto")
    print("-="*20)
    #Produto Update
    product = find_product(productId, productCol)
    if not product:
        print("Produto não encontrado!")
        return
    valor = int(input("Mudar Valor (ou Enter para continuar):"))
    if valor:
        product["valor"] = valor
    estoque = int(input("Mudar estoque (ou Enter para continuar): "))
    if estoque:
        product["estoque"] = estoque
    productCol.update_one({"_id":product["_id"]},{"$set":{"valor":valor, "estoque": estoque}})
    sellerCol.update_one({"cnpj": product["vendedor"]["cnpj"], "produtos.nome": product["nome"]},{"$set": {"produtos.$.valor": product.get("valor", product["valor"]),"produtos.$.estoque": product.get("estoque", product["estoque"])}})
    print("-="*20)
    return print("Produto atualiazado com sucesso!")
    

def update_sale_and_stock(product, quantity, productCol):
    stock = int(product.get("estoque"))
    sale = int(product.get("vendas"))
    product["estoque"] = stock - quantity
    product["vendas"] = sale + quantity
    productCol.update_one({"_id":product["_id"]}, {"$set": {"estoque": product["estoque"], "vendas": product["vendas"]}})
