def list_purchases(db_redis, user):
    user_purchase_key = f"user:{user['_id']}:purchases"
    purchase_keys = db_redis.lrange(user_purchase_key, 0, -1)

    if not purchase_keys:
        print("Nenhuma compra encontrada para o usuário.")
        return
    
    purchases = []
    
    for purchase_key in purchase_keys:
        purchase_details = db_redis.hgetall(purchase_key) 
        if purchase_details:
            purchases.append(purchase_details)

    if purchases:
        for i, purchase in enumerate(purchases, 1):
            print(f"Compra {i}: {purchase}")
    else:
        print("Nenhuma compra encontrada.")