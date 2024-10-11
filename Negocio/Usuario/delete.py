from helpers.utils import find_user
def delete_user(cpf, userCol):
    #Delete
    user = find_user(cpf, userCol)
    if user:
        userCol.delete_one({"_id":user["_id"]})
        return print("Usuario Deletado!")
    return print("Usuario não encontrado!")



