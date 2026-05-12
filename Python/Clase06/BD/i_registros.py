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
            valores = ('Carlos', 'Lara', 'clara@gmail.com') #Esto es para definir el valor de los placeholders de la sentencia SQL.
            cursor.execute(sentencia, valores) #Esto es para ejecutar la sentencia SQL en la base de datos, pasando el valor del id_persona como parámetro.
            registros_insertados = cursor.rowcount #Esto es para obtener el número de registros que se han insertado en la base de datos.
            print(f'Registros insertados: {registros_insertados}') #Esto es para imprimir el número de registros que se han insertado en la base de datos.
except Exception as e: #Esto es para capturar cualquier excepción que pueda ocurrir durante la ejecución del programa.
    print(f'Ocurrió un error: {e}') #Esto es para imprimir un mensaje de error en caso de que ocurra una excepción.
finally: #Esto es para ejecutar el bloque de código que se encuentra dentro del bloque finally, sin importar si se produce una excepción o no.
    conexion.close() #Esto es para cerrar la conexión con la base de datos.

#Explicacion del código:
# import psycopg2 # Adaptador para conectar Python con PostgreSQL

# # --- BLOQUE 1: CONFIGURACIÓN DE ACCESO ---
# # Establecemos las credenciales para abrir el túnel hacia el servidor.
# conexion = psycopg2.connect(
#     user = 'postgres',
#     password = 'admin',
#     host = '127.0.0.1',
#     port = '5432',
#     database = 'test_bd'
# )

# try:
#     # --- BLOQUE 2: GESTIÓN DE TRANSACCIÓN (COMMIT/ROLLBACK) ---
#     # En operaciones de escritura (INSERT), 'with conexion' es vital. 
#     # Si el código llega al final del bloque sin errores, hace un COMMIT (guarda los cambios).
#     # Si algo falla, hace un ROLLBACK (deshace el intento) para no dejar datos corruptos.
#     with conexion:

#         # --- BLOQUE 3: EL CURSOR (EL EJECUTOR) ---
#         # Creamos el cursor para enviar los comandos. Al terminar el bloque, se cierra solo.
#         with conexion.cursor() as cursor:

#             # --- BLOQUE 4: DEFINICIÓN DE LA TAREA ---
#             # Preparamos la sentencia INSERT. Usamos tres %s como moldes para los datos.
#             sentencia = 'INSERT INTO persona (nombre, apellido, email) VALUES (%s, %s, %s)'
            
#             # --- BLOQUE 5: PREPARACIÓN DE DATOS ---
#             # Agrupamos los datos en una tupla. El orden debe coincidir exacto con la sentencia.
#             valores = ('Carlos', 'Lara', 'clara@gmail.com')
            
#             # --- BLOQUE 6: EJECUCIÓN DEL COMANDO ---
#             # El cursor combina la sentencia con los valores de forma segura y la envía a la BD.
#             cursor.execute(sentencia, valores)
            
#             # --- BLOQUE 7: CONFIRMACIÓN DE IMPACTO ---
#             # .rowcount nos devuelve un número entero con la cantidad de filas afectadas.
#             # En este caso, debería devolver 1 si la inserción fue exitosa.
#             registros_insertados = cursor.rowcount
#             print(f'Registros insertados: {registros_insertados}')

# # --- BLOQUE 8: CONTROL DE EXCEPCIONES ---
# # Atrapa errores comunes: por ejemplo, si el email ya existe (si es UNIQUE) 
# # o si falta un campo obligatorio en la tabla.
# except Exception as e:
#     print(f'Ocurrió un error: {e}')

# # --- BLOQUE 9: CIERRE SEGURO ---
# # Liberamos la conexión. Es la "buena práctica" que evita saturar el servidor de BD.
# finally:
#     conexion.close()

# 3. Inserción de Datos (INSERT INTO)
# ¿Qué hace?
# Agrega un nuevo registro (una nueva persona) de forma permanente a la base de datos.

# Lógica: Define los campos donde se va a escribir (nombre, apellido, email) y envía los valores agrupados en una tupla.

# El rol del Commit: Aquí el bloque with conexion es fundamental; si el código se ejecuta correctamente, "confirma" la operación (Commit). Si hay un error, la deshace (Rollback).

# Resultado: Utiliza cursor.rowcount para informarte cuántas filas se insertaron exitosamente (en este caso, 1).