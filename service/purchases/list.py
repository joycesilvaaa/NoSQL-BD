from bson import ObjectId

def list_purchases(db_redis, user):
    user_purchase_key = f"user:{user['_id']}:purchases"
    purchase_keys = db_redis.lrange(user_purchase_key, 0, -1)

    if not purchase_keys:
        print("Nenhuma compra encontrada para o usuário.")
        return
    
    purchases = []
    
    for purchase_key in purchase_keys:
        purchase_data = db_redis.hgetall(purchase_key)
        purchase_id = ObjectId(purchase_key.decode('utf-8').split(":")[-1])
        
        compra = {
            "_id": purchase_id,
            "data_compra": purchase_data[b"data_compra"].decode('utf-8'),
            "nota_fiscal": purchase_data[b"nota_fiscal"].decode('utf-8'),
            "usuario": eval(purchase_data[b"usuario"].decode('utf-8')),  
            "produtos": eval(purchase_data[b"produtos"].decode('utf-8')),  
            "valor_total": purchase_data[b"valor_total"].decode('utf-8'), 
            "endereco_entrega": eval(purchase_data[b"endereco_entrega"].decode('utf-8')),
            "status": purchase_data[b"status"].decode('utf-8')
        }
        purchases.append(compra)

    if purchases:
        for i, purchase in enumerate(purchases, 1):
            print("-="*20)
            print("     Detalhes da Compra:")
            print("-="*20)
            print(f"Nota Fiscal: {purchase['nota_fiscal']}")
            print(f"Data da Compra: {purchase['data_compra']}")
            print(f"Usuário: {purchase['usuario']['nome']}")
            for index, product in enumerate(purchase["produtos"]):
                print(f"{index + 1} - Produto: {product['nome']}, Marca: {product['marca']}, Quantidade: {product['quantidade']}")
            print(f"Endereço de Entrega: {purchase['endereco_entrega']['rua']}, {purchase['endereco_entrega']['num']}")
            print(f"Valor Total: R$ {purchase['valor_total']}")
            print(f"Status: {purchase['status']}")
            print("-="*20)
    else:
        print("Nenhuma compra encontrada.")
