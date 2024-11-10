from uuid import UUID
from utils.utils import get_purchase, get_user

def delete_purchase(session, purchase_id):
    try:
        # Obtém a compra pelo ID
        purchase = get_purchase(session, UUID(purchase_id))
        if purchase is None:
            print("Compra não encontrada")
            return

        # Obtém o usuário associado à compra
        user = get_user(session, purchase.user_id)
        if user is None:
            print("Comprador não encontrado")
            return

        # Converte user.compras para uma lista e remove a compra específica
        user_compras = list(user.compras) if user.compras else []
        user_compras = [compra for compra in user_compras if compra["id"] != str(purchase_id)]

        # Atualiza o usuário com a lista modificada de compras
        update_query = """
            UPDATE user
            SET compras = %s
            WHERE id = %s
        """
        session.execute(update_query, (user_compras, user.id))  # Passando user.id diretamente

        # Deleta a compra da tabela `purchase`
        delete_query = """
            DELETE FROM purchase WHERE id = %s
        """
        session.execute(delete_query, (UUID(purchase_id),))

        print(f"Compra com ID {purchase_id} deletada com sucesso!")
        return

    except Exception as e:
        print(f"Erro ao deletar a compra: {e}")

