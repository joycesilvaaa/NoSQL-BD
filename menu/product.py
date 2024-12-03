from service.product.create import create_product_form
from service.product.read import read_product

def manager_product(session):
    while True:
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("      Gerenciamento de Produtos")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("1. Criar Produto")
        print("2. Visualizar Produtos")
        print("0. Voltar")
        
        choice = input("Escolha uma opção: ").strip()
        
        if choice == '1':
            create_product_form(session) 
        elif choice == '2':
            read_product(session)
        elif choice == '0':
            print("Voltando ao menu anterior...")
            break 
        else:
            print("Opção inválida! Tente novamente.")
