from uuid import uuid4, UUID
from datetime import datetime
from utils.utils import list_products, get_product, update_sale_and_stock, convert_ordered_map_to_dict, get_user, row_to_dict_user

def create_purchase(session, user_id):
    try:
        purchase_id = uuid4() 
        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
        print("Informe os dados da nova compra:")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
        
        user = get_user(session, UUID(user_id))
        if user is None:
            print("Usuário não encontrado!")
            return
        user_data = row_to_dict_user(user)
        
        products = list_products(session)
        if products is None:
            print("Sem produtos cadastrados no sistema.")
            return
        
        produtos = []
        while True:
            print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
            product_id = input("Digite o ID do produto que deseja comprar: ")
            quantity = int(input("Digite a quantidade do produto: "))
            
            product = get_product(session, UUID(product_id))  
            if product is None:
                print("Produto não encontrado!")
                continue  

            product_dict = convert_ordered_map_to_dict(product)

            produtos.append({
                "produto_id": product_dict['id'],
                "nome_produto": product_dict["nome_produto"],
                "quantidade": quantity,
                "preco_unitario": product_dict["valor"]
            })

            continuar = input("Deseja adicionar outro produto? (s/n): ")
            if continuar.lower() != 's':
                break
        
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
                endereco_entrega = enderecos[index_to_select - 1] 
            else:
                print("Seleção inválida ou operação cancelada.")
                return
        except ValueError:
            print("Por favor, insira um número válido.")
            return
        
        valor_total = 0
        for produto in produtos:
            valor_total += produto["preco_unitario"] * produto["quantidade"]
        
        data_compra = datetime.now()
        nota_fiscal = str(uuid4())
        compras = user_data['compras']
        compra = {
            "id": purchase_id,
            "data_compra": data_compra,
            "valor_total": valor_total,
            "produtos": produtos,
            "endereco_entrega": endereco_entrega,
            "status": "Processando",
            "nota_fiscal": nota_fiscal
        }
        compras.append(compra)

        query = """
            INSERT INTO purchase (id, user_id, data_compra, valor_total, produtos, endereco_entrega, status, nota_fiscal)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        session.execute(query, (purchase_id, user_data["id"], data_compra, valor_total, produtos, endereco_entrega, "Processando", nota_fiscal))
        
        print(f"Compra realizada com sucesso! ID: {purchase_id}")

        query_update_user = """
            UPDATE user
            SET compras = %s
            WHERE id = %s
        """
        session.execute(query_update_user, (compras, UUID(user_id)))

        for produto in produtos:
            update_sale_and_stock(session, UUID(produto["produto_id"]), produto["quantidade"])
        
        return
    except Exception as e:
        print(f"Erro ao criar compra: {e}")
        return None
