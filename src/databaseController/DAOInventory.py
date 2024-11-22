import sqlite3
from models import Inventory 


class InventoryManager:
    def __init__(self, db_name: str):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def add_inventory(self, inventory : Inventory):
        """Agrega un producto al inventario con ID manual"""
        self.cursor.execute("SELECT * FROM Inventory WHERE product_id = ?", (inventory.product_id,))
        result = self.cursor.fetchone()

        if result:
            # Si el producto ya está en inventario, lo actualiza
            self.cursor.execute(
                "UPDATE Inventory SET quantity = quantity + ? WHERE product_id = ?",
                (inventory.quantity, inventory.product_id)
            )
        else:
            # Si el producto no está en inventario, lo agrega
            self.cursor.execute(
                "INSERT INTO Inventory (product_id, quantity) VALUES (?, ?)",
                (Inventory.product_id, inventory.quantity)
            )
        self.conn.commit()
        print(f"Inventory updated ")

    def close(self):
        """Cierra la conexión"""
        self.conn.close()
        
    def delete_inventory(self,inventory : Inventory):
        """Elimina un producto del inventario por ID"""
        try:
            self.cursor.execute(
                "DELETE FROM Inventory WHERE product_id = ?", (inventory.product_id,)
            )
            self.conn.commit()
            print(f"Product  removed from inventory")
        except sqlite3.Error as e:
            print(f"“Error deleting product from inventory")
