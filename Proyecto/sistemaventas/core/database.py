import sqlite3

class Database:
    def __init__(self, db_name="ventas.db"):
        self.db_name = db_name
        self.conexion = None # Aquí guardaremos la conexión activa

    def get_connection(self):
        # Si no hay conexión o se cerró, creamos una
        if self.conexion is None:
            self.conexion = sqlite3.connect(self.db_name)
        return self.conexion
    
    def cerrarConexion(self):
        if self.conexion:
            self.conexion.close()
            self.conexion = None # Limpiamos la variable
            print("Conexión cerrada correctamente.")

# Uso:
db = Database()