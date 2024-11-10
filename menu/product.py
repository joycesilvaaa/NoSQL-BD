from service.product.create import create_product
from service.product.read import read_product
from utils.utils import list_products, list_sellers

def manager_product(session):
    while True:
        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
        print("1. Criar produto")
        print("2. Buscar produto")
        print("3. Listagem")
        print("4. Voltar ao menu principal")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")

        try:
            choice = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Opção inválida! Escolha novamente.")
            continue

        match choice:
            case 1:
                sellers = list_sellers(session)
                if sellers is None:
                    return
                seller_id = input("Digite o Id do vendedor: ").strip()
                create_product(session,seller_id)
            case 2:
                products = list_products(session)
                if products is None:
                    return
                product_id = input("Digite o Id do produto: ").strip()
                read_product(session, product_id)
            case 3:
                list_products(session)
            case 4:
                 break           