import sqlite3 

class ConexionDB:
    def __init__(self, db_name="hydrobyte.sqlite"):
        """Inicializa la conexión a la base de datos."""
        self.db_name = db_name

    def conectar(self):
        """Establece la conexión y devuelve el objeto conexión."""
        try:
            conn = sqlite3.connect(self.db_name)
            return conn
        except sqlite3.Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None

    def cerrar(self, conn):
        """Cierra la conexión a la base de datos."""
        if conn:
            conn.close()
