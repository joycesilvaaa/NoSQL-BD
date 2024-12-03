from service.seller.create import create_seller_form
from service.seller.read import read_seller
def manager_seller(session):
    while True:
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("     Gerenciamento de Vendedores")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("1. Criar Vendedor")
        print("2. Visualizar Vendedores")
        print("0. Voltar")
        
        choice = input("Escolha uma opção: ").strip()
        
        if choice == '1':
            create_seller_form(session)  # Chama a função para criar um vendedor
        elif choice == '2':
            read_seller(session)  # Chama a função para visualizar os vendedores
        elif choice == '0':
            print("Voltando ao menu anterior...")
            break  # Sai do loop e volta para o menu anterior
        else:
            print("Opção inválida! Tente novamente.")
