from utils.utils import get_user
def update_user(session, user_id):
    try:
        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
        print(f"Atualize os dados do usuário com ID: {user_id}")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
        
        user = get_user(session, user_id)

        if user is None:
            print("Usuário não encontrado!")
            return None
        
        nome = input(f"Novo Nome (atual: {user.nome} ou Enter para manter): ") or user.nome
        email = input(f"Novo Email (atual: {user.email} ou Enter para manter): ") or user.email
        cpf = input(f"Novo CPF (atual: {user.cpf} ou Enter para manter): ") or user.cpf
        senha = input(f"Nova Senha (atual: {user.senha} ou Enter para manter): ") or user.senha

        endereco = user.endereco if user.endereco else [] 
        while True:
            print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
            print("Escolha uma opção:")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
            print("1. Adicionar novo endereço")
            print("2. Remover um endereço")
            print("3. Finalizar")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
            try:
                choice = int(input("Digite a opção desejada: "))
            except ValueError:
                print("Opção inválida! Escolha novamente.")
                continue
            
            if choice == "1":
                while True:
                    rua = input(f"Nova Rua: ")
                    numero = input(f"Novo Número: ")
                    tipo_imovel = input(f"Novo Tipo de imóvel: ")
                    complemento = input(f"Novo Complemento: ")
                    bairro = input(f"Novo Bairro: ")
                    cidade = input(f"Nova Cidade: ")
                    estado = input(f"Novo Estado: ")
                    
                    endereco.append({
                        "rua": rua,
                        "numero": numero,
                        "tipo_imovel": tipo_imovel,
                        "complemento": complemento,
                        "bairro": bairro,
                        "cidade": cidade,
                        "estado": estado
                    })
                    print("Endereço adicionado com sucesso!")
                    print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")

                    continuar = input("Deseja adicionar outro endereço? (s/n): ")
                    if continuar.lower() != 's':
                        break
        
            elif choice == "2":
                if endereco:
                    print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
                    print("Escolha um endereço para remover:")
                    print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
                    for idx, end in enumerate(endereco, start=1):
                        print(f"{idx} - {end['rua']}, {end['bairro']}, {end['cidade']}")

                    try:
                        index_to_remove = int(input(f"Digite o número do endereço a ser removido (ou 0 para cancelar): "))
                        if index_to_remove > 0 and index_to_remove <= len(endereco):
                            endereco.pop(index_to_remove - 1)  
                            print("Endereço removido com sucesso!")
                        else:
                            print("Opção inválida! Nenhum endereço foi removido.")
                    except ValueError:
                        print("Por favor, digite um número válido.")
                else:
                    print("Nenhum endereço para remover!")
            
            elif choice == "3":
                break
            else:
                print("Opção inválida! Tente novamente.")
        query = """
            UPDATE user
            SET nome = COALESCE(%s, nome),
                email = COALESCE(%s, email),
                cpf = COALESCE(%s, cpf),
                senha = COALESCE(%s, senha),
                endereco = COALESCE(%s, endereco),
                favoritos = COALESCE(%s, favoritos),
                compras = COALESCE(%s, compras)
            WHERE user_id = %s
        """
        session.execute(query, (nome, email, cpf, senha, endereco, user_id))
        
        print(f"Usuário com ID {user_id} atualizado com sucesso!")
        return 
    except Exception as e:
        print(f"Erro ao atualizar usuário: {e}")
        return None
