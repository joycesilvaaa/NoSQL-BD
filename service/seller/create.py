from uuid import uuid4

def create_seller(session):
    try:
        seller_id = uuid4() 
        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
        print("Informe os dados do novo vendedor:")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
        
        nome = input("Nome: ")
        email = input("Email: ")
        cnpj = input("CNPJ: ")
        avaliacao = 5
        
        enderecos = []
        while True:
            print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
            rua = input("Rua: ")
            numero = input("Número: ")
            tipo_imovel = input("Tipo de imóvel: ")
            complemento = input("Complemento (deixe em branco se não houver): ")
            bairro = input("Bairro: ")
            cidade = input("Cidade: ")
            estado = input("Estado: ")

            enderecos.append({
                "rua": rua,
                "numero": numero,
                "tipo_imovel": tipo_imovel,
                "complemento": complemento,
                "bairro": bairro,
                "cidade": cidade,
                "estado": estado
            })

            continuar = input("Deseja adicionar outro endereço? (s/n): ")
            if continuar.lower() != 's':
                break
        
        produtos = []        
        query = """
            INSERT INTO seller (id, nome, email, cnpj, avaliacao, enderecos, produtos)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        session.execute(query, (seller_id, nome, email, cnpj, avaliacao, enderecos, produtos))
        
        print(f"Vendedor criado com sucesso! ID: {seller_id}")
        return
    except Exception as e:
        print(f"Erro ao criar vendedor: {e}")
        return None

