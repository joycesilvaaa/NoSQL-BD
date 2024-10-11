def create_product( seller, productCol, sellerCol):
    print("-="*20)
    print("     Inserindo um novo produto")
    print("-="*20)
    nome = input("Nome: ")
    marca = input("Marca: ")
    valor = float(input("Valor: ")) 
    estoque = int(input("Estoque: "))  
    vendas = 0  
    vendedor = seller
    mydoc = {
        "nome": nome,
        "marca": marca,
        "valor": valor,
        "estoque": estoque,
        "vendas": vendas,
        "vendedor": {
            "_id":seller["_id"],
            "cnpj": seller["cnpj"], 
            "nome": seller["nome"],
            "avaliacao": seller["avaliacao"]
        }
    }
    result = productCol.insert_one(mydoc)
    product_id = result.inserted_id 
    seller_product = {
        "_id": product_id,  
        "nome": nome,
        "marca": marca,
        "valor": valor,
        "estoque": estoque,
        "vendas": vendas
    }

    sellerCol.update_one({"cnpj": vendedor["cnpj"]}, {"$push": {"produtos": seller_product}})
    return print("Documento inserido com ID", product_id)

