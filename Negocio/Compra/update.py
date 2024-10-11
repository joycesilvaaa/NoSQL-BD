from helpers.utils import find_purchases

def update_purchase(user, userCol, nota_fiscal, purCol):
    print("-="*20)
    print("     Atualizar Compra")
    print("-="*20)
    purchase = find_purchases(nota_fiscal, purCol)
    if not purchase:
        print("-="*20)
        return print("Compra não encotrada.")
        print("-="*20)
    new_status = input("Digite o novo status: ")

    purCol.update_one({"notaFiscal": nota_fiscal},{"$set": {"status": new_status}})

    for user_purchase in user["compras"]:
        if user_purchase["notaFiscal"] == nota_fiscal:
            user_purchase["status"] = new_status
            break

    userCol.update_one({"_id": user["_id"], "compras.notaFiscal": nota_fiscal},{"$set": {"compras.$.status": new_status}})
    print("-="*20)
    return print("      Status de entrega atualizado!")
    print("-="*20)
