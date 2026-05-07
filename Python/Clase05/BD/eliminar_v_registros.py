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
            sentencia = 'DELETE FROM persona WHERE id_persona IN %s' #Esto es para definir la sentencia SQL para eliminar registros de la tabla persona, utilizando un placeholder para el valor del id_persona que se va a eliminar, pero utilizando la cláusula IN para permitir eliminar múltiples registros a la vez.
            entrada = input('Ingrese los id_persona a eliminar: ') #Esto es para definir el valor del id_persona que se va a utilizar en la sentencia SQL.
            valores = (tuple(entrada.split(',')),) #Esto es para convertir la entrada del usuario, que es una cadena de texto con los id_persona separados por comas, en una tupla de enteros, y luego envolver esa tupla en otra tupla para que sea compatible con el placeholder %s en la sentencia SQL.
            cursor.execute(sentencia, valores) #Esto es para ejecutar la sentencia SQL en la base de datos, pasando el valor del id_persona como parámetro. 
            registros_eliminados = cursor.rowcount #Esto es para obtener el número de registros que se han eliminado en la base de datos.
            print(f'Registros eliminados: {registros_eliminados}') #Esto es para imprimir el número de registros que se han eliminado en la base de datos.
except Exception as e: #Esto es para capturar cualquier excepción que pueda ocurrir durante la ejecución del programa.
    print(f'Ocurrió un error: {e}') #Esto es para imprimir un mensaje de error en caso de que ocurra una excepción.
finally: #Esto es para ejecutar el bloque de código que se encuentra dentro del bloque finally, sin importar si se produce una excepción o no.
    conexion.close() #Esto es para cerrar la conexión con la base de datos.