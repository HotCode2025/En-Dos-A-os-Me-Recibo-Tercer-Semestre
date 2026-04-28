import psycopg2 #Esto es para importar la libreria de psycopg2, que es un adaptador de base de datos para PostgreSQL en Python.
conexion = psycopg2.connect( #Objeto de conexión a la base de datos, que se crea utilizando la función connect de psycopg2.
    user = 'postgres',
    password = 'admin',
    host = '127.0.0.1',
    port = '5432',
    database = 'test_bd'
) #Esto es para establecer la conexión con la base de datos.

cursor = conexion.cursor() #Esto es para crear un cursor, que es un objeto que permite ejecutar comandos SQL en la base de datos.
sentencia = 'SELECT * FROM persona' #Esto es para definir la sentencia SQL que se va a ejecutar
cursor.execute(sentencia) #Esto es para ejecutar la sentencia SQL en la base de datos.
registros = cursor.fetchall() #Esto es para obtener todos los registros que se han devuelto por la sentencia SQL.

# print(conexion) #Esto es para imprimir la conexión con la base de datos.
print(registros) #Esto es para imprimir los registros obtenidos de la base de datos.

cursor.close() #Esto es para cerrar el cursor.
conexion.close() #Esto es para cerrar la conexión con la base de datos.