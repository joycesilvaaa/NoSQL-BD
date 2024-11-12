from config.connection_neo4j import connection_neo4j
from menu.product import manager_product
from menu.purchase import manager_purchase
from menu.seller import manager_seller
from menu.user import manager_user

def main():

    driver, session = connection_neo4j()

    if driver is None or session is None:
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
        except ValueError as e :
            print(f"[Error] : ${e}")
            continue
        match choice:
             case 1:
                manager_user()
                break
             case 2:
                manager_seller()
                break
             case 3:
                manager_product()
                break
             case 4:
                manager_purchase()
                break
             case 0:
                session.close()
                driver.close()
                print("Saindo...")
                break



if __name__ == "__main__":
    main()