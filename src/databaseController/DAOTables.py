import sqlite3
from models import Table  


class DAOTable:
    def __init__(self, db_name: str):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def add_table(self, table: Table):
        """Agrega una mesa con ID manual"""
        try:
            self.cursor.execute(
                "INSERT INTO Tables (id_table, total_table) VALUES (?, ?)",
                (table.table_id, table.total_table)
            )
            self.conn.commit()
            print(f"Table added")
        except sqlite3.IntegrityError as e:
            print(f"Error adding table")

    def close(self):
        """Cierra la conexión"""
        self.conn.close()
        
    def delete_table(self, table: Table):
        """Elimina una mesa de la base de datos por ID"""
        try:
            self.cursor.execute(
                "DELETE FROM Tables WHERE id_table = ?", (table.table_id,)
            )
            self.conn.commit()
            print(f"Table deleted")
        except sqlite3.Error as e:
            print(f"Error deleting table")
