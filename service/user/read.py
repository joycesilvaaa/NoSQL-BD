from utils.utils import get_user, row_to_dict_user
from uuid import UUID

def read_user(session, user_id):
    print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
    print(f"Visualizar usuário com ID: {user_id}")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
        
    user = get_user(session, UUID(user_id))

    if user is None:
        print("Usuário não encontrado!")
        return None
    
    user_data = row_to_dict_user(user)

    print(f"| Nome: {user_data['nome']}")
    print(f"| E-mail: {user_data['email']}")
    print(f"| CPF: {user_data['cpf']}")
    print(f"| Senha: {user_data['senha']}")
    
    if user_data['favoritos']:
        print("| Favoritos:")
        for favorito in user_data['favoritos']:
            print(f"- {favorito}")
    else:
        print("| Favoritos: Nenhum favorito registrado")

    if user_data['compras']:
        print("| Compras:")
        for compra in user_data['compras']:
            print(f"    ID da Compra: {compra['id']}")
            print(f"    Data da Compra: {compra['data_compra']}")
            print(f"    Valor Total: R$ {float(compra['valor_total']):.2f}")
            print(f"    Status: {compra['status']}")
    else:
        print("| Compras: Nenhuma compra registrada")

    if user_data['enderecos']:
        print("| Endereços:")
        for endereco in user_data['enderecos']:
            print(f"    Rua: {endereco['rua']}, Número: {endereco['numero']}, Tipo de Imóvel: {endereco['tipo_imovel']}, Complemento: {endereco['complemento']},"
                  f" Bairro: {endereco['bairro']}, Cidade: {endereco['cidade']}, Estado: {endereco['estado']}")
    else:
        print("| Endereços: Nenhum endereço registrado")
    
    print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")

    