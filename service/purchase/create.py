from utils.utils import create_purchase

def create_purchase_form(session):
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("         Cadastro de Compra")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

    try:
        query_users = "MATCH (u:User) RETURN u.cpf AS cpf, u.nome AS nome"
        result_users = session.run(query_users)
        users = result_users.data()

        if not users:
            print("Nenhum usuário encontrado!")
            return
        
        print("\nUsuários Disponíveis:")
        for user in users:
            print(f"Cpf: {user['cpf']}, Nome: {user['nome']}")

        user_cpf = input("\nDigite o CPF do usuário para realizar a compra: ").strip()

        query_products = """
            MATCH (v:Seller)-[:VENDE]->(p:Product)
            RETURN p.nome AS nome_produto, p.preco AS preco, p.marca AS marca
        """
        result_products = session.run(query_products)
        products = result_products.data()

        if not products:
            print("Nenhum produto disponível para compra!")
            return

        print("\nProdutos Disponíveis para Compra:")
        for product in products:
            print(f"Nome: {product['nome_produto']}, Preço: R${product['preco']}, Marca: {product['marca']}")

        total_value = 0
        purchase_products = []

        while True:
            product_name = input("\nDigite o nome do produto que deseja comprar: ").strip()

            product = next((p for p in products if p['nome_produto'] == product_name), None)
            if not product:
                print("Produto não encontrado! Tente novamente.")
                return
            quantity = int(input(f"Digite a quantidade de {product_name}: ").strip())

            product_value = product['preco'] * quantity
            total_value += product_value

            purchase_products.append(product['nome_produto'])

            add_more = input("Deseja adicionar outro produto? (s/n): ").strip().lower()
            if add_more != 's':
                break
        if purchase_products:
            status = "Esperando pagamento" 
            purchase_id = create_purchase(session, user_cpf, purchase_products, total_value, status)
            if purchase_id:
                print(f"Compra criada com sucesso! ID da compra: {purchase_id}")
            else:
                print("Falha ao criar a compra.")
        else:
            print("Compra não realizada. Nenhum produto foi selecionado.")

    except Exception as e:
        print(f"Erro ao criar a compra: {e}")
