from config.connection_cassandra import connection_cassandra
from menu.product import manager_product
from menu.purchases import manager_purchases
from menu.user import manager_user
from menu.seller import manager_seller

def main():
    cluster = connection_cassandra()
    if cluster is None:
        print('Erro ao conectar ao Banco de Dados')
        return
    
    while True:
        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
        print(" Banco de dados do Mercado Livre")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
        print("1. Gerenciar Cliente")
        print("2. Gerenciar Compra")
        print("3. Gerenciar Vendedor")
        print("4. Gerenciar Produto")
        print("5. Sair")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")

        try:
            choice = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Opção inválida! Escolha novamente.")
            continue

        match choice:
            case 1:
                manager_user(cluster)
            case 2:
                manager_purchases(cluster)
            case 3:
                manager_seller(cluster)
            case 4:
                manager_product(cluster)
            case 5:
                print("Saindo...")
                break
            case _:
                print("Opção inválida! Escolha novamente.")

if __name__ == "__main__":
    main()
