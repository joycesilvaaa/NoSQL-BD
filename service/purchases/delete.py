from uuid import UUID
from utils.utils import get_purchase

def delete_purchase(session, purchase_id):
    try:
        purchase = get_purchase(session, UUID(purchase_id))
        if purchase is None:
            print("Compra não encontrada")
            return
        
        query = """
            DELETE FROM purchase WHERE id = %s
        """
        session.execute(query, (UUID(purchase_id),))

        print(f"Compra com ID {purchase_id} deletada com sucesso!")
        return

    except Exception as e:
        print(f"Erro ao deletar a compra: {e}")
