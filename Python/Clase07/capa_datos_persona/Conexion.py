import sys

import psycopg2 as bd
from logger_base import log

class Conexion: 
    _DATABASE: str = "test_bd"
    _USERNAME: str = "postgres"
    _PASSWORD: str = "admin"
    _DB_PORT: str = "5432"
    _HOST: str = "127.0.0.1"
    _conexion = None
    _cursor = None

    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = bd.connect(host=cls._HOST, user= cls._USERNAME, password=cls._PASSWORD, port=cls._DB_PORT)
                log.debug(f'Conexion exitosa: {cls._conexion}')
                return cls._conexion
            except Exception as e:
                log.error(f'Ocurrió un error: {e}')
                sys.exit()
        else: 
            return cls._conexion
            
    @classmethod
    def obtenerCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                log.debug(f'Se abrio correctamente el cursor: {cls._cursor}')
                return cls._cursor
            except Exception as e:
                log.error(f'Ocurrió un error: {e}')
                sys.exit()
        else:
            return cls._cursor  
            
if __name__ == "__main__":
    Conexion.obtenerConexion()
    Conexion.obtenerCursor()

# ¿Para qué es esto y de qué sirve?
# Sirve para no tener que escribir los datos de conexión (usuario, clave, host) en cada parte de tu programa. Centraliza el acceso para:
# Seguridad: Si cambias la contraseña, solo la tocas en un lugar.
# Eficiencia: Usa el patrón Singleton (aunque sea de forma simplificada). Si la conexión ya existe, te devuelve la misma en lugar de crear una nueva, ahorrando recursos de memoria.
# Manejo de Errores: Si el servidor de la base de datos está caído, el programa te avisa por el log y se cierra ordenadamente en lugar de "romperse" sin explicaciones.

'''
EXPLICACIÓN DEL CÓDIGO - CLASE CONEXIÓN (CAPA DE DATOS)

1. CONSTANTES DE CONFIGURACIÓN:
   - _DATABASE, _USERNAME, etc.: Son los datos necesarios para entrar a Postgres.
   - _HOST "127.0.0.1" indica que la base de datos está en tu misma computadora (localhost).

2. ATRIBUTOS DE CLASE:
   - _conexion y _cursor: Se inicializan en None. Guardarán el objeto de conexión 
     una vez que se logre establecer el vínculo.

3. DECORADOR @classmethod:
   - Indica que estos métodos pertenecen a la clase y no a un objeto específico. 
     Podés llamarlos como 'Conexion.obtenerConexion()' sin crear una instancia.

4. MÉTODO obtenerConexion():
   - 'if cls._conexion is None': Verifica si ya estamos conectados. 
   - Si no hay conexión, intenta crear una con 'bd.connect(...)'.
   - 'sys.exit()': Si falla la conexión, detiene todo el programa porque 
     sin base de datos el sistema no puede funcionar.

5. MÉTODO obtenerCursor():
   - El 'cursor' es el objeto que realmente ejecuta las sentencias SQL (SELECT, INSERT).
   - Este método asegura que siempre tengas un cursor disponible llamando a obtenerConexion().

6. BLOQUE DE PRUEBA:
   - Simplemente intenta conectar y abrir el cursor para verificar que los datos 
     de acceso (user, password) sean correctos.
'''