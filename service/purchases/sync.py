def sync_purchases(db_redis, user_col, user):
    user_purchase_key = f"user:{user['_id']}:purchases"
    
    purchase_keys = db_redis.lrange(user_purchase_key, 0, -1)

    purchase_details = []

    for purchase_key in purchase_keys:

        purchase_data = db_redis.hgetall(purchase_key)

        purchase_id = purchase_key.decode('utf-8').split(":")[-1]
        
        compra = {
            "_id": purchase_id,
            "data_compra": purchase_data["data_compra"].decode('utf-8'),
            "nota_fiscal": purchase_data["nota_fiscal"].decode('utf-8'),
            "usuario": eval(purchase_data["usuario"].decode('utf-8')),  
            "produtos": eval(purchase_data["produtos"].decode('utf-8')),  
            "valor_total": float(purchase_data["valor_total"].decode('utf-8')), 
            "endereco_entrega": eval(purchase_data["endereco_entrega"].decode('utf-8')),
            "status": purchase_data["status"].decode('utf-8')
        }

        purchase_details.append(compra)

    user_col.update_one(
        {"_id": user["_id"]},  
        {"$set": {"compras": purchase_details}}  
    )
    print("Sincronização das compras com o MongoDB realizada com sucesso!")
