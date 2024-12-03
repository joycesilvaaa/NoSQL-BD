def read_seller(session):
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("        Listagem de Vendedores")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    
    try:
        query = """
        MATCH (s:Seller)
        RETURN elementId(s) AS id, s.nome AS nome, s.email AS email, s.cnpj AS cnpj, s.telefone AS telefone
        """
        result = session.run(query)
        
        sellers = result.data()

        if not sellers:
            print("Nenhum vendedor encontrado!")
            return
        
        print("\nVendedores Disponíveis:")
        print("-" * 50)
        for seller in sellers:
            print(f"ID: {seller['id']}")
            print(f"Nome: {seller['nome']}")
            print(f"E-mail: {seller['email']}")
            print(f"CNPJ: {seller['cnpj']}")
            print(f"Telefone: {seller['telefone']}")
            print("-" * 50)

    except Exception as e:
        print(f"Erro ao buscar informações do vendedor: {e}")
