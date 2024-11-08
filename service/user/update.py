from utils.utils import get_user
from uuid import UUID

def update_user(session, user_id):
    try:
        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
        print(f"Atualize os dados do usuário com ID: {user_id}")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
        
        user = get_user(session, UUID(user_id))

        if user is None:
            print("Usuário não encontrado!")
            return None
        
        nome = input(f"Novo Nome (atual: {user.nome} ou Enter para manter): ") or user.nome
        email = input(f"Novo Email (atual: {user.email} ou Enter para manter): ") or user.email
        cpf = input(f"Novo CPF (atual: {user.cpf} ou Enter para manter): ") or user.cpf
        senha = input(f"Nova Senha (Enter para manter): ") or user.senha

        enderecos = user.enderecos if user.enderecos else []
        while True:
            print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
            print(" Escolha uma opção:")
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
            match choice:
                case 1:
                    while True:
                        rua = input("Nova Rua: ")
                        numero = input("Novo Número: ")
                        tipo_imovel = input("Novo Tipo de imóvel: ")
                        complemento = input("Novo Complemento: ")
                        bairro = input("Novo Bairro: ")
                        cidade = input("Nova Cidade: ")
                        estado = input("Novo Estado: ")
                        
                        enderecos.append({
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
        
                case 2:
                    if enderecos:
                        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
                        print("Escolha um endereço para remover:")
                        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
                        for idx, end in enumerate(enderecos, start=1):
                            print(f"{idx} - {end['rua']}, {end['bairro']}, {end['cidade']}")

                        try:
                            index_to_remove = int(input("Digite o número do endereço a ser removido (ou 0 para cancelar): "))
                            if 0 < index_to_remove <= len(enderecos):
                                enderecos.pop(index_to_remove - 1)
                                print("Endereço removido com sucesso!")
                            else:
                                print("Nenhum endereço foi removido.")
                        except ValueError:
                            print("Por favor, digite um número válido.")
                    else:
                        print("Nenhum endereço para remover!")
                
                case 3:
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
        
        query = """
            UPDATE user
            SET nome = %s, email = %s, cpf = %s, senha = %s, enderecos = %s
            WHERE id = %s
        """
    
        session.execute(query, (nome, email, cpf, senha, enderecos, UUID(user_id)))
        
        print(f"Usuário com ID {user_id} atualizado com sucesso!")
        return 
    except Exception as e:
        print(f"Erro ao atualizar usuário: {e}")
        return None
