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
            sentencia = 'DELETE FROM persona WHERE id_persona= %s' #Esto es para definir la sentencia SQL que se va a ejecutar, en este caso para eliminar una persona. #Placeholder para el valor de id_persona, que se va a pasar como parámetro en la ejecución de la sentencia SQL.
            entrada = input('Ingrese el id_persona a eliminar: ') #Esto es para definir el valor del id_persona que se va a utilizar en la sentencia SQL.
            valores = (int(entrada),) #Esto es para definir el valor del placeholder de la sentencia SQL para eliminar la persona con id_persona igual a 7. Se debe colocar una coma después del número para indicar que es una tupla de un solo elemento.
            cursor.execute(sentencia, valores) #Esto es para ejecutar la sentencia SQL en la base de datos, pasando el valor del id_persona como parámetro. 
            registros_eliminados = cursor.rowcount #Esto es para obtener el número de registros que se han eliminado en la base de datos.
            print(f'Registros eliminados: {registros_eliminados}') #Esto es para imprimir el número de registros que se han eliminado en la base de datos.
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
#     # El 'with' es CRÍTICO en el DELETE. Si borrás algo por error y el código falla,
#     # el sistema puede hacer un Rollback para evitar la pérdida de datos.
#     with conexion:

#         # --- BLOQUE 3: EL CURSOR (EL INTERMEDIARIO) ---
#         # Creamos el objeto que enviará la orden de eliminación. Se cierra automáticamente.
#         with conexion.cursor() as cursor:

#             # --- BLOQUE 4: DEFINICIÓN DE LA SENTENCIA (DELETE) ---
#             # 'DELETE FROM' quita filas. El 'WHERE' es OBLIGATORIO para no borrar toda la tabla.
#             sentencia = 'DELETE FROM persona WHERE id_persona = %s'
            
#             # --- BLOQUE 5: ENTRADA Y FORMATEO ---
#             # Capturamos el ID del usuario y lo convertimos a entero.
#             # Se usa una tupla con coma final (id,) para que Python lo reconozca como tal.
#             entrada = input('Ingrese el id_persona a eliminar: ')
#             valores = (int(entrada),)
            
#             # --- BLOQUE 6: EJECUCIÓN ---
#             # El cursor envía la orden de borrar al registro que coincida con el ID.
#             cursor.execute(sentencia, valores)
            
#             # --- BLOQUE 7: VERIFICACIÓN DE IMPACTO ---
#             # rowcount confirma si realmente se borró algo. Si el ID no existía, dirá 0.
#             registros_eliminados = cursor.rowcount
#             print(f'Registros eliminados: {registros_eliminados}')

# # --- BLOQUE 8: CONTROL DE ERRORES ---
# # Captura fallas como errores de sintaxis o restricciones de integridad (ej: no podés
# # borrar una persona que tiene datos vinculados en otras tablas).
# except Exception as e:
#     print(f'Ocurrió un error: {e}')

# # --- BLOQUE 9: CIERRE DE CONEXIÓN ---
# # Siempre cerramos el túnel al finalizar para liberar recursos del servidor.
# finally:
#     conexion.close()

# ¿Qué hace este código en texto (resumen)?
# Este script realiza la eliminación definitiva de un registro específico en la tabla persona.

# Eliminación Controlada: Utiliza la instrucción SQL DELETE junto con un filtro WHERE. Esto es vital para asegurar que solo se elimine la fila que coincide con el ID ingresado y no se vacíe toda la tabla accidentalmente.

# Conversión de Datos: A diferencia de otros ejemplos, aquí se asegura de convertir la entrada del usuario (input) a un entero (int), lo cual es una buena práctica de validación antes de enviarlo a la base de datos.

# Seguridad Transaccional: Al estar dentro de un bloque with conexion, la eliminación solo se confirma (Commit) si el bloque termina sin errores. Si algo sale mal, el registro no se borra.

# Confirmación de Acción: Informa mediante rowcount si la operación tuvo éxito. Esto es útil porque si ponés un ID que no existe, el programa no dará error, pero te avisará que se eliminaron "0" registros.