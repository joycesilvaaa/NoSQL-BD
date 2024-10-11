from Negocio.Produto.create import create_product
from Negocio.Produto.update import update_product
from Negocio.Produto.read import read_product, list_products
from Negocio.Produto.delete import delete_product
from helpers.utils import find_seller

def manager_product(productCol,sellerCol):
    while True:
        print("-="*20)
        print("     Gerenciamento de Produtos")
        print("-="*20)
        print("1 - Criar novo produto")
        print("2 - Ver produto específico")
        print("3 - Atualizar produto")
        print("4 - Deletar produto")
        print("5 - Sair")
        print("-="*20)
        
        try:
            opcao = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Opção inválida! Escolha novamente.")
            continue

        if opcao == 1:
            cnpj =input("Digite o cnpj do vendedor: ")
            seller = find_seller(cnpj,sellerCol)
            if seller:
                create_product(seller, productCol, sellerCol)
        elif opcao == 2:
            list_products(productCol)
            product_id = str(input("Digite o id do produto que deseja ver: "))
            if product_id:
                read_product(product_id, productCol)
        elif opcao == 3:
            list_products(productCol)
            product_id = str(input("Digite o id do produto que deseja ver: "))
            if product_id:
                update_product(product_id, productCol, sellerCol)
        elif opcao == 4:
            list_products(productCol)
            product_id = str(input("Digite o id do produto que deseja ver: "))
            if product_id:
                delete_product(product_id, productCol, sellerCol)
        elif opcao == 5:
            print("Saindo do gerenciamento de usuários.")
            break
        else:
            print("Opção inválida! Escolha novamente.")
