from helpers.utils import find_purchases 

def delete_purchase(user, userCol, nota_fiscal, purCol):
    print("-="*20)
    print("     Deletar Compra")
    print("-="*20)

    purchase = find_purchases(nota_fiscal, purCol)

    if not purchase:
        return print(f"Compra com nota fiscal {nota_fiscal} não encontrada!")


    if purchase["status"] in ["Enviado", "Entregue"]:
        return print(f"Não é possível deletar uma compra com status '{purchase['status']}'!")

    purCol.delete_one({"nota_fiscal": nota_fiscal})

    userCol.update_one(
        {"_id": user["_id"]},
        {"$pull": {"compras": {"nota_fiscal":purchase["nota_fiscal"]}}}
    )
    
    print(f"Compra com nota fiscal {nota_fiscal} deletada com sucesso!")

