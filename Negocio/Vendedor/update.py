from helpers.utils import  find_address, register_address, find_seller, list_addresses

def update_seller(cnpj, sellerCol):
    seller = find_seller(cnpj, sellerCol)
    
    if not seller:
        return "Vendedor não encontrado!"

    novo_nome = input("Mudar Nome (ou Enter para manter): ")
    if novo_nome:
        seller["nome"] = novo_nome

    email = input("Mudar E-mail (ou Enter para manter): ")
    if email:
        seller["email"] = email
    
   
    print("-="*20)
    print("Leia com atenção e escolha uma opção:")
    print("1 - Cadastrar novo endereço;")
    print("2 - Editar endereço existente;")
    print("3 - Remover endereço")
    print("4 - Próximo (não modificar endereço)")
    print("-="*20)
    opcao = int(input("Digite a opção escolhida: "))
    
    if opcao == 1:
        quantidade = int(input("Digite a quantidade de endereços que deseja cadastrar: "))
        c = 0
        while c < quantidade:
            novo_endereco = register_address(cnpj, sellerCol,"VEND") 
            sellerCol.update_one({"cnpj": cnpj}, {"$push": {"end": novo_endereco}})
            c += 1
    
    elif opcao == 2:
        print("-="*20)
        rua = input("Rua: ")
        numero = input("Número: ")
        bairro = input("Bairro: ")
        print("-="*20)
        index, address = find_address(rua, numero, bairro, seller)
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
            novo_estado = input("Novo nestdo (ou Enter para manter): ")
            if novo_estado:
                address["estado"] = novo_estado
            sellerCol.update_one(
                {"cnpj": cnpj},
                {"$set": {f"end.{index}": address}}
            )
            print("-="*20)
            print("Endereço atualizado com sucesso.")
            print("-="*20)
        else:
            print("Endereço não encontrado.")
    elif opcao == 3:
        list_address = list_addresses(seller)
        if not list_address:
            print("Sem endereços cadastrados.")
        print("-="*20)
        print("     Endereços cadastrados:")
        print("-="*20)
        for index, address in enumerate(list_address):
            print(f"Rua: {address.get('rua')}, Número: {address.get('num')}, Bairro: {address.get('bairro')}, Cidade: {address.get('cidade')}, Estado: {address.get('estado')}")

        print("-="*20)
        rua = input("Rua: ")
        numero = input("Número: ")
        bairro = input("Bairro: ")
        address = find_address(rua, numero, bairro,seller)
        sellerCol.update_one({"cnpj": seller["cnpj"]},{"$pull": {"end": {"rua": rua, "num": numero, "bairro": bairro}}})
        print("-="*20)
        print("Endereço removido.")
    else:
        print("-="*20)
        print("Nenhuma mudança feita no endereço.")
    sellerCol.update_one({"cnpj": cnpj}, {"$set": {"nome": seller["nome"], "email": seller["email"]}})
    print("-="*20)
    print("Dados atualizados com sucesso!")
