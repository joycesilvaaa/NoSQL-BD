def create_seller(sellerCol):
    print("-="*20)
    print(" Inserindo um novo vendedor")
    print("-="*20)
    nome = input("Nome: ")
    email = input("E-mail: ")
    cnpj = input("Cnpj: ")
    avaliacao = int(input("Avaliação: "))
    key = 1
    end = []
    produtos =[]
    while (key != 'n'):
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
    mydoc = { "nome": nome, "email": email, "cnpj": cnpj,"avaliacao":avaliacao, "end": end, "produtos": produtos}
    x = sellerCol.insert_one(mydoc)
    print("-="*20)
    print("Documento inserido com ID ",x.inserted_id)