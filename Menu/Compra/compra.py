from Negocio.Compra.create import create_purchase
from Negocio.Compra.read import read_purchase
from Negocio.Compra.update import update_purchase
from Negocio.Compra.delete import delete_purchase
from helpers.utils import find_user

def manager_purchase(userCol, productCol, purchaseCol):
    while True:
        print("-="*20)
        print("     Gerenciamento de Compras")
        print("-="*20)
        print("1 - Criar nova compra")
        print("2 - Ver compra específica")
        print("3 - Atualizar status da compra")
        print("4 - Deletar compra")
        print("5 - Sair")
        print("-="*20)
        
        try:
            opcao = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Opção inválida! Escolha novamente.")
            continue

        if opcao == 1:
            cpf = input("Digite o CPF do cliente para gerenciar suas compras: ")
            user = find_user(cpf, userCol)
            if not user:
                print("Usuário não encontrado!")
                continue
            create_purchase(user, userCol, productCol, purchaseCol)
        
        elif opcao == 2:
            nota_fiscal = input("Digite a nota fiscal da compra que deseja ver: ")
            if nota_fiscal:
                read_purchase(nota_fiscal, purchaseCol)
        
        elif opcao == 3:
            nota_fiscal = input("Digite a nota fiscal da compra que deseja atualizar: ")
            if nota_fiscal:
                cpf = input("Digite o CPF do cliente para atualizar a compra: ")
                user = find_user(cpf, userCol) 
                if user:
                    update_purchase(user, userCol, nota_fiscal, purchaseCol)
                else:
                    print("Usuário não encontrado!")
        
        elif opcao == 4:
            nota_fiscal = input("Digite a nota fiscal da compra que deseja deletar: ")
            if nota_fiscal:
                cpf = input("Digite o CPF do cliente para atualizar a compra: ")
                user = find_user(cpf, userCol)  
                if user:
                    delete_purchase(user, userCol, nota_fiscal, purchaseCol)
                else:
                    print("Usuário não encontrado!")
        
        elif opcao == 5:
            print("Saindo do gerenciamento de compras.")
            break
        
        else:
            print("Opção inválida! Escolha novamente.")
