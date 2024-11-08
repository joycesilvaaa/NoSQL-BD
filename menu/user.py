from service.user.create import create_user
from service.user.update import update_user 
from utils.utils import list_users
def manager_user(session):
    while True:
        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
        print("1. Criar usuario")
        print("2. Atualizar usuario")
        print("3. Voltar ao menu principal")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")

        try:
            choice = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Opção inválida! Escolha novamente.")
            continue

        match choice:
            case 1:
                create_user(session)
                break
            case 2:
                users = list_users(session)
                if users is None:
                    break
                user_id = input("Digite o ID do usuario: ").strip()
                update_user(session, user_id)
                break
            case 3:
                break