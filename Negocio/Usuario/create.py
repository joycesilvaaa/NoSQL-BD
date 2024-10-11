def create_user(userCol):
    print("\nInserindo um novo usuário")
    nome = input("Nome: ")
    email = input("E-mail: ")
    cpf = input("CPF: ")
    senha = input("Senha: ")
    key = 1
    end = []
    favoritos =[]
    compras = []
    while (key != 'n' and key != "nao"):
        rua = input("Rua: ")
        num = input("Num: ")
        tipo_imovel = input("Tipo do Imovél: ")
        complemento = input("Complemento: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        estado = input("Estado: ")
        endereco = {        
            "rua":rua,
            "num": num,
            "tipo_imovel": tipo_imovel,
            "complemento": complemento,
            "bairro": bairro,
            "cidade": cidade,
            "estado": estado,
        }
        end.append(endereco) 
        key = input("Deseja cadastrar um novo endereço (S/N)? ").lower()
    mydoc = { "nome": nome, "email": email, "cpf": cpf, "end": end, "senha": senha, "favoritos": favoritos, "compras": compras }
    x = userCol.insert_one(mydoc)
    print("-="*20)
    print("Documento inserido com ID ",x.inserted_id)
