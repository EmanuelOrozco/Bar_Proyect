import sqlite3
from models import Admin


class DAOAdmin:
    def __init__(self, db_name: str):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def add_admin(self, admin : Admin):
        """Agrega un administrador con ID manual"""
        try:
            self.cursor.execute(
                "INSERT INTO Admins (id_admin, name, password) VALUES (?, ?, ?)",
                (admin.admin_id, admin.name, admin.password)
            )
            self.conn.commit()
            print(f"Admin added.")
        except sqlite3.IntegrityError as e:
            print(f"Error adding admin")

    def close(self):
        """Cierra la conexión"""
        self.conn.close()

    def delete_admin(self, admin : Admin):
        """Elimina un administrador de la base de datos por ID"""
        try:
            self.cursor.execute(
                "DELETE FROM Admins WHERE id_admin = ?", (admin.admin_id,)
            )
            self.conn.commit()
            print(f"Admin deleted.")
        except sqlite3.Error as e:
            print(f"Error deleting admin")
