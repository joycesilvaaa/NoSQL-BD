def list_favorite(user):
    favorites = user["favoritos"]
    
    if not favorites:
        print("Sua lista de favoritos está vazia.")
        return
    print("-="*20)
    print("     Seus produtos favoritos:")
    print("-="*20)
    
    for product in favorites:
        print("-="*20)
        print(f"Nome: {product.get('nome', 'N/A')}")
        print(f"Marca: {product.get('marca', 'N/A')}")
        print(f"Valor: R$ {int(product.get('valor', 'N/A')):.2f}")
        print("-="*20)
