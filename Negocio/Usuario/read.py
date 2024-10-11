from helpers.utils import find_user
def read_user(cpf, userCol):
    user = find_user(cpf, userCol)
    if user:
        print("-="*20)
        print(f"ID: {user.get('_id')}")
        print(f"Nome: {user.get('nome')}")
        print(f"Email: {user.get('email')}")
        print(f"CPF: {user.get('cpf')}")
        print(f"Senha: {user.get('senha')}")
        print("-="*20)
        print("Endereço(s):")
        print("-="*20)
        for endereco in user.get('end', []):

            print(f"  Rua: {endereco.get('rua')}")
            print(f"  Número: {endereco.get('num')}")
            print(f"  Tipo de Imóvel: {endereco.get('tipo_imovel')}")
            print(f"  Complemento: {endereco.get('complemento')}")
            print(f"  Bairro: {endereco.get('bairro')}")
            print(f"  Cidade: {endereco.get('cidade')}")
            print(f"  Estado: {endereco.get('estado')}")
        print("-="*20)
        
        if len(user.get("favoritos", [])) >= 1:
            print("-="*20)
            print("     Favoritos: ")
            print("-="*20)
            for index, product in enumerate(user["favoritos"]):
                nome_produto = product.get('nome', 'N/A')
                marca_produto = product.get('marca', 'N/A')
                valor_produto = product.get('valor', 'N/A')
                print(f"    {index + 1} - Produto: {nome_produto}, Marca: {marca_produto}, Valor: R$ {valor_produto}")
                print("-="*20)
        else:
            print(f"Sua lista de favoritos está vazia.")
        if len(user.get("compras", [])) >= 1:
            print("-="*20)
            print("Compras: ")
            print("-="*20)
            for index, compra in enumerate(user["compras"]):
                print(f"    {index + 1} - Nota Fiscal: {compra.get('notaFiscal')}, Status: {compra.get('status')}, Valor Total: R$ {compra.get('valorTotal', 0.0):.2f}")
                for produto in compra.get("produtos", []):
                    print(f"        Produto: {produto.get('nome')}, Marca: {produto.get('marca')}, Quantidade: {produto.get('quantidade')}")
                print("-="*20)
        else:
            print("-="*20)
            print("Nenhuma compra registrada.")
    else:
        print("Usuario não encontrado!")

def read_users(userCol):
    users = userCol.find().sort("nome")
    users_list = [{"nome": user.get("nome"), "cpf": user.get("cpf")} for user in users]
    print("Lista de usuários:")
    for user in users_list:
        print(f"Nome: {user['nome']}, CPF: {user['cpf']}")
