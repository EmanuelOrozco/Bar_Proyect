import sqlite3
from models import Waiter


class WaiterManager:
    def __init__(self, db_name: str):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def add_waiter(self, waiter: Waiter):
        """Agrega un mesero con ID manual"""
        try:
            self.cursor.execute(
                "INSERT INTO Waiters (id_waiter, name, password) VALUES (?, ?, ?)",
                (waiter.waiter_id, waiter.name, waiter.password)
            )
            self.conn.commit()
            print(f"Waiter added")
        except sqlite3.IntegrityError as e:
            print(f"Error adding waiter")

    def close(self):
        """Cierra la conexión"""
        self.conn.close()

    def delete_waiter(self, waiter: Waiter):
        """Elimina un mesero de la base de datos por ID"""
        try:
            self.cursor.execute(
                "DELETE FROM Waiters WHERE id_waiter = ?", (waiter.waiter_id,)
            )
            self.conn.commit()
            print(f"waiter deleted.")
        except sqlite3.Error as e:
            print(f"Error deleting waiter")
