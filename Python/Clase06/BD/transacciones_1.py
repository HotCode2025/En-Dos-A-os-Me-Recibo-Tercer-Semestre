import psycopg2 as bd #Esto es para importar la libreria de psycopg2, que es un adaptador de base de datos para PostgreSQL en Python.
conexion = bd.connect( #Objeto de conexión a la base de datos, que se crea utilizando la función connect de psycopg2.
    user = 'postgres',
    password = 'admin',
    host = '127.0.0.1',
    port = '5432',
    database = 'test_bd'
) #Esto es para establecer la conexión con la base de datos.

try: #Esto es para intentar ejecutar el bloque de código que se encuentra dentro del bloque try, y capturar cualquier excepción que pueda ocurrir durante la ejecución del programa.
    # conexion.autocommit = False #Esto es para desactivar el autocommit de la conexión, lo que significa que los cambios realizados en la base de datos no se confirmarán automáticamente, sino que se tendrán que confirmar manualmente utilizando el método commit de la conexión.
    cursor = conexion.cursor() #Esto es para crear un cursor utilizando el método cursor de la conexión, que es el objeto que realmente ejecuta el SQL y recorre los resultados.
    sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)' #Esto es para definir la sentencia SQL para insertar un nuevo registro en la tabla persona, utilizando placeholders para los valores de nombre, apellido y email que se van a insertar.
    valores = ('Maria', 'Gomez', 'maria@gmail.com') #Esto es para definir el valor de los placeholders de la sentencia SQL.
    cursor.execute(sentencia, valores) #Esto es para ejecutar la sentencia SQL en la base de datos, pasando los valores como parámetros.
    print('Termina la transacción') #Esto es para imprimir un mensaje indicando que la transacción ha terminado, pero los cambios aún no se han confirmado en la base de datos.
    conexion.commit() #Esto es para confirmar los cambios realizados en la base de datos utilizando el método commit de la conexión.
except Exception as e: #Esto es para capturar cualquier excepción que pueda ocurrir durante la ejecución del programa.
    conexion.rollback() #Esto es para deshacer los cambios realizados en la base de datos utilizando el método rollback de la conexión, en caso de que ocurra una excepción durante la ejecución del programa.
    print(f'Ocurrió un error, se hizo un rollback: {e}') #Esto es para imprimir un mensaje de error en caso de que ocurra una excepción.
finally: #Esto es para ejecutar el bloque de código que se encuentra dentro del bloque finally, sin importar si se produce una excepción o no.
    conexion.close() #Esto es para cerrar la conexión con la base de datos.