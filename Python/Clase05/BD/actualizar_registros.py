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
            valores = ('Juan Carlos', 'Roldan', 'juanroldan@gmail.com', 1) #Esto es para definir el valor de los placeholders de la sentencia SQL para actualizar los datos de la persona con id_persona igual a 1.
            cursor.execute(sentencia, valores) #Esto es para ejecutar la sentencia SQL en la base de datos, pasando el valor del id_persona como parámetro. 
            registros_actualizados = cursor.rowcount #Esto es para obtener el número de registros que se han actualizado en la base de datos.
            print(f'Registros actualizados: {registros_actualizados}') #Esto es para imprimir el número de registros que se han actualizado en la base de datos.
except Exception as e: #Esto es para capturar cualquier excepción que pueda ocurrir durante la ejecución del programa.
    print(f'Ocurrió un error: {e}') #Esto es para imprimir un mensaje de error en caso de que ocurra una excepción.
finally: #Esto es para ejecutar el bloque de código que se encuentra dentro del bloque finally, sin importar si se produce una excepción o no.
    conexion.close() #Esto es para cerrar la conexión con la base de datos.

#Explicacion del código:
# import psycopg2 # Importamos el adaptador para conectar Python con PostgreSQL

# # --- BLOQUE 1: CONFIGURACIÓN DE ACCESO ---
# # Establecemos las credenciales para conectarnos al servidor local.
# conexion = psycopg2.connect(
#     user = 'postgres',
#     password = 'admin',
#     host = '127.0.0.1',
#     port = '5432',
#     database = 'test_bd'
# )

# try:
#     # --- BLOQUE 2: GESTIÓN DE TRANSACCIÓN ---
#     # Al ser una edición de datos, 'with conexion' asegura que el cambio sea permanente (Commit).
#     # Si algo falla antes de terminar el bloque, no se guarda nada (Rollback).
#     with conexion:

#         # --- BLOQUE 3: EL CURSOR (EL INTERMEDIARIO) ---
#         # Creamos el cursor que llevará la orden de actualización a la base de datos.
#         with conexion.cursor() as cursor:

#             # --- BLOQUE 4: DEFINICIÓN DE LA SENTENCIA (UPDATE) ---
#             # 'UPDATE' modifica columnas específicas. 'WHERE' es VITAL para indicar
#             # exactamente qué fila queremos cambiar y no afectar a toda la tabla.
#             sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            
#             # --- BLOQUE 5: VALORES NUEVOS ---
#             # Pasamos los nuevos datos y, al final, el ID de la persona que queremos editar.
#             # El orden en la tupla debe ser el mismo que el de los %s en la sentencia.
#             valores = ('Juan Carlos', 'Roldan', 'juanroldan@gmail.com', 1)
            
#             # --- BLOQUE 6: EJECUCIÓN ---
#             # El cursor combina la sentencia SQL con los valores de forma segura.
#             cursor.execute(sentencia, valores)
            
#             # --- BLOQUE 7: VERIFICACIÓN DE CAMBIOS ---
#             # .rowcount nos dice cuántas filas se modificaron. Si el ID no existe, devolverá 0.
#             registros_actualizados = cursor.rowcount
#             print(f'Registros actualizados: {registros_actualizados}')

# # --- BLOQUE 8: CONTROL DE ERRORES ---
# # Captura errores de sintaxis o problemas de restricción (ej: poner un email que ya existe).
# except Exception as e:
#     print(f'Ocurrió un error: {e}')

# # --- BLOQUE 9: CIERRE DE CONEXIÓN ---
# # Liberamos la conexión para mantener el servidor optimizado.
# finally:
#     conexion.close()

# ¿Qué hace este código en texto (resumen)?
# Este script realiza la modificación de un registro existente en la tabla persona.

# Modificación Selectiva: Utiliza el comando SQL UPDATE junto con la cláusula WHERE para localizar a una persona específica mediante su id_persona (en este caso, el ID 1) y sobreescribir sus campos nombre, apellido y email.

# Integridad de Datos: Gracias al bloque with conexion, el programa garantiza que los cambios se guarden correctamente. Si por algún motivo la base de datos rechazara el cambio, el sistema no quedaría en un estado inconsistente.

# Confirmación: Al finalizar, informa con precisión cuántas filas fueron alteradas mediante rowcount, lo que permite confirmar si el registro realmente existía y fue actualizado.