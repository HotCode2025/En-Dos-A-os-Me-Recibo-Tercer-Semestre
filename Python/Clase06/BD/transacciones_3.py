import psycopg2 as bd #Esto es para importar la libreria de psycopg2, que es un adaptador de base de datos para PostgreSQL en Python.
conexion = bd.connect( #Objeto de conexión a la base de datos, que se crea utilizando la función connect de psycopg2.
    user = 'postgres',
    password = 'admin',
    host = '127.0.0.1',
    port = '5432',
    database = 'test_bd'
) #Esto es para establecer la conexión con la base de datos.

try: #Esto es para intentar ejecutar el bloque de código que se encuentra dentro del bloque try, y capturar cualquier excepción que pueda ocurrir durante la ejecución del programa.
    with conexion: #Esto es para utilizar la conexión como un contexto, lo que significa que se encargará de manejar automáticamente la apertura y cierre de la conexión, así como el manejo de transacciones.
        with conexion.cursor() as cursor: 
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)' #Esto es para definir la sentencia SQL para insertar un nuevo registro en la tabla persona, utilizando placeholders para los valores de nombre, apellido y email que se van a insertar.
            valores = ('Alex', 'Rojas', 'alexrojas@gmail.com') #Esto es para definir el valor de los placeholders de la sentencia SQL.
            cursor.execute(sentencia, valores) #Esto es para ejecutar la sentencia SQL en la base de datos, pasando los valores como parámetros.

            sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s' #Esto es para definir la sentencia SQL para actualizar un registro en la tabla persona, utilizando placeholders para los valores de nombre, apellido, email y id_persona que se van a actualizar.
            valores = ('Juan Carlos', 'Roldan', 'juanroldan@gmail.com', 1) #Esto es para definir el valor de los placeholders de la sentencia SQL.
            cursor.execute(sentencia, valores) #Esto es para ejecutar la sentencia SQL en la base de datos, pasando los valores como parámetros.

except Exception as e: #Esto es para capturar cualquier excepción que pueda ocurrir durante la ejecución del programa.
    print(f'Ocurrió un error, se hizo un rollback: {e}') #Esto es para imprimir un mensaje de error en caso de que ocurra una excepción.
finally: #Esto es para ejecutar el bloque de código que se encuentra dentro del bloque finally, sin importar si se produce una excepción o no.
    conexion.close() #Esto es para cerrar la conexión con la base de datos.

print('Termina la transacción') #Esto es para imprimir un mensaje indicando que la transacción ha terminado, pero los cambios aún no se han confirmado en la base de datos.

#Esta es la mejor práctica para manejar transacciones en Python con psycopg2, ya que el uso de 'with' garantiza que la conexión se cierre correctamente y que cualquier error durante la ejecución de las sentencias SQL provoque un rollback automático, evitando así la pérdida de datos.