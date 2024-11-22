import sqlite3
from models import Order,Product,Inventory 


class OrderProductManager:
    def __init__(self, db_name: str):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def add_product_to_order(self, order: Order, product: Product, inventary:Inventory):
        """Agrega un producto a una orden en la tabla OrderProduct"""
        try:
            self.cursor.execute(
                "INSERT INTO OrderProduct (order_id, product_id, quantity) VALUES (?, ?, ?)",
                (order.order_id, product.product_id, inventary.inventory[product])
            )
            self.conn.commit()
            print(f"new order added")
        except sqlite3.IntegrityError as e:
            print(f"Error adding order")

    def close(self):
        """Cierra la conexión"""
        self.conn.close()
        
    def delete_product_from_order(self,  order: Order, product: Product):
        """Elimina un producto de una orden por los IDs de orden y producto"""
        try:
            self.cursor.execute(
                "DELETE FROM OrderProduct WHERE order_id = ? AND product_id = ?",
                (order.order_id, product.product_id)
            )
            self.conn.commit()
            print(f"product deleted.")
        except sqlite3.Error as e:
            print(f"Error deleting product")
