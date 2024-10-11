from Negocio.Usuario.create import create_user
from Negocio.Usuario.read import read_user
from Negocio.Usuario.update import update_user
from Negocio.Usuario.delete import delete_user
from Menu.Favoritos.favorito import manager_favorite

def manager_user(userCol, productCol):
    while True:
        print("-="*20)
        print("     Gerenciamento de Usuario")
        print("-="*20)
        print("1 - Criar novo usuario")
        print("2 - Ver usuario específico")
        print("3 - Atualizar usuario")
        print("4 - Deletar usuario")
        print("5 - Favoritos")
        print("6 - Sair")
        print("-="*20)
        
        try:
            opcao = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Opção inválida! Escolha novamente.")
            continue

        if opcao == 1:
            create_user(userCol)
        elif opcao == 2:
            cpf = input("Digite o CPF do usuario que deseja ver: ")
            if cpf:
                read_user(cpf, userCol)
        elif opcao == 3:
            cpf = input("Digite o CPF do usuario que deseja atualizar: ")
            if cpf:
                update_user(cpf, userCol)
        elif opcao == 4:
            cpf = input("Digite o CPF do usuario que deseja deletar: ")
            if cpf:
                delete_user(cpf, userCol)
        elif opcao == 5:
            cpf = input("Digite o CPF do usuario que deseja: ")
            if cpf:
                manager_favorite(cpf, userCol, productCol)
        elif opcao == 6:
            print("Saindo do gerenciamento de usuario.")
            break
        else:
            print("Opção inválida! Escolha novamente.")


