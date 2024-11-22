import sqlite3
from models import Product  


class ProductManager:
    def __init__(self, db_name: str):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def add_product(self, product: Product):
        """Agrega un producto a la base de datos usando un objeto Product"""
        try:
            self.cursor.execute(
                "INSERT INTO Products (id, name, price) VALUES (?, ?, ?)",
                (product.product_id, product.name, product.price)
            )
            self.conn.commit()
            print(f"Producto '{product.name}' agregado con ID {product.product_id}.")
        except sqlite3.IntegrityError as e:
            print(f"Error adding product")

    def close(self):
        """Cierra la conexión"""
        self.conn.close()
    
    def delete_product(self, product: Product):
        """Elimina un producto de la base de datos por ID usando un objeto Product"""
        try:
            self.cursor.execute(
                "DELETE FROM Products WHERE id = ?", (product.product_id,)
            )
            self.conn.commit()
            print(f"Producto con ID {product.product_id} eliminado.")
        except sqlite3.Error as e:
            print(f"Error deleting product")
