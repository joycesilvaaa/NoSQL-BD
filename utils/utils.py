# Função para criar um usuário
def create_user(session, nome, email, cpf, senha):
    query = """
    CREATE (u:User {nome: $nome, email: $email, cpf: $cpf, senha: $senha})
    RETURN u.id AS user_id
    """
    result = session.run(query, nome=nome, email=email, cpf=cpf, senha=senha)
    user_id = result.single()['user_id']
    return user_id

# Função para criar um endereço
def create_address(session, rua, cidade, estado, cep):
    query = """
    CREATE (a:Address {rua: $rua, cidade: $cidade, estado: $estado, cep: $cep})
    RETURN a.id AS address_id
    """
    result = session.run(query, rua=rua, cidade=cidade, estado=estado, cep=cep)
    address_id = result.single()['address_id']
    return address_id

# Função para criar um produto
def create_product(session, nome_produto, marca_produto, valor, estoque):
    query = """
    CREATE (p:Product {nome_produto: $nome_produto, marca_produto: $marca_produto, valor: $valor, estoque: $estoque})
    RETURN p.id AS product_id
    """
    result = session.run(query, nome_produto=nome_produto, marca_produto=marca_produto, valor=valor, estoque=estoque)
    product_id = result.single()['product_id']
    return product_id

# Função para criar uma compra
def create_purchase(session, user_id, valor_total, status):
    query = """
    CREATE (c:Purchase {user_id: $user_id, valor_total: $valor_total, status: $status})
    RETURN c.id AS purchase_id
    """
    result = session.run(query, user_id=user_id, valor_total=valor_total, status=status)
    purchase_id = result.single()['purchase_id']
    return purchase_id

# Função para criar um relacionamento de compra entre um usuário e um produto
def link_purchase_product(session, purchase_id, product_id, quantidade):
    # Decrementar o estoque do produto e incrementar as vendas com base na quantidade
    update_query = """
    MATCH (p:Product {id: $product_id})
    SET p.estoque = p.estoque - $quantidade,
        p.vendas = p.vendas + $quantidade
    """
    session.run(update_query, product_id=product_id, quantidade=quantidade)
    
    # Criar o relacionamento de compra entre a compra e o produto
    query = """
    MATCH (p:Product {id: $product_id}), (c:Purchase {id: $purchase_id})
    CREATE (c)-[:CONTAINS {quantidade: $quantidade}]->(p)
    """
    session.run(query, purchase_id=purchase_id, product_id=product_id, quantidade=quantidade)

# Função para criar um relacionamento de residência entre um usuário e um endereço
def link_user_address(session, user_id, address_id):
    query = """
    MATCH (u:User {id: $user_id}), (a:Address {id: $address_id})
    CREATE (u)-[:LIVES_AT]->(a)
    """
    session.run(query, user_id=user_id, address_id=address_id)

# Função para criar um usuário com endereço
def create_user_with_address(session, nome, email, cpf, senha, rua, cidade, estado, cep):
    # Cria o usuário
    user_id = create_user(session, nome, email, cpf, senha)
    
    # Cria o endereço
    address_id = create_address(session, rua, cidade, estado, cep)
    
    # Cria o relacionamento entre o usuário e o endereço
    link_user_address(session, user_id, address_id)
    return user_id, address_id

# Função para criar um produto e vincular a um vendedor (vendedor_id)
def create_product_and_link(session, nome_produto, marca_produto, valor, estoque, vendedor_id):
    # Cria o produto
    product_id = create_product(session, nome_produto, marca_produto, valor, estoque)
    
    # Aqui você pode criar um relacionamento entre o vendedor e o produto se necessário
    # Por exemplo:
    # link_product_seller(session, product_id, vendedor_id)
    
    return product_id

# Função para criar uma compra com múltiplos produtos e vincular os produtos à compra
def create_purchase_with_products(session, user_id, valor_total, status, products):
    """
    Cria uma compra e vincula múltiplos produtos à compra.
    `products` é uma lista de tuplas (product_id, quantidade).
    """
    # Cria a compra
    purchase_id = create_purchase(session, user_id, valor_total, status)
    
    # Vincula cada produto à compra
    for product_id, quantidade in products:
        link_purchase_product(session, purchase_id, product_id, quantidade)
    
    return purchase_id

# Função para recuperar as informações de um usuário
def get_user_info(session, user_id):
    query = """
    MATCH (u:User {id: $user_id})-[:LIVES_AT]->(a:Address),
          (u)-[:FRIEND]->(f:User),
          (u)-[:PURCHASED]->(p:Product)
    RETURN u, a, f, p
    """
    result = session.run(query, user_id=user_id)
    return result

