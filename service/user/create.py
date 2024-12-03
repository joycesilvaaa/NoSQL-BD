from utils.utils import create_user 

def create_user_form(session):
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("         Cadastro de Usuário ")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    
    nome = input("Digite o nome do usuário: ").strip()
    email = input("Digite o email do usuário: ").strip()
    cpf = input("Digite o CPF do usuário: ").strip()
    senha = input("Digite a senha do usuário: ").strip()

    try:
        user_id = create_user(session, nome, email, cpf, senha)
        print(f"Usuário e endereço criados com sucesso! ID do Usuário: {user_id}.")
    except Exception as e:
        print(f"Erro ao criar o usuário ou o endereço: {e}")
