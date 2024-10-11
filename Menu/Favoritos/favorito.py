from Negocio.Favorito.list import list_favorite
from Negocio.Favorito.add import add_favorite
from Negocio.Favorito.remove import remove_favorite
from helpers.utils import find_user

def manager_favorite(userCpf, userCol, productCol):
    user = find_user(userCpf,userCol)
    if not user:
        return print("Usuario não encontrado!")
    while True:
        print("-="*20)
        print("1 - Exibir favoritos")
        print("2 - Adicionar produto aos favoritos")
        print("3 - Remover produto dos favoritos")
        print("4 - Sair")
        print("-="*20)

        try:
            choice = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Opção inválida! Escolha um número entre 1 e 4.")
            continue
        
        if choice == 1:
            user = find_user(userCpf, userCol)
            list_favorite(user)  
        elif choice == 2:
            add_favorite(user, userCol, productCol)  
        elif choice == 3:
            remove_favorite(user, userCol, productCol) 
        elif choice == 4:
            print("Saindo dos favoritos.")
            break
        else:
            print("Opção inválida! Escolha um número entre 1 e 4.")
