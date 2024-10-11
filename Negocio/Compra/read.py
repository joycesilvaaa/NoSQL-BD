from helpers.utils import find_purchases

def read_purchase(nota_fiscal, purCol):
    print("-="*20)
    print("     Consultar Compra:")
    print("-="*20)
    purchase = find_purchases(nota_fiscal, purCol)

    if not purchase:
        return f"Compra com nota fiscal {nota_fiscal} não encontrada!"
    print("-="*20)
    print("     Detalhes da Compra:")
    print("-="*20)
    print(f"Nota Fiscal: {purchase['nota_fiscal']}")
    print(f"Data da Compra: {purchase['data_compra']}")
    print(f"Usuário: {purchase['usuario']['nome']}")
    for index, product in enumerate(purchase["produtos"]):
        print(f"{index+1} - Produto: {product['nome']}, Marca: {product['marca']}, Quantidade: {product['quantidade']}")
    print(f"Endereço de Entrega: {purchase['endereco_entrega']['rua']}, {purchase['endereco_entrega']['num']}")
    print(f"Valor Total: R$ {purchase['valor_total']:.2f}")
    print(f"Status: {purchase['status']}")
    print("-="*20)
    
