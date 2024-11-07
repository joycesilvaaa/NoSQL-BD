from cassandra.util import uuid4

def create_user(session):
    try:
        user_id = uuid4() 
        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
        print("Informe os dados do novo usuário:")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
        nome = input("Nome: ")
        email = input("Email: ")
        cpf = input("CPF: ")
        senha = input("Senha: ")
        endereco = []
        while True:
            print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
            rua = input("Rua: ")
            numero = input("Número: ")
            tipo_imovel = input("Tipo de imóvel: ")
            complemento = input("Complemento (deixe em branco se não houver): ")
            bairro = input("Bairro: ")
            cidade = input("Cidade: ")
            estado = input("Estado: ")

            endereco.append({
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

        favoritos = []
        compras = []
        query = """
            INSERT INTO user (user_id, nome, email, cpf, senha, endereco, favoritos, compras)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        session.execute(query, (user_id, nome, email, cpf, senha, endereco, favoritos, compras))
        
        print(f"Usuário criado com sucesso! ID: {user_id}")
        return 
    except Exception as e:
        print(f"Erro ao criar usuário: {e}")
        return None
