from uuid import uuid4, UUID
from utils.utils import get_seller, row_to_dict_seller

def create_product(session, seller_id):
    try:
        product_id = uuid4()
        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
        print("Informe os dados do novo produto:")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")

        seller = get_seller(session, UUID(seller_id))
        if seller is None:
            print("Vendedor não encontrado!")
            return
        
        nome_produto = input("Digite o nome do produto: ")
        marca_produto = input("Digite a marca do produto: ")
        valor = float(input("Digite o valor do produto: "))
        estoque = int(input("Digite o estoque disponível: "))

        seller_data = row_to_dict_seller(seller)
        
        produto = {
            "id": product_id,
            "nome_produto": nome_produto,
            "marca_produto": marca_produto,
            "valor": valor,
            "estoque": estoque,
            "vendas": 0,
            "vendedor_id": UUID(seller_id),  
            "nome_vendedor": seller_data["nome"],
            "email_vendedor": seller_data["email"],
            "cnpj_vendedor": seller_data["cnpj"]
        }

        produto_map = {
            "id": str(produto["id"]),
            "nome_produto": produto["nome_produto"],
            "marca_produto": produto["marca_produto"],
            "valor": str(produto["valor"]),
            "estoque": str(produto["estoque"]),
            "vendas": str(produto["vendas"]),
            "vendedor_id": str(produto["vendedor_id"]),
            "nome_vendedor": produto["nome_vendedor"],
            "email_vendedor": produto["email_vendedor"],
            "cnpj_vendedor": produto["cnpj_vendedor"]
        }

        produtos = seller_data['produtos']
        produtos.append(produto_map)

        query_insert_product = """
            INSERT INTO products (id, nome_produto, marca_produto, valor, estoque, vendas, vendedor_id, nome_vendedor, email_vendedor, cnpj_vendedor)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        session.execute(query_insert_product, (
            produto["id"],
            produto["nome_produto"],
            produto["marca_produto"],
            produto["valor"],
            produto["estoque"],
            produto["vendas"],
            produto["vendedor_id"],
            produto["nome_vendedor"],
            produto["email_vendedor"],
            produto["cnpj_vendedor"]
        ))

        query_update_seller = """
            UPDATE seller
            SET produtos = %s
            WHERE id = %s
        """
        session.execute(query_update_seller, (produtos, UUID(seller_id)))

        print(f"Produto adicionado à lista de produtos do vendedor {seller_data['nome']}.")
        print(f"Produto '{nome_produto}' criado com sucesso! ID: {product_id}")

        return 
        
    except Exception as e:
        print(f"Erro ao criar produto: {e}")
        return None
