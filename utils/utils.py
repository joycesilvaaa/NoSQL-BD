def create_user(session, nome, email, cpf, senha):
    query = """
    CREATE (u:User {nome: $nome, email: $email, cpf: $cpf, senha: $senha})
    RETURN elementId(u) as user_id
    """
    result = session.run(query, nome=nome, email=email, cpf=cpf, senha=senha)
    user_id = result.single()['user_id']
    return user_id

def create_product(session, cnpj, nome_produto, preco, marca):
    query = """
    MATCH (v:Seller {cnpj: $cnpj})
    CREATE (p:Product {nome: $nome_produto, preco: $preco, marca: $marca})
    CREATE (v)-[:VENDE]->(p)
    RETURN elementId(p) AS product_id
    """
    result = session.run(query, cnpj=cnpj, nome_produto=nome_produto, preco=preco, marca=marca)
    product_id = result.single()['product_id']
    return product_id


def create_purchase(session, cpf, nomes_produtos, valor_total, status):
    query = """
    MATCH (u:User {cpf: $cpf})  
    UNWIND $nomes_produtos AS nome_produto
    MATCH (p:Product {nome: nome_produto})  
    CREATE (c:Purchase {data: datetime(), valor_total: $valor_total, status: $status})
    CREATE (u)-[:COMPROU]->(c) 
    CREATE (c)-[:INCLUI]->(p) 
    RETURN elementId(c) AS purchase_id
    """
    result = session.run(query, cpf=cpf, nomes_produtos= nomes_produtos,valor_total=valor_total, status=status )
    purchase_id = result.single()['purchase_id']
    return purchase_id

def create_seller(session, nome, email, cnpj, telefone):
    query = """
        CREATE (s:Seller {
            nome: $nome,
            email: $email,
            cnpj: $cnpj,
            telefone: $telefone
        })RETURN elementId(s) as seller_id
    """
    result = session.run(query, 
                nome=nome,
                email=email,
                cnpj=cnpj,
                telefone=telefone)
    seller_id = result.single()["seller_id"]
    return seller_id



