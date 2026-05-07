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
            sentencia = 'UPDATE PERSONA SET nombre= %s, apellido= %s, email= %s WHERE id_persona= %s' #Esto es para definir la sentencia SQL que se va a ejecutar, en este caso para actualizar los datos de una persona. #Placeholder para los valores de nombre, apellido, email y id_persona, que se van a pasar como parámetros en la ejecución de la sentencia SQL.
            valores = (
                ('Maximo', 'Gomez', 'maxigomez@gmail.com', 9),
                ('Ramiro', 'Muñoz', 'ramiromunoz2712@gmail.com', 5)
                ) #Esto es una tupla de tuplas para definir el valor de los placeholders de la sentencia SQL para actualizar los datos de las personas con id_persona igual a 9 y 5.
            cursor.executemany(sentencia, valores) #Esto es para ejecutar la sentencia SQL en la base de datos, pasando el valor del id_persona como parámetro. Se ha cambiado a executemany para permitir la actualización de múltiples registros.
            registros_actualizados = cursor.rowcount #Esto es para obtener el número de registros que se han actualizado en la base de datos.
            print(f'Registros actualizados: {registros_actualizados}') #Esto es para imprimir el número de registros que se han actualizado en la base de datos.
except Exception as e: #Esto es para capturar cualquier excepción que pueda ocurrir durante la ejecución del programa.
    print(f'Ocurrió un error: {e}') #Esto es para imprimir un mensaje de error en caso de que ocurra una excepción.
finally: #Esto es para ejecutar el bloque de código que se encuentra dentro del bloque finally, sin importar si se produce una excepción o no.
    conexion.close() #Esto es para cerrar la conexión con la base de datos.

#Explicacion del código:
# import psycopg2 # Adaptador para conectar Python con PostgreSQL

# # --- BLOQUE 1: CONFIGURACIÓN DE ACCESO ---
# # Credenciales para entrar al servidor de base de datos.
# conexion = psycopg2.connect(
#     user = 'postgres',
#     password = 'admin',
#     host = '127.0.0.1',
#     port = '5432',
#     database = 'test_bd'
# )

# try:
#     # --- BLOQUE 2: GESTIÓN DE TRANSACCIÓN ---
#     # Al editar múltiples filas, el 'with' asegura que si una falla, ninguna se guarde.
#     # Esto mantiene la consistencia de los datos (todo o nada).
#     with conexion:

#         # --- BLOQUE 3: EL CURSOR (EL INTERMEDIARIO) ---
#         # El objeto que transporta las órdenes SQL. Se cierra solo al salir del bloque.
#         with conexion.cursor() as cursor:

#             # --- BLOQUE 4: DEFINICIÓN DEL MOLDE (UPDATE) ---
#             # La sentencia indica qué columnas cambiar y usa el WHERE para filtrar por ID.
#             sentencia = 'UPDATE PERSONA SET nombre= %s, apellido= %s, email= %s WHERE id_persona= %s'
            
#             # --- BLOQUE 5: ESTRUCTURA DE DATOS MASIVA ---
#             # Una tupla de tuplas. Cada tupla interna contiene los nuevos datos y el ID
#             # de la persona específica que queremos modificar.
#             valores = (
#                 ('Maximo', 'Gomez', 'maxigomez@gmail.com', 9),
#                 ('Ramiro', 'Muñoz', 'ramiromunoz2712@gmail.com', 5)
#             )
            
#             # --- BLOQUE 6: ACTUALIZACIÓN MÚLTIPLE ---
#             # 'executemany' toma la sentencia y la aplica para cada tupla de datos.
#             # Es mucho más rápido que hacer varios 'execute' individuales.
#             cursor.executemany(sentencia, valores)
            
#             # --- BLOQUE 7: CONTEO DE FILAS AFECTADAS ---
#             # Devuelve el total de registros que fueron encontrados y modificados.
#             registros_actualizados = cursor.rowcount
#             print(f'Registros actualizados: {registros_actualizados}')

# # --- BLOQUE 8: CONTROL DE ERRORES ---
# # Captura problemas como IDs inexistentes, errores de red o emails duplicados.
# except Exception as e:
#     print(f'Ocurrió un error: {e}')

# # --- BLOQUE 9: CIERRE DE CONEXIÓN ---
# # Liberamos los recursos del sistema siempre, sin excepción.
# finally:
#     conexion.close()

# ¿Qué hace este código en texto (resumen)?
# Este script realiza una actualización masiva y selectiva de registros en la tabla persona.

# Eficiencia en Lote: A diferencia de un UPDATE simple, aquí se utiliza executemany() para procesar una lista de cambios. Esto reduce la carga sobre el servidor al enviar todas las modificaciones juntas.

# Identificación Precisa: Cada conjunto de datos en la tupla valores incluye su propio id_persona al final. Esto permite que el programa sepa exactamente que a la fila 9 le debe poner los datos de "Maximo" y a la fila 5 los de "Ramiro".

# Seguridad Transaccional: Al estar dentro de un bloque de transacción, se garantiza que si ocurre un error (por ejemplo, con los datos de Ramiro), los cambios de Maximo tampoco se apliquen, evitando que la base de datos quede "a medias".