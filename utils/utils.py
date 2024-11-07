def get_product(session,product_id):
    query = """
        SELECT * FROM products WHERE id = %s
    """
    product = session.execute(query, (product_id,)).one()
    return product if product else None

def get_seller(session, seller_id):
    query = """
        SELECT * FROM seller WHERE id = %s
    """
    seller = session.execute(query, (seller_id,)).one()
    return seller if seller else None

def get_purchase(session, purchase_id):
    query = """
        SELECT * FROM purchases WHERE id = %s
    """
    purchase = session.execute(query, (purchase_id,)).one()
    return purchase if purchase else None

def get_user(session, user_id):
    query = """
        SELECT * FROM user WHERE id = %s
    """
    user = session.execute(query, (user_id,)).one()
    return user if user else None