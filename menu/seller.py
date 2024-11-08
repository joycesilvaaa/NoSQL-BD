from service.seller.create import create_seller
from service.seller.read import read_seller
from utils.utils import list_sellers

def manager_seller(session):
    while True:
        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
        print("1. Criar vendedor")
        print("2. Buscar vendedor")
        print("3. Listagem de todos")
        print("4. Voltar ao menu principal")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")

        try:
            choice = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Opção inválida! Escolha novamente.")
            continue

        match choice:
            case 1:
                create_seller(session)
                break
            case 2:
                sellers = list_sellers(session)
                if sellers is None:
                    break
                seller_id = input("Digite o ID do vendedor: ").strip()
                read_seller(session, seller_id)
                break
            case 3:
                list_sellers(session)
                break
            case 4:
                break