from helpers.utils import find_product

def read_product(productId, productCol):
    product = find_product(productId, productCol)
    if product:
        print("-="*20)
        print("     Informações do Produto:")
        print("-="*20)
        print(f"Nome: {product.get('nome', 'Informação não disponível')}")
        print(f"Marca: {product.get('marca', 'Informação não disponível')}")
        print(f"Valor: R$ {product.get('valor', 'Informação não disponível')}")
        print(f"Estoque: {product.get('estoque', 'Informação não disponível')}")
        print(f"Vendas: {product.get('vendas', 'Informação não disponível')}")
        vendedor = product.get('vendedor')
        if vendedor:
            print("Informações do Vendedor:")
            print(f"Nome: {vendedor.get('nome', 'Informação não disponível')}")
            print(f"E-mail: {vendedor.get('email', 'Informação não disponível')}")
            print(f"CNPJ: {vendedor.get('cnpj', 'Informação não disponível')}")
            print(f"Avaliação: {vendedor.get('avaliacao', 'Informação não disponível')}")
    else: 
        return  print("Produto não encontrado!")

def list_products(collection):
    mydoc = collection.find().sort("nome")
    products = list(mydoc)
    products_list = [{"id": str(product.get("_id")), "nome": product.get("nome"), "marca": product["marca"]} for product in products]
    print("     Lista de produtos:")
    print("-="*20)
    for product in products_list:
        print(f"ID: {product['id']}, Nome: {product['nome']}, Marca: {product["marca"]}")
    print("-="*20)


    


