from cassandra.util import OrderedMapSerializedKey

def convert_ordered_map_to_dict(ordered_map):
    if isinstance(ordered_map, OrderedMapSerializedKey):
        return dict(ordered_map)
    return ordered_map 

def row_to_dict(row):
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
    return row_to_dict(user) if user else None

def get_all_users(session):
    query = "SELECT * FROM user"
    users = session.execute(query)  
    return list(users)



def list_users(session):
    users = get_all_users(session)
    if not users:
        return None
    for user in users:
        user_dict = row_to_dict(user)
        user_id = user_dict["id"]  
        user_name = user_dict["nome"]
        print(f"ID: {user_id}, Nome: {user_name}")
    return users
