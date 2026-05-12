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
            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s' #Esto es para definir la sentencia SQL que se va a ejecutar. #Placeholder para el valor del id_persona, que se va a pasar como parámetro en la ejecución de la sentencia SQL.
            entrada = input('Ingrese los id_persona separados por coma: ') #Esto es para definir el valor del id_persona que se va a utilizar en la sentencia SQL.
            llaves_primarias = (tuple(entrada.split(',')),) #Esto es para convertir la entrada del usuario en una tupla de tuplas, que es el formato esperado por el placeholder %s en la sentencia SQL.
            cursor.execute(sentencia, llaves_primarias) #Esto es para ejecutar la sentencia SQL en la base de datos, pasando el valor del id_persona como parámetro.
            registros = cursor.fetchall() #Esto es para obtener todos los registros que se encuentran en la base de datos que coinciden con el id_persona especificado.
            for i in registros:
                print(i)
except Exception as e: #Esto es para capturar cualquier excepción que pueda ocurrir durante la ejecución del programa.
    print(f'Ocurrió un error: {e}') #Esto es para imprimir un mensaje de error en caso de que ocurra una excepción.
finally: #Esto es para ejecutar el bloque de código que se encuentra dentro del bloque finally, sin importar si se produce una excepción o no.
    conexion.close() #Esto es para cerrar la conexión con la base de datos.

#Explicacion del código:
# import psycopg2 # Importamos el adaptador para conectar Python con PostgreSQL

# # --- BLOQUE 1: CONFIGURACIÓN DE ACCESO ---
# # Definimos las credenciales necesarias para establecer el puente con el servidor.
# conexion = psycopg2.connect(
#     user = 'postgres',
#     password = 'admin',
#     host = '127.0.0.1',
#     port = '5432',
#     database = 'test_bd'
# )

# try:
#     # --- BLOQUE 2: GESTIÓN DE TRANSACCIÓN ---
#     # Asegura que la operación sea atómica: si algo falla dentro, no se aplica ningún cambio.
#     with conexion:

#         # --- BLOQUE 3: EL CURSOR (EL INTERMEDIARIO) ---
#         # Creamos el objeto que enviará los comandos SQL. 
#         # El 'with' garantiza que el cursor se cierre al terminar de procesar los datos.
#         with conexion.cursor() as cursor:

#             # --- BLOQUE 4: PREPARACIÓN Y LÓGICA DE ENTRADA ---
#             # 'IN %s' permite buscar una lista de valores en lugar de uno solo.
#             sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'
#             entrada = input('Ingrese los id_persona separados por coma (ej: 1,2,3): ')
            
#             # --- BLOQUE 5: FORMATEO DE DATOS (CRUCIAL) ---
#             # 1. split(',') convierte el texto "1,2" en una lista ['1', '2'].
#             # 2. tuple(...) lo convierte en tupla, que es lo que SQL entiende para el operador IN.
#             # 3. La coma final (...,) crea la tupla de tuplas que requiere el método execute.
#             llaves_primarias = (tuple(entrada.split(',')),)
            
#             # --- BLOQUE 6: EJECUCIÓN ---
#             # El cursor inyecta la tupla de IDs de forma segura en la sentencia SQL.
#             cursor.execute(sentencia, llaves_primarias)
            
#             # --- BLOQUE 7: RECUPERACIÓN MULTIPLE ---
#             # fetchall() a diferencia de fetchone(), trae TODOS los registros que coincidieron.
#             # Devuelve una lista de tuplas.
#             registros = cursor.fetchall()
            
#             # --- BLOQUE 8: PROCESAMIENTO DE RESULTADOS ---
#             # Usamos un ciclo for para recorrer la lista y mostrar cada persona por separado.
#             for i in registros:
#                 print(i)

# # --- BLOQUE 9: CONTROL DE ERRORES ---
# # Captura fallas, como por ejemplo si el usuario ingresa letras en lugar de números.
# except Exception as e:
#     print(f'Ocurrió un error: {e}')

# # --- BLOQUE 10: CIERRE DE CONEXIÓN ---
# # Siempre cerramos el canal de comunicación para liberar recursos en nuestra PC y el servidor.
# finally:
#     conexion.close()

# 1. Consulta por ID Único (SELECT con un parámetro)
# ¿Qué hace?
# Busca una sola fila en la tabla persona utilizando su clave primaria.

# Lógica: Abre una conexión segura y utiliza un marcador de posición (%s) para filtrar por el ID que el usuario ingresa por teclado.

# Resultado: Utiliza cursor.fetchone(), que devuelve una tupla con los datos de esa persona específica o None si no la encuentra.

# Seguridad: Al usar %s, protege la base de datos contra ataques de inyección.

# 2. Consulta Múltiple Dinámica (SELECT con operador IN)
# ¿Qué hace?
# Permite buscar y traer varios registros al mismo tiempo enviando una lista de IDs.

# Lógica: Captura una cadena de texto (ej: "1,2,3"), la convierte en una tupla de Python y se la pasa al operador IN de SQL.

# Resultado: Utiliza cursor.fetchall(), que devuelve una lista de tuplas. Luego, recorre esa lista con un ciclo for para imprimir cada registro encontrado.

# Dato técnico: Es más eficiente que hacer varios SELECT por separado porque hace un solo viaje a la base de datos.
