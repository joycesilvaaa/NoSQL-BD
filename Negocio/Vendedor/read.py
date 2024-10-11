from helpers.utils import find_seller

def read_seller(cnpj, sellerCol):
    seller = find_seller(cnpj, sellerCol)
    if seller:
        print("-="*20)
        print("Informações do vendedor: ")
        print(f"Nome: {seller.get('nome')}")
        print(f"E-mail: {seller.get('email')}")
        print(f"CNPJ: {seller.get('cnpj')}")
        print(f"Avaliação: {seller.get('avaliacao')}")
        print("-="*20)
        print("     Endereços:")
        print("-="*20)
        for endereco in seller.get('end', []):
            print(f"  Rua: {endereco.get('rua')}")
            print(f"  Número: {endereco.get('num')}")
            print(f"  Tipo de Imóvel: {endereco.get('tipo_imovel')}")
            print(f"  Complemento: {endereco.get('complemento')}")
            print(f"  Bairro: {endereco.get('bairro')}")
            print(f"  Cidade: {endereco.get('cidade')}")
            print(f"  Estado: {endereco.get('estado')}")
            print("-="*20)
        if len(seller.get("produtos", [])) >= 1:
            print("-="*20)
            print("     Produtos:")
            print("-="*20)
            for index, product in enumerate(seller["produtos"]):
                nome_produto = product.get('nome', 'N/A')
                marca_produto = product.get('marca', 'N/A')
                valor_produto = product.get('valor', 'N/A')
                estoque_produto = product.get('estoque', 'N/A')
                vendas_produto = product.get('vendas', 'N/A')
                print(f"""   {index + 1} - Produto: {nome_produto}, Marca: {marca_produto}
                             Valor: R$ {valor_produto}, Estoque: {estoque_produto}, Vendas: {vendas_produto}""")
        else:
            print("Você não possui nenhum produto cadastrado.")
    else:
        return print("Vendedor não encontrado!")

def read_sellers(sellerCol):
    sellers = sellerCol.find().sort("nome")
    sellers_list = [{"nome": user.get("nome"), "cnpj": user.get("cnpj")} for user in sellers]
    print("-="*20)
    print("     Lista de Vendedores:")
    print("-="*20)
    if len(sellers_list) >= 1:
        for seller in sellers_list:
            print(f"Nome: {seller['nome']}, CNPJ: {seller['cnpj']}")
    else:
        return print("Sem Vendedores Cadastrados")
