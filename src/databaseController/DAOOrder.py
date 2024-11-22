import sqlite3
from models import Order 


class OrderManager:
    def __init__(self, db_name: str):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def add_order(self, order: Order):
        """Agrega una orden con ID manual"""
        try:
            self.cursor.execute(
                "INSERT INTO Orders (id_order, waiter_id, table_id, total_order, value_tip) VALUES (?, ?, ?, ?, ?)",
                (order.order_id, order.waiter_id, order.table_id, order.total_order, order.value_tip)
            )
            self.conn.commit()
            print(f"Order Added.")
        except sqlite3.IntegrityError as e:
            print(f"Error adding order")

    def close(self):
        """Cierra la conexión"""
        self.conn.close()
        
    def delete_order(self, order: Order):
        """Elimina una orden de la base de datos por ID"""
        try:
            self.cursor.execute(
                "DELETE FROM Orders WHERE id_order = ?", (order.order_id,)
            )
            self.conn.commit()
            print(f"Order deleted.")
        except sqlite3.Error as e:
            print(f"Error deleting order")