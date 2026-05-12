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
            sentencia = 'SELECT * FROM persona WHERE id_persona = %s' #Esto es para definir la sentencia SQL que se va a ejecutar. #Placeholder para el valor del id_persona, que se va a pasar como parámetro en la ejecución de la sentencia SQL.
            id_persona = input('Ingrese el id_persona: ') #Esto es para definir el valor del id_persona que se va a utilizar en la sentencia SQL.
            cursor.execute(sentencia, (id_persona,)) #Esto es para ejecutar la sentencia SQL en la base de datos, pasando el valor del id_persona como parámetro.
            registros = cursor.fetchone() #Esto es para obtener el primer registro que se encuentra en la base de datos que coincide con el id_persona especificado.
            # print(conexion) #Esto es para imprimir la conexión con la base de datos.
            print(registros) #Esto es para imprimir los registros obtenidos de la base de datos.
except Exception as e: #Esto es para capturar cualquier excepción que pueda ocurrir durante la ejecución del programa.
    print(f'Ocurrió un error: {e}') #Esto es para imprimir un mensaje de error en caso de que ocurra una excepción.
finally: #Esto es para ejecutar el bloque de código que se encuentra dentro del bloque finally, sin importar si se produce una excepción o no.
    conexion.close() #Esto es para cerrar la conexión con la base de datos.

#Explicacion del código:
# import psycopg2 # Importamos el adaptador para que Python "entienda" PostgreSQL

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
#     # 'with conexion' asegura que si hay cambios (INSERT/UPDATE), se confirmen (commit) 
#     # automáticamente al finalizar este bloque sin errores.
#     with conexion:

#         # --- BLOQUE 3: EL CURSOR (EL INTERMEDIARIO) ---
#         # El cursor es el objeto que realmente ejecuta el SQL y recorre los resultados.
#         # Al usar 'with', el cursor se cierra solo al terminar, liberando memoria.
#         with conexion.cursor() as cursor:

#             # --- BLOQUE 4: PREPARACIÓN Y SEGURIDAD ---
#             # Usamos '%s' como marcador de posición. Esto es VITAL: evita que un usuario 
#             # malintencionado inyecte código SQL dañino en el input.
#             sentencia = 'SELECT * FROM persona WHERE id_persona = %s'
#             id_persona = input('Ingrese el id_persona: ')
            
#             # --- BLOQUE 5: EJECUCIÓN ---
#             # Enviamos la sentencia y los datos por separado. 
#             # El cursor los une de forma segura antes de enviarlos a la base de datos.
#             cursor.execute(sentencia, (id_persona,))
            
#             # --- BLOQUE 6: RECUPERACIÓN DE DATOS ---
#             # fetchone() pide a la base de datos que nos devuelva solo una fila.
#             # Ideal cuando buscamos por un ID único.
#             registros = cursor.fetchone()
            
#             # Mostramos el resultado (una tupla con los datos de la persona).
#             print(registros)

# # --- BLOQUE 7: CONTROL DE ERRORES ---
# # Si la base de datos está caída o el SQL está mal escrito, el programa no muere;
# # captura el error y lo muestra de forma legible.
# except Exception as e:
#     print(f'Ocurrió un error: {e}')

# # --- BLOQUE 8: CIERRE DEFINITIVO ---
# # Pase lo que pase (haya error o no), cerramos la conexión. 
# # Esto es obligatorio para no dejar conexiones "colgadas" que consuman RAM en el servidor.
# finally:
#     conexion.close()

# 1. Consulta por ID Único (SELECT con un parámetro)
# ¿Qué hace?
# Busca una sola fila en la tabla persona utilizando su clave primaria.

# Lógica: Abre una conexión segura y utiliza un marcador de posición (%s) para filtrar por el ID que el usuario ingresa por teclado.

# Resultado: Utiliza cursor.fetchone(), que devuelve una tupla con los datos de esa persona específica o None si no la encuentra.

# Seguridad: Al usar %s, protege la base de datos contra ataques de inyección.