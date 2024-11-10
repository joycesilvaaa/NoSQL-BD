from uuid import uuid4, UUID
from datetime import datetime
from utils.utils import list_products, get_product, update_sale_and_stock, get_user, row_to_dict_user

def create_purchase(session, user_id):
    try:
        # Gera ID para a nova compra
        purchase_id = uuid4() 
        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
        print("Informe os dados da nova compra:")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
        
        # Obtém dados do usuário
        user = get_user(session, UUID(user_id))
        if user is None:
            print("Usuário não encontrado!")
            return
        user_data = row_to_dict_user(user)
        
        # Lista produtos disponíveis
        products = list_products(session)
        if not products:
            print("Sem produtos cadastrados no sistema.")
            return
        
        # Coleta produtos da compra
        produtos = []
        while True:
            print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
            product_id = input("Digite o ID do produto que deseja comprar: ")
            quantity = int(input("Digite a quantidade do produto: "))
            
            product = get_product(session, UUID(product_id))  
            if product is None:
                print("Produto não encontrado!")
                continue  

            if quantity > product.estoque:
                print(f"Quantidade disponível para venda: {product.estoque}")
                continue
            
            # Formata o produto como `map<text, text>`
            produtos.append({
                "produto_id": str(product_id),
                "nome_produto": str(product.nome_produto),
                "quantidade": str(quantity),
                "preco_unitario": str(product.valor)
            })

            continuar = input("Deseja adicionar outro produto? (s/n): ")
            if continuar.lower() != 's':
                break
        
        # Seleciona endereço de entrega
        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
        print("Selecione um endereço de entrega:")
        
        enderecos = user_data.get("enderecos", [])
        if not enderecos:
            print("Você não tem endereços cadastrados!")
            return
        
        for idx, end in enumerate(enderecos, start=1):
            print(f"{idx} - {end['rua']}, {end['bairro']}, {end['cidade']}")

        try:
            index_to_select = int(input("Digite o número do endereço a ser selecionado (ou 0 para cancelar): "))
            if 0 < index_to_select <= len(enderecos):
                endereco_entrega = dict(enderecos[index_to_select - 1])
            else:
                print("Seleção inválida ou operação cancelada.")
                return
        except ValueError:
            print("Por favor, insira um número válido.")
            return
        
        # Calcula o valor total da compra
        valor_total = sum(float(produto["preco_unitario"]) * int(produto["quantidade"]) for produto in produtos)
        
        # Gera informações para a compra
        data_compra = datetime.now()
        
        # Insere compra na tabela `purchase`
        query = """
            INSERT INTO purchase (id, user_id, data_compra, valor_total, produtos, endereco_entrega, status)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        # Converte `endereco_entrega` em `map<text, text>`
        endereco_formatado = {
            "rua": endereco_entrega.get("rua"),
            "bairro": endereco_entrega.get("bairro"),
            "cidade": endereco_entrega.get("cidade"),
            "estado": endereco_entrega.get("estado"),
            "numero": endereco_entrega.get("numero"),
            "complemento": endereco_entrega.get("complemento")
        }

        session.execute(query, (purchase_id, UUID(user_id), data_compra, valor_total, produtos, endereco_formatado, "Processando"))
        
        print(f"Compra realizada com sucesso! ID: {purchase_id}")

        # Simplifica dados da compra para o campo `compras`
        compra_simplificada = {
            "id": str(purchase_id),
            "data_compra": data_compra.isoformat(),
            "valor_total": str(valor_total),
            "status": "Processando"
        }

        # Atualiza a lista de compras do usuário na tabela `user`
        compras = user_data['compras'] if user_data.get('compras') else []
        compras.append(compra_simplificada)

        query_update_user = """
            UPDATE user
            SET compras = %s
            WHERE id = %s
        """
        session.execute(query_update_user, (compras, UUID(user_id)))

        # Atualiza o estoque para cada produto na compra
        for produto in produtos:
            update_sale_and_stock(session, UUID(produto["produto_id"]), int(produto["quantidade"]))
        
    except Exception as e:
        print(f"Erro ao criar compra: {e}")
