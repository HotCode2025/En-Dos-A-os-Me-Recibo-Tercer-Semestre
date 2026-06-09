import sys
import psycopg2 as bd
from logger_base import log
from psycopg2 import pool #Se importa 'pool' de psycopg2 para manejar el grupo de conexiones

class Conexion: 
    # Atributos de configuración de la base de datos
    _DATABASE: str = "test_bd"
    _USERNAME: str = "postgres"
    _PASSWORD: str = "admin"
    _DB_PORT: str = "5432"
    _HOST: str = "127.0.0.1"
    # Parámetros del Pool: mínimo 1 conexión abierta, máximo 5 simultáneas
    _MIN_CON = 1
    _MAX_CON = 5
    _poll = None # Acá se guardará el objeto del Pool una vez creado

    @classmethod
    def obtenerConexion(cls):
        """
        Solicita una conexión que YA ESTÁ CREADA dentro del pool.
        No crea una conexión nueva desde cero, la "alquila" del pool.
        """
        # .getconn() toma una conexión libre del pool y la asigna a 'conexion'
        conexion = cls.obtenerPool().getconn()
        log.debug(f"Conexión obtenida del pool: {conexion}")
        return conexion

    @classmethod
    def obtenerPool(cls):
        """
        Método interno (Patrón Singleton) para asegurarse de que 
        el Pool se cree UNA SOLA VEZ.
        """
        # Si el pool no existe todavía, lo crea
        if cls._poll is None:
            try:
                # Inicializa el pool con los límites y credenciales configurados
                cls._poll = pool.SimpleConnectionPool(cls._MIN_CON,
                                                    cls._MAX_CON,
                                                    host=cls._HOST,
                                                    user=cls._USERNAME,
                                                    password=cls._PASSWORD,
                                                    port=cls._DB_PORT,
                                                    database=cls._DATABASE)
                log.debug(f"Creación del pool exitosa: {cls._poll}")
                return cls._poll
            except Exception as e:
                log.error(f"Error al obtener el pool: {e}")
                sys.exit() # Corta la ejecución si no se puede conectar
        else: # Si el pool ya existía, simplemente lo devuelve para no crear otro
            return cls._poll
        
    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion) # Devuelve la conexión al pool para que otro proceso la use
        log.debug(f"Regresamos la conexión al pool: {conexion}")
    
    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall() # Cierra todas las conexiones del pool, útil para apagar la aplicación ordenadamente
        log.debug("Todas las conexiones del pool han sido cerradas.")
            
if __name__ == "__main__":
    # Al pedir 5 conexiones seguidas, el pool va entregando una por una
    # (Conexion1, Conexion2, etc., son objetos de conexión distintos sacados de la pileta)
    Conexion1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(Conexion1) # Devolvemos la conexión al pool para que pueda ser reutilizada
    Conexion2 = Conexion.obtenerConexion()
    Conexion.liberarConexion(Conexion2)
    Conexion3 = Conexion.obtenerConexion()
    Conexion.liberarConexion(Conexion3)
    Conexion4 = Conexion.obtenerConexion()
    Conexion5 = Conexion.obtenerConexion()
    Conexion6 = Conexion.obtenerConexion()


# ¿Para qué es esto y de qué sirve?
# Sirve para no tener que escribir los datos de conexión (usuario, clave, host) en cada parte de tu programa. Centraliza el acceso para:
# Seguridad: Si cambias la contraseña, solo la tocas en un lugar.
# Eficiencia: Usa el patrón Singleton (aunque sea de forma simplificada). Si la conexión ya existe, te devuelve la misma en lugar de crear una nueva, ahorrando recursos de memoria.
# Manejo de Errores: Si el servidor de la base de datos está caído, el programa te avisa por el log y se cierra ordenadamente en lugar de "romperse" sin explicaciones.

'''
La Diferencia Clave (Explicación Rápida)
Código 1 (Con Pool de Conexiones): Creás una "pileta" o reserva de conexiones (SimpleConnectionPool) al principio. Cada vez que pedís una conexión, el pool te da una que ya está abierta y lista para usar. Cuando terminás, se devuelve al pool. Es el enfoque profesional y eficiente para aplicaciones reales, porque abrir y cerrar conexiones a la base de datos todo el tiempo es muy costoso en rendimiento.

Código 2 (Conexión Única o "Singleton"): Creás una sola conexión física en toda la vida del programa. Si volvés a llamar a obtenerConexion(), te devuelve exactamente la misma que ya habías abierto. Es un enfoque simple, pero peligroso si muchos usuarios o hilos intentan usar la base de datos al mismo tiempo.

¿Cuándo usar el 1? Siempre que hagas aplicaciones web o sistemas que atiendan a muchos usuarios en paralelo (como con Flask, FastAPI o Django).
¿Cuándo usar el 2? Para scripts locales, tareas automáticas chicas (cronjobs) o cuando estás aprendiendo las bases de las conexiones y el flujo de los cursores.
'''