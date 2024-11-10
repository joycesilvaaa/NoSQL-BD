from cassandra.util import OrderedMapSerializedKey

def convert_ordered_map_to_dict(ordered_map):
    if isinstance(ordered_map, OrderedMapSerializedKey):
        return dict(ordered_map)
    return ordered_map 

def row_to_dict_user(row):
    row_dict = {
        "id": str(row.id), 
        "compras": row.compras,
        "cpf": row.cpf,
        "email": row.email,
        "enderecos": [convert_ordered_map_to_dict(endereco) for endereco in row.enderecos],
        "favoritos": row.favoritos,
        "nome": row.nome,
        "senha": row.senha,
    }
    return row_dict

def row_to_dict_seller(row):
    row_dict = {
        "id": str(row.id),  
        "nome": row.nome, 
        "email": row.email, 
        "cnpj": row.cnpj,  
        "avaliacao": row.avaliacao,  
        "enderecos": [convert_ordered_map_to_dict(endereco) for endereco in row.enderecos] if row.enderecos else [], 
        "produtos": [convert_ordered_map_to_dict(produto) for produto in row.produtos] if row.produtos else [], 
    }
    return row_dict

def row_to_dict_purchase(row):
    row_dict = {
        "id": str(row.id), 
        "data_compra": row.data_compra,  
        "valor_total": row.valor_total,
        "status": row.status,  
        "user_id": row.user_id,
        "endereco_entrega": convert_ordered_map_to_dict(row.endereco_entrega) if row.endereco_entrega else {},
        "produtos": [convert_ordered_map_to_dict(produto) for produto in row.produtos] if row.produtos else []
    }
    return row_dict

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
        SELECT * FROM purchase WHERE id = %s
    """
    purchase = session.execute(query, (purchase_id,)).one()
    return purchase if purchase else None

def get_user(session, user_id):
    query = """
        SELECT * FROM user WHERE id = %s
    """
    user = session.execute(query, (user_id,)).one()
    return user if user else None

def get_all_users(session):
    query = "SELECT * FROM user"
    users = session.execute(query)  
    return list(users)

def get_all_sellers(session):
    query = "SELECT * FROM seller"
    sellers = session.execute(query)  
    return list(sellers)

def get_all_purchases(session):
    query = "SELECT * FROM purchase"
    purchases = session.execute(query)  
    return list(purchases)

def get_all_products(session):
    query = "SELECT * FROM products"
    products = session.execute(query)
    return list(products)

def list_users(session):
    users = get_all_users(session)
    if not users:
        print("Nenhum usuário cadastrado.")
        return None
    for user in users:
        user_dict = row_to_dict_user(user)
        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
        print(f"| ID: {user_dict['id']}")
        print(f"| Nome: {user_dict['nome']}")
        print(f"| E-mail: {user_dict['email']}")
    return users


def list_sellers(session):
    sellers = get_all_sellers(session)
    if not sellers:
        print("Nenhum vendedor cadastrado.")
        return None
    for seller in sellers:
        seller_dict = row_to_dict_seller(seller)
        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
        print(f"| ID: {seller_dict['id']}")
        print(f"| Nome: {seller_dict['nome']}")
        print(f"| E-mail: {seller_dict['email']}")
    return sellers

def list_purchases(session):
    purchases = get_all_purchases(session)
    if not purchases:
        print("Nenhuma compra cadastrada.")
        return None
    for purchase in purchases:
        purchase_dict = row_to_dict_purchase(purchase)
        user = get_user(session, purchase_dict['user_id'])
        user_dict = row_to_dict_user(user)
        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
        print(f"| ID: {purchase_dict['id']}")
        print(f"| Data: {purchase_dict['data_compra']}")
        print(f"| Valor: {purchase_dict['valor_total']}")
        print(f"| Comprador: {user_dict['nome']}")
    return purchases

def list_products(session):
    products = get_all_products(session)
    if not products:
        print("Nenhum produto cadastrado.")
        return None
    for product in products:
        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
        print(f"| ID: {product.id}") 
        print(f"| Nome: {product.nome_produto}") 
        print(f"| Valor: {product.valor:.2f}")  
        print(f"| Vendedor: {product.nome_vendedor}")  
    return products

def update_sale_and_stock(session, product_id, quantity):
    query = f"SELECT estoque, vendas FROM products WHERE id = %s"
    result = session.execute(query, (product_id,))
    if not result:
        print(f"Produto não encontrado.")
        return
    product = result[0]
    estoque = product.estoque
    vendas = product.vendas
        
    new_estoque = estoque - quantity
    new_vendas = vendas + quantity

    update_query = f"""
            UPDATE products
            SET estoque = %s, vendas = %s
            WHERE id = %s
        """     
    session.execute(update_query, (new_estoque, new_vendas, product_id))

