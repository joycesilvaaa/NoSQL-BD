from uuid import UUID
from utils.utils import get_seller, row_to_dict_seller

def read_seller(session, seller_id):
    print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
    print(f"Visualizar vendedor com ID: {seller_id}")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
        
    seller = get_seller(session, UUID(seller_id))

    if seller is None:
        print("Vendedor não encontrado!")
        return None
    
    seller_data = row_to_dict_seller(seller) 

    print(f"| Nome: {seller_data['nome']}")
    print(f"| E-mail: {seller_data['email']}")
    print(f"| CNPJ: {seller_data['cnpj']}")
    
    if seller_data['produtos']:
        print("| Produtos:")
        for produto in seller_data['produtos']:
            print(f"- {produto}")
    else:
        print("| Produtos: Nenhum produto registrado")

    if seller_data['enderecos']:
        print("| Endereços:")
        for endereco in seller_data['enderecos']:
            print(f"    - Rua: {endereco['rua']}, Número: {endereco['numero']}, Tipo de Imóvel: {endereco['tipo_imovel']}, Complemento: {endereco['complemento']}," 
                  f"Bairro: {endereco['bairro']}, Cidade: {endereco['cidade']}, Estado: {endereco['estado']}")
    else:
        print("| Endereços: Nenhum endereço registrado")

    print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
