def read_product(session):
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("         Listagem de Produtos")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    
    query = """
    MATCH (v:Seller)-[:VENDE]->(p:Product)
    RETURN v.cnpj AS seller_cnpj, v.nome AS seller_name, 
           p.nome AS product_name, p.preco AS price, p.marca AS brand
    """
    
    try:
        result = session.run(query)
        
        for record in result:
            print(f"Vendedor: {record['seller_name']} (CNPJ: {record['seller_cnpj']})")
            print(f"  Produto: {record['product_name']}")
            print(f"  Preço: R$ {record['price']}")
            print(f"  Marca: {record['brand']}")
            print("-" * 30)
    
    except Exception as e:
        print(f"Erro ao listar os produtos: {e}")
