from datetime import datetime
from bson import ObjectId
from helpers.utils import generate_nota_fical, find_user, find_product, calculate_final_value, list_addresses, register_address
from Negocio.Produto.read import list_products
from Negocio.Produto.update import update_sale_and_stock

def create_purchase(user, userCol, productCol, purchaseCol):
    print("-=" * 20)
    print("     Inserindo uma nova compra")
    print("-=" * 20)
    list_products(productCol)
    
    shopping_cart = []  
    value_purchase = 0 

    while True:
        product_id = input("Digite o ID do produto que deseja comprar: ")
        product = find_product(product_id, productCol)
        if not product:
            print("Produto não encontrado!")
            continue  
        
        quantity = int(input("Digite a quantidade que deseja comprar: "))
        shopping_cart.append({"product": product, "quantity": quantity})
        
        continue_process = input("Deseja selecionar mais algum produto? (S/N) ").lower()
        if continue_process == "n":
            break

    addresses = list_addresses(user)
    
    if not addresses:
        print("Registrar novo endereço de entrega:")
        print("-="*20)
        endereco = register_address(user["cpf"], userCol, "USER")
        userCol.update_one({"_id": user["_id"]}, {"$push": {"end": endereco}})
        print("-="*20)
        print("Endereço cadastrado com sucesso!")
        user = find_user(user["cpf"], userCol)
        addresses = list_addresses(user)

    print("-="*20)
    print("     Endereços disponíveis: ")
    print("-="*20)
    for index, address in enumerate(addresses):
        print(f"ID {index}. Rua: {address.get('rua')}, Número: {address.get('num')}, Bairro: {address.get('bairro')}, Cidade: {address.get('cidade')}, Estado: {address.get('estado')}")
    print("-="*20)
    
    delivery_address_id = int(input("Digite o ID do endereço de entrega: "))
    if delivery_address_id < 0 or delivery_address_id >= len(addresses):
        return print("Endereço de entrega inválido!")
    
    delivery_address_final = addresses[delivery_address_id]
    date_purchase = datetime.now()
    nota_fiscal = generate_nota_fical()

    for item in shopping_cart:
        product = item["product"]
        quantity = item["quantity"]
        value_purchase += calculate_final_value(product, quantity)
        
    user_data = {
        "_id":user["_id"],
        "nome": user["nome"],
        "email": user["email"],
        "cpf": user["cpf"]
    }

    product_list = []
    for item in shopping_cart:
        product = item["product"]
        quantity = item["quantity"]
        
        product_data = {
            "_id":product["_id"],
            "nome": product["nome"],
            "marca": product["marca"],
            "valor": product["valor"],
            "quantidade": quantity,
            "vendedor": {
                "_id":product["vendedor"]["_id"],
                "cnpj": product["vendedor"]["cnpj"],
                "nome": product["vendedor"]["nome"],
                "avaliacao": product["vendedor"]["avaliacao"]
            }
        }
        product_list.append(product_data)

    compra = {
        "data_compra": date_purchase,
        "nota_fiscal": nota_fiscal,
        "usuario": user_data,
        "produtos": product_list,  
        "valor_total": value_purchase,
        "endereco_entrega": delivery_address_final,
        "status": "Processando"
    }

    result = purchaseCol.insert_one(compra)
    purchase_id = result.inserted_id  
    compra_user = {
        "_id": purchase_id, 
        "data_compra": date_purchase,
        "nota_fiscal": nota_fiscal,
        "produtos": product_list,  
        "valor_total": value_purchase,
        "endereco_entrega": delivery_address_final,
        "status": "Processando"
    }
    userCol.update_one({"_id": user["_id"]}, {"$push": {"compras": compra_user}})

    for item in shopping_cart:
        product = item["product"]
        quantity = item["quantity"]
        update_sale_and_stock(product, quantity, productCol)
    print("-="*20)
    print(f"Documento inserido com ID {result.inserted_id}")
    print("-="*20)



