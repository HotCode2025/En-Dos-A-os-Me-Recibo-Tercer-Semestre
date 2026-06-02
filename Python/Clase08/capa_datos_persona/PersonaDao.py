from Persona import Persona
from Conexion import Conexion
from logger_base import log

class PersonaDAO:
    """
    DAO (Data Access Object) para la entidad Persona.
    Proporciona métodos para interactuar con la base de datos.
    CRUD: Create (Insertar), Read (Leer), Update (Actualizar), Delete (Eliminar)
    """
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'


# Definimos los métodos de clase
    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                personas = []
                for i in registros:
                    persona = Persona(i[0], i[1], i[2], i[3])
                    personas.append(persona)
                return personas
            
    @classmethod
    def insertar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'Persona Insertada: {persona}')
                return cursor.rowcount
            
    @classmethod
    def actualizar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
                cursor.execute(cls._ACTUALIZAR, valores)
                log.debug(f'Persona Actualizada: {persona}')
                return cursor.rowcount
            
    @classmethod
    def eliminar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.id_persona,)
                cursor.execute(cls._ELIMINAR, valores)
                log.debug(f'Persona Eliminada: {persona}')
                return cursor.rowcount
            

if __name__ == '__main__':
    # Prueba de selección
    personas = PersonaDAO.seleccionar()
    for i in personas:
        log.debug(i)

    # Prueba de inserción
    # persona1 = Persona(nombre="Pato", apellido="Gervasi", email="patogervasi@gmail.com")
    # personas_insertadas = PersonaDAO.insertar(persona1)
    # log.debug(f'Personas Insertadas: {personas_insertadas}')

    # Prueba de actualización
    # persona1 = Persona(24, "Santiago", "LLorente", "santiagollorente@gmail.com")
    # personas_actualizadas = PersonaDAO.actualizar(persona1)
    # log.debug(f'Personas Actualizadas: {personas_actualizadas}')

    # Prueba de eliminación
    # persona1 = Persona(id_persona=24)
    # personas_eliminadas = PersonaDAO.eliminar(persona1)
    # log.debug(f'Personas Eliminadas: {personas_eliminadas}')




# ¿Para qué es esto y de qué sirve?
# Sirve para separar la lógica de tu aplicación de la base de datos.
# Encapsulamiento de SQL: En lugar de tener sentencias SQL desparramadas por todo tu programa, las tenés centralizadas en una clase.
# Mantenimiento: Si mañana cambiás el nombre de una tabla o columna en pgAdmin, solo modificás una línea acá y el resto de tu programa sigue funcionando igual.
# Seguridad: El uso de %s (placeholders) garantiza que el sistema sea inmune a la Inyección SQL, como vimos antes.

'''EXPLICACIÓN DEL CÓDIGO - CLASE PERSONA DAO (CAPA DE DATOS)

1. EL PATRÓN DAO:
   - 'Data Access Object': Es una clase encargada exclusivamente de las 
     operaciones CRUD en la base de datos para una entidad (en este caso, Persona).

2. LAS CONSTANTES SQL (Sentencias):
   - Estas variables almacenan los comandos que se enviarán a PostgreSQL.
   - Usamos guion bajo (_SELECCIONAR) para indicar que son constantes privadas.

3. EXPLICACIÓN DE LAS SENTENCIAS:
   - _SELECCIONAR: Trae todos los registros ordenados por su ID.
   - _INSERTAR: Agrega una persona. Nota que no pasamos el 'id_persona' porque 
     Postgres lo suele generar automáticamente (SERIAL).
   - _ACTUALIZAR: Modifica los datos de una persona específica usando su ID 
     como filtro en el WHERE.
   - _ELIMINAR: Borra un registro permanentemente basándose en el ID.

4. LOS PLACEHOLDERS (%s):
   - Muy importante: NO usamos f-strings ni concatenación.
   - El '%s' es el parámetro posicional. La librería psycopg2 se encarga de 
     reemplazarlos por los datos reales de forma segura.
'''