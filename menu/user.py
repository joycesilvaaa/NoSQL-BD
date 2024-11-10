from service.user.create import create_user
from service.user.update import update_user 
from utils.utils import list_users
from service.user.read import read_user
def manager_user(session):
    while True:
        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
        print("1. Criar usuario")
        print("2. Atualizar usuario")
        print("3. Ver usuario")
        print("4. Listagem de todos os usuarios")
        print("5. Voltar ao menu principal")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")

        try:
            choice = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Opção inválida! Escolha novamente.")
            continue

        match choice:
            case 1:
                create_user(session)
            case 2:
                users = list_users(session)
                if users is None:
                    break
                user_id = input("Digite o ID do usuario: ").strip()
                update_user(session, user_id)
            case 3:
                users = list_users(session)
                if users is None:
                    break
                user_id = input("Digite o ID do usuario: ").strip()
                read_user(session, user_id)
            case 4:
                list_users(session)
            case 5:
                break