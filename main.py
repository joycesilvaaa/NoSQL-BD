from Banco.config import connection
from Menu.Produto.produto import manager_product
from Menu.Compra.compra import manager_purchase
from Menu.Usuario.usuario import manager_user
from Menu.Vendedor.vendedor import manager_seller

def main():
    db = connection()  
    if db is None:
        print("Erro ao conectar ao banco de dados.")
        return
    mercado_livre_db = db['MercadoLivre']  
    productCol = mercado_livre_db['productCol']
    userCol = mercado_livre_db['userCol']
    sellerCol = mercado_livre_db['sellerCol']
    purchasesCol = mercado_livre_db['purchasesCol']

    print("Bem-vindo ao Banco de Dados Do Mercado Livre")
    
    while True:
        print("-="*20)
        print("         Menu Principal")
        print("-="*20)
        print("1 - Gerenciar Produtos")
        print("2 - Gerenciar Compras")
        print("3 - Gerenciar Usuários")
        print("4 - Gerenciar Vendedores")
        print("5 - Sair")
        print("-="*20)
        
        try:
            opcao = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Opção inválida! Escolha novamente.")
            continue
        
        if opcao == 1:
            manager_product(productCol,sellerCol)
        elif opcao == 2:
            manager_purchase(userCol, productCol, purchasesCol)
        elif opcao == 3:
            manager_user(userCol, productCol)
        elif opcao == 4:
            manager_seller(sellerCol)
        elif opcao == 5:
            print("Saindo...")
            break
        else:
            print("Opção inválida! Escolha novamente.")

if __name__ == "__main__":
    main()
