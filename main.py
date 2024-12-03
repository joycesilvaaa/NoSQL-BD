from config.connection_neo4j import connection_neo4j
from menu.product import manager_product
from menu.purchase import manager_purchase
from menu.seller import manager_seller
from menu.user import manager_user

def main():
    # Conectar ao banco de dados Neo4j
    driver, session = connection_neo4j()

    if driver is None or session is None:
        print("Erro ao conectar ao banco de dados.")
        return
    
    while True:
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("        Mercado Livre - Neo4j")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("1. Gerenciar Usuario")
        print("2. Gerenciar Vendedor")
        print("3. Gerenciar Produto")
        print("4. Gerenciar Compras")
        print("0. Sair ")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

        try:
            choice = int(input("Digite a opção que deseja: "))
        except ValueError as e:
            print(f"[Error] : {e}")
            continue

        # Chama o método correspondente com base na escolha
        match choice:
            case 1:
                manager_user(session)  # Corrigido para passar session
            case 2:
                manager_seller(session)  # Corrigido para passar session
            case 3:
                manager_product(session)  # Corrigido para passar session
            case 4:
                manager_purchase(session)  # Corrigido para passar session
            case 0:
                session.close()  # Fechar a sessão
                driver.close()  # Fechar o driver
                print("Saindo...")
                break  # Sai do loop e encerra o programa
            case _:
                print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
