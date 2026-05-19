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

    
# ¿Para qué es esto y de qué sirve?
# Sirve para separar la lógica de tu aplicación de la base de datos.
# Encapsulamiento de SQL: En lugar de tener sentencias SQL desparramadas por todo tu programa, las tenés centralizadas en una clase.
# Mantenimiento: Si mañana cambiás el nombre de una tabla o columna en pgAdmin, solo modificás una línea acá y el resto de tu programa sigue funcionando igual.
# Seguridad: El uso de %s (placeholders) garantiza que el sistema sea inmune a la Inyección SQL, como vimos antes.

'''
EXPLICACIÓN DEL CÓDIGO - CLASE PERSONA DAO (CAPA DE DATOS)

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