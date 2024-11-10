from service.purchases.delete import delete_purchase
from service.purchases.create import create_purchase
from utils.utils import list_purchases, list_users

def manager_purchases(session):
    while True:
        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
        print("1. Criar compra")
        print("2. Listagem de todas")
        print("3. Deletar compra")
        print("4. Voltar ao menu principal")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")

        try:
            choice = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Opção inválida! Escolha novamente.")
            continue

        match choice:
            case 1:
                users = list_users(session)
                if users is None:
                    break
                user_id = input("Digite o ID do usuario: ").strip()
                create_purchase(session, user_id)
            case 2:
                list_purchases(session)
            case 3:
                purchases = list_purchases(session)
                if purchases is None:
                    return
                purchase_id = input("Digite o Id da compra que deseja deletar: ").strip()
                delete_purchase(session, purchase_id)
            case 4:
                break