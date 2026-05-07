import psycopg2 #Esto es para importar la libreria de psycopg2, que es un adaptador de base de datos para PostgreSQL en Python.
conexion = psycopg2.connect( #Objeto de conexión a la base de datos, que se crea utilizando la función connect de psycopg2.
    user = 'postgres',
    password = 'admin',
    host = '127.0.0.1',
    port = '5432',
    database = 'test_bd'
) #Esto es para establecer la conexión con la base de datos.

try: #Esto es para intentar ejecutar el bloque de código que se encuentra dentro del bloque try, y capturar cualquier excepción que pueda ocurrir durante la ejecución del programa.
    with conexion: #Esto es para utilizar el contexto de la conexión, lo que garantiza que la conexión se cerrara automáticamente al finalizar el bloque.
        with conexion.cursor() as cursor: #Esto es para crear un cursor utilizando el contexto de la conexión, lo que garantiza que el cursor se cerrará automáticamente al finalizar el bloque.
            sentencia = 'INSERT INTO persona (nombre, apellido, email) VALUES (%s, %s, %s)' #Esto es para definir la sentencia SQL que se va a ejecutar. #Placeholder para los valores de nombre, apellido y email, que se van a pasar como parámetros en la ejecución de la sentencia SQL.
            valores = (
                ('Carlos', 'Lara', 'clara@gmail.com'), #Esto es para definir el valor de los placeholders de la sentencia SQL.
                ('Ana', 'García', 'ana@gmail.com'),
                ('Luis', 'Pérez', 'luis@gmail.com')
            ) #Esto es para definir el valor de los placeholders de la sentencia SQL. Se ha cambiado a una tupla de tuplas para permitir la inserción de múltiples registros.
            cursor.executemany(sentencia, valores) #Esto es para ejecutar la sentencia SQL en la base de datos, pasando el valor del id_persona como parámetro. Se ha cambiado a executemany para permitir la inserción de múltiples registros.
            registros_insertados = cursor.rowcount #Esto es para obtener el número de registros que se han insertado en la base de datos.
            print(f'Registros insertados: {registros_insertados}') #Esto es para imprimir el número de registros que se han insertado en la base de datos.
except Exception as e: #Esto es para capturar cualquier excepción que pueda ocurrir durante la ejecución del programa.
    print(f'Ocurrió un error: {e}') #Esto es para imprimir un mensaje de error en caso de que ocurra una excepción.
finally: #Esto es para ejecutar el bloque de código que se encuentra dentro del bloque finally, sin importar si se produce una excepción o no.
    conexion.close() #Esto es para cerrar la conexión con la base de datos.

#Explicacion del código:
# import psycopg2 # Importamos el adaptador para conectar Python con PostgreSQL

# # --- BLOQUE 1: CONFIGURACIÓN DE ACCESO ---
# # Definimos las credenciales para abrir el canal de comunicación con el servidor.
# conexion = psycopg2.connect(
#     user = 'postgres',
#     password = 'admin',
#     host = '127.0.0.1',
#     port = '5432',
#     database = 'test_bd'
# )

# try:
#     # --- BLOQUE 2: GESTIÓN DE TRANSACCIÓN ---
#     # Al insertar varios registros, el 'with' es vital: si falla la inserción de 
#     # la tercera persona, se deshacen las anteriores para no dejar datos incompletos.
#     with conexion:

#         # --- BLOQUE 3: EL CURSOR (EL INTERMEDIARIO) ---
#         # Creamos el cursor para ejecutar las sentencias. El 'with' asegura su cierre.
#         with conexion.cursor() as cursor:

#             # --- BLOQUE 4: DEFINICIÓN DEL MOLDE (SQL) ---
#             # La sentencia es la misma que para un solo registro. 
#             # Los '%s' actúan como moldes para los datos que vendrán luego.
#             sentencia = 'INSERT INTO persona (nombre, apellido, email) VALUES (%s, %s, %s)'
            
#             # --- BLOQUE 5: ESTRUCTURA DE DATOS MASIVA ---
#             # Definimos una "Tupla de Tuplas". Cada tupla interna es una fila nueva.
#             # Esto permite organizar muchos datos antes de enviarlos.
#             valores = (
#                 ('Carlos', 'Lara', 'clara@gmail.com'),
#                 ('Ana', 'García', 'ana@gmail.com'),
#                 ('Luis', 'Pérez', 'luis@gmail.com')
#             )
            
#             # --- BLOQUE 6: EJECUCIÓN MÚLTIPLE (EL CAMBIO CLAVE) ---
#             # Usamos 'executemany' en lugar de 'execute'. 
#             # Este método recorre automáticamente la tupla de valores y ejecuta la sentencia por cada uno.
#             cursor.executemany(sentencia, valores)
            
#             # --- BLOQUE 7: CONTADOR DE IMPACTO ---
#             # rowcount nos dirá el total de filas insertadas (en este caso: 3).
#             registros_insertados = cursor.rowcount
#             print(f'Registros insertados: {registros_insertados}')

# # --- BLOQUE 8: CONTROL DE ERRORES ---
# # Captura errores, como por ejemplo si uno de los emails de la lista ya existe en la BD.
# except Exception as e:
#     print(f'Ocurrió un error: {e}')

# # --- BLOQUE 9: CIERRE DE CONEXIÓN ---
# # Siempre liberamos el recurso para mantener la salud del servidor.
# finally:
#     conexion.close()

# ¿Qué hace este código en texto (resumen)?
# Este script realiza una inserción masiva de datos en la tabla persona.

# Optimización: Utiliza la función executemany(), que es mucho más rápida que ejecutar muchos INSERT individuales, ya que optimiza la comunicación con PostgreSQL.

# Organización: Los datos se preparan en una estructura anidada (una tupla que contiene otras tuplas), donde cada elemento interno representa a una persona diferente.

# Seguridad y Transaccionalidad: Mantiene el uso de placeholders (%s) para evitar ataques y utiliza el bloque de conexión para asegurar que, o se insertan todos los nombres de la lista, o no se inserta ninguno si ocurre un error (integridad de datos).