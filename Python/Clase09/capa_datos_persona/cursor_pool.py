from logger_base import log
from Conexion import Conexion

class CursorDelPool:
    def __init__(self):
        """
        Paso 1: El constructor. 
        Prepara las variables locales donde se van a guardar la conexión y el cursor.
        Todavía no hace nada en la base de datos, solo reserva el espacio.
        """
        self._conexion = None
        self._cursor = None

    def __enter__(self): # Método que se ejecuta al iniciar el bloque 'with'
        """
        Paso 2: Se ejecuta AUTOMÁTICAMENTE cuando ponés 'with CursorDelPool()'.
        Se encarga de toda la preparación pesada.
        """
        log.debug("Inicio del método with __enter__")
        self._conexion = Conexion.obtenerConexion() # Obtiene una conexión del pool
        self._cursor = self._conexion.cursor() # Crea un cursor a partir de esa conexión
        log.debug(f"Cursor creado: {self._cursor}")
        return self._cursor # Devuelve el cursor para que se use dentro del bloque 'with'
    
    def __exit__(self, tipo_excp, valor_excp, detalle_excp): # Método que se ejecuta al finalizar el bloque 'with'
        """
        Paso 4: Se ejecuta AUTOMÁTICAMENTE al salir del bloque 'with'.
        No importa si el código falló o terminó con éxito, este método se ejecuta SI o SÍ.
        Python le pasa 3 argumentos por si hubo errores (tipo, valor y el 'traceback').
        """
        log.debug("Se ejecuta el método __exit__")
        if valor_excp:
            self._conexion.rollback() # Si hubo una excepción, se hace rollback para no dejar la base de datos en un estado inconsistente
            log.error(f"Ocurrió una excepción: {valor_excp}")
        else: 
            self._conexion.commit() # Si no hubo excepciones, se confirma la transacción
            log.debug("Transacción confirmada (commit)")
        self._cursor.close() # Se cierra el cursor
        Conexion.liberarConexion(self._conexion) # Se libera la conexion del pool para que otro proceso la use
        log.debug("Cursor cerrado y conexión liberada al pool")

if __name__ == "__main__":
    with CursorDelPool() as cursor:
        log.debug("Dentro del bloque 'with'")
        cursor.execute("SELECT * FROM persona")
        log.debug(cursor.fetchall()) # Imprime todas las filas de la tabla persona usando el cursor obtenido del pool

'''
Este código es una de las mejores prácticas que vas a encontrar en Python para manejar bases de datos. Lo que hace es crear un Context Manager (Administrador de Contexto) personalizado.

Su único objetivo es automatizar completamente el abrir, cerrar y controlar errores (transacciones) cuando usás el pool de conexiones. Gracias a esto, te evitás escribir bloques try-except-finally gigantes cada vez que querés hacer una consulta SQL.

Acá tenés la explicación detallada y el código súper comentado para que te lo guardes:

El Concepto Clave: El bloque with y los métodos mágicos
Para entender este código, tenés que saber que en Python, cuando usás la palabra reservada with, estás llamando tras bambalinas a dos métodos "mágicos":

__enter__: Se ejecuta automáticamente al arrancar el with. Lo que devuelva este método se guarda en la variable que ponés después del as (en tu caso, as cursor).

__exit__: Se ejecuta automáticamente al salir del bloque with, ya sea porque el código terminó bien o porque saltó un error (excepción).
'''