def read_purchase(session):
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("         Listagem de Compras")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    try:
        query = """
        MATCH (u:User)-[:COMPROU]->(c:Purchase)-[:INCLUI]->(p:Product)
        RETURN u.nome AS user_name, c.valor_total AS total_value, c.status AS status,
               COLLECT({product_name: p.nome, price: p.preco, brand: p.marca}) AS products
        """
        result = session.run(query)
        purchases = result.data()

        if not purchases:
            print("Nenhuma compra encontrada!")
            return

        for purchase in purchases:
            print("\n--- Compra ---")
            print(f"Usuário: {purchase['user_name']}")
            print(f"Valor Total: R${purchase['total_value']}")
            print(f"Status: {purchase['status']}")
            print("Produtos:")
            for product in purchase['products']:
                print(f"  - Nome: {product['product_name']}, Preço: R${product['price']}, Marca: {product['brand']}")

    except Exception as e:
        print(f"Erro ao listar as compras: {e}")
