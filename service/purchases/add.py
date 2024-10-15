from utils.utils import list_products, find_product, list_addresses, generate_nota_fical, calculate_final_value, update_sale_and_stock
from datetime import datetime

def add_purchase(product_col, purchase_col, db_redis, user):
    list_products(product_col)

    shopping_cart = []  
    value_purchase = 0 

    while True:
        product_id = input("Digite o ID do produto que deseja comprar: ")
        product = find_product(product_id, product_col)
        if not product:
            print("Produto não encontrado!")
            continue  
        
        quantity = int(input("Digite a quantidade que deseja comprar: "))
        shopping_cart.append({"product": product, "quantity": quantity})
        
        continue_process = input("Deseja selecionar mais algum produto? (S/N) ").lower()
        if continue_process == "n":
            break

    list_addresses(user)

    delivery_address_id = int(input("Digite o ID do endereço de entrega: "))
    if delivery_address_id < 0 or delivery_address_id >= len(user['end']):
        return print("Endereço de entrega inválido!")
    
    delivery_address_final = user['end'][delivery_address_id]
    date_purchase = datetime.now()
    nota_fiscal = generate_nota_fical()

    for item in shopping_cart:
        product = item["product"]
        quantity = item["quantity"]
        value_purchase += calculate_final_value(product, quantity)

    user_data = {
        "_id": user["_id"],
        "nome": user["nome"],
        "email": user["email"],
        "cpf": user["cpf"]
    }

    product_list = []
    for item in shopping_cart:
        product = item["product"]
        quantity = item["quantity"]
        
        product_data = {
            "_id": product["_id"],
            "nome": product["nome"],
            "marca": product["marca"],
            "valor": product["valor"],
            "quantidade": quantity,
            "vendedor": {
                "_id": product["vendedor"]["_id"],
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

    result = purchase_col.insert_one(compra)
    purchase_id = result.inserted_id 

    redis_key = f"user:{user['_id']}:purchases:{purchase_id}"

    db_redis.hmset(redis_key, {
        "data_compra": date_purchase.strftime("%Y-%m-%d %H:%M:%S"),
        "nota_fiscal": nota_fiscal,
        "usuario": str(user_data),  
        "produtos": str(product_list),  
        "valor_total": value_purchase,
        "endereco_entrega": str(delivery_address_final),
        "status": "Processando"
    })

    user_purchase_key = f"user:{user['_id']}:purchases"
    db_redis.rpush(user_purchase_key, redis_key) 

    for item in shopping_cart:
        product = item["product"]
        quantity = item["quantity"]
        update_sale_and_stock(product, quantity, product_col)
    print("-="*20)
    print("Compra realizada com sucesso!")
    print("-="*20)

    
