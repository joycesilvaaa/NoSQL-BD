from uuid import UUID
from utils.utils import get_product, convert_ordered_map_to_dict

def read_product(session, product_id):
    try:
        product = get_product(session, UUID(product_id))
        if not product:
            print("Produto não encontrado!")
            return


        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
        print(f"| ID: {product.id}")
        print(f"| Nome: {product.nome_produto}")
        print(f"| Marca: {product.marca_produto}")
        print(f"| Preço: R${product.valor:.2f}")
        print(f"| Estoque: {product.estoque}")
        print(f"| Vendas: {product.vendas}")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
        print(" Informações do Vendedor:")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
        print(f"| Nome do Vendedor: {product.nome_vendedor}")
        print(f"| Email do Vendedor: {product.email_vendedor}")
        print(f"| CNPJ do Vendedor: {product.cnpj_vendedor}")
        
    except Exception as e:
        print(f"Erro ao buscar o produto: {e}")
