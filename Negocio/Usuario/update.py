from helpers.utils import find_user, find_address, register_address,list_addresses

def update_user(cpf, userCol):
    user = find_user(cpf, userCol)
    if not user:
        print("Usuário não encontrado!")
        return
    novo_nome = input("Mudar Nome (ou Enter para manter): ")
    if novo_nome:
        user["nome"] = novo_nome

    email = input("Mudar E-mail (ou Enter para manter): ")
    if email:
        user["email"] = email
    print("-="*20)
    print(" Leia com atenção e escolha uma opção:")
    print("1 - Cadastrar novo endereço;")
    print("2 - Editar endereço existente;")
    print("3 - Remover endereço existente;")
    print("4 - Próximo (não modificar endereço)")
    print("-="*20)

    try:
        opcao = int(input("Digite a opção escolhida: "))
    except ValueError:
        print("Opção inválida!")
        return
    if opcao == 1:
        quantidade = int(input("Digite a quantidade de endereços que deseja cadastrar: "))
        c = 0
        while c < quantidade:
            novo_endereco = register_address(cpf, userCol, "USER")
            userCol.update_one({"cpf": cpf}, {"$push": {"end": novo_endereco}})
            c += 1
    elif opcao == 2:
        rua = input("Rua: ")
        numero = input("Número: ")
        bairro = input("Bairro: ")
        index, address = find_address(rua, numero, bairro, user)
        if address is not None:
            nova_rua = input("Nova Rua (ou Enter para manter): ")
            if nova_rua:
                address["rua"] = nova_rua
            novo_numero = input("Novo Número (ou Enter para manter): ")
            if novo_numero:
                address["num"] = novo_numero
            novo_tipo_imovel = input("Atualizar Tipo de imovél (ou Enter para manter): ")
            if novo_tipo_imovel:
                address["tipo_imovel"] = novo_tipo_imovel
            novo_complemento = input("Novo complemento (ou Enter para manter): ")
            if novo_complemento:
                address["complemento"] = novo_complemento
            novo_bairro = input("Novo Bairro (ou Enter para manter): ")
            if novo_bairro:
                address["bairro"] = novo_bairro
            nova_cidade = input("Novo Cidade (ou Enter para manter): ")
            if nova_cidade:
                address["cidade"] = nova_cidade
            novo_estado = input("Novo estado (ou Enter para manter): ")
            if novo_estado:
                address["estado"] = novo_estado
            userCol.update_one(
                {"cpf": cpf},
                {"$set": {f"end.{index}": address}}
            )
            print("-="*20)
            print("Endereço atualizado com sucesso.")
            print("-="*20)
        else:
            print("Endereço não encontrado.")
    elif opcao == 3:
        addresses = list_addresses(user)
        if not addresses:
            return print("Sem endereços cadastrados.")
        print("-="*20)
        print("     Endereços cadastrados:")
        print("-="*20)
        for address in addresses:
            print(f"Rua: {address.get('rua')}, Número: {address.get('num')}, Bairro: {address.get('bairro')}, Cidade: {address.get('cidade')}, Estado: {address.get('estado')}")
        print("-="*20)
        rua = input("Rua: ")
        numero = input("Número: ")
        bairro = input("Bairro: ")
        address = find_address(rua, numero, bairro,user)
        userCol.update_one({"cpf": user["cpf"]},{"$pull": {"end": {"rua": rua, "num": numero, "bairro": bairro}}})
        print("Endereço removido e banco de dados atualizado com sucesso.")
    else:
        print("-="*20)
        print("Nenhuma mudança feita no endereço.")
    userCol.update_one({"cpf": cpf}, {"$set": {"nome": user["nome"], "email": user["email"]}})
    print("-="*20)
    print("Dados atualizados com sucesso!")
