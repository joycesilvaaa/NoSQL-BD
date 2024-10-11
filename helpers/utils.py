import uuid
from bson.objectid import ObjectId

def find_seller(cnpj,collection):
    #busca vendedor
    myquery = {"cnpj": cnpj }
    mydoc = collection.find_one(myquery)
    return mydoc

def find_product(productId, productCol):
    # Busca o produto
    myquery = {"_id": ObjectId(productId)}
    product = productCol.find_one(myquery)
    return product  

def find_user(cpf, collection):
    #busca cliente
    myquery = {"cpf": cpf }
    mydoc = collection.find_one(myquery)
    return mydoc

def find_purchases(notaFiscal, collection):
    #busca compra
    myquery = {"nota_fiscal": notaFiscal}
    mydoc = collection.find_one(myquery)
    return mydoc
    
def find_address(rua, numero, bairro, user):
    enderecos = user.get("end", [])
    for i, address in enumerate(enderecos):
        if (address.get("rua") == rua and
            address.get("num") == numero and
            address.get("bairro") == bairro):
            return i, address  
    return None, None

def register_address(documento, collection, tipo):
    if tipo == "VEND":
        user = find_seller(documento, collection)
    if tipo == "USER":
        user = find_user(documento,collection)
    if user:
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
        return endereco

def list_addresses(user):
    addresses = user.get("end", [])
    if not addresses:
        print("-="*20)
        print("Não existem endereços cadastrados!")
        print("-="*20)
        return None
    return addresses

def generate_nota_fical():
    return str(uuid.uuid4())

def calculate_final_value(product, quantity):
    value_product = float(product.get("valor"))
    final_value = value_product * quantity
    return round(final_value, 2)







    
