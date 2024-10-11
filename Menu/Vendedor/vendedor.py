from Negocio.Vendedor.create import create_seller
from Negocio.Vendedor.read import read_seller, read_sellers
from Negocio.Vendedor.update import update_seller
from Negocio.Vendedor.delete import delete_seller

def manager_seller(collection):
    while True:
        print("-="*20)
        print("     Gerenciamento de Vendedores")
        print("-="*20)
        print("1 - Criar novo vendedor")
        print("2 - Ver vendedor específico")
        print("3 - Atualizar vendedor")
        print("4 - Deletar vendedor")
        print("5 - Lista de vendedores")
        print("6 - Sair")
        print("-="*20)
        
        try:
            opcao = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Opção inválida! Escolha novamente.")
            continue

        if opcao == 1:
            create_seller(collection)
        elif opcao == 2:
            seller_cnpj = input("Digite o CNPJ do vendedor que deseja ver: ")
            if seller_cnpj:
                read_seller(seller_cnpj, collection)
        elif opcao == 3:
            seller_cnpj = input("Digite o CNPJ do vendedor que deseja atualizar: ")
            if seller_cnpj:
                update_seller(seller_cnpj, collection)
        elif opcao == 4:
            seller_cnpj = input("Digite o CNPJ do vendedor que deseja deletar: ")
            if seller_cnpj:
                delete_seller(seller_cnpj, collection)
        elif opcao ==5:
            read_sellers(collection)
        elif opcao == 6:
            print("-="*20)
            print("Saindo do gerenciamento de vendedores.")
            break
        else:
            print("Opção inválida! Escolha novamente.")
