

def read_usuario(session):
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("          Listagem de Usuarios")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    
    try:
        query = """
            MATCH (u:User)
            RETURN elementId(u) AS id, u.nome AS nome, u.email AS email, u.cpf AS cpf
        """
        result = session.run(query)
        
        usuarios = result.data()
        
        if not usuarios:
            print("Nenhum usuário encontrado!")
            return
        
        print("Usuários Disponíveis:")
        print("-" * 50)
        for usuario in usuarios:
            id = usuario['id']
            nome = usuario['nome']
            email = usuario['email'] 
            cpf = usuario['cpf']  
            print(f"ID: {id}")
            print(f"Nome: {nome}")
            print(f"Email: {email}")
            print(f"CPF: {cpf}")
            print("-" * 50) 
    
    except Exception as e:
        print(f"Erro ao buscar informações do usuário: {e}")
