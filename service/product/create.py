from utils.utils import create_product
def create_product_form(session):
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("         Cadastro de Produto")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    try:
        query = "MATCH (s:Seller) RETURN s.cnpj AS cnpj, s.nome AS nome"
        result = session.run(query)

        sellers = result.data()

        if not sellers:
            print("Nenhum vendedor encontrado!")
            return

        print("\nVendedores Disponíveis:")
        for seller in sellers:
            print(f"CNPJ: {seller['cnpj']}, Nome: {seller['nome']}")

        seller_cnpj = input("Digite o CNPJ do vendedor para buscar as informações: ").strip()

        nome_produto = input("Digite o nome do produto: ").strip()
        marca_produto = input("Digite a marca do produto: ").strip()
        valor = float(input("Digite o valor do produto: ").strip())

        product_id = create_product(session,seller_cnpj, nome_produto,valor, marca_produto)
        
        print(f"Produto criado e vinculado ao vendedor com sucesso! ID do Produto: {product_id}")
    except Exception as e:
        print(f"Erro ao criar o produto ou vincular ao vendedor: {e}")
