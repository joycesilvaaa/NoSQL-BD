from utils.utils import create_seller  

def create_seller_form(session):
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("         Cadastro de Vendedor")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

    nome = input("Digite o nome do vendedor: ").strip()
    email = input("Digite o email do vendedor: ").strip()
    cnpj = input("Digite o cnpj do vendedor: ").strip()
    telefone = input("Digite o telefone do vendedor: ").strip()

    try:
        seller_id = create_seller(session, nome, email, cnpj, telefone)
        print(f"Vendedor criado com sucesso! ID: {seller_id}")
    except Exception as e:
        print(f"Erro ao criar o vendedor: {e}") 
