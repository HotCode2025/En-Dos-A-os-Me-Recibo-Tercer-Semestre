import os #libreria para manejar el sistema operativo
# El diagrama indica que los métodos son estáticos (static), lo que significa que no necesitamos crear un objeto de esta clase para usarlos. Su responsabilidad es gestionar el archivo de texto.

class CatalogoPeliculas:
    ruta_archivo = 'peliculas.txt' #atributo de clase, no es necesario crear un objeto para acceder a él, se crea de esta manera para que sea compartido por todos los objetos de la clase

    #Métodos
    @classmethod #decorador para indicar que es un método de clase, no necesita un objeto para ser llamado, se puede llamar directamente desde la clase
    def agregar_pelicula(cls, pelicula): #cls es el objeto de la clase
        with open(cls.ruta_archivo, 'a', encoding='utf8') as archivo: #with es una forma de manejar archivos que asegura que se cierren correctamente, 'a' es para agregar al final del archivo, encoding='utf8' para evitar problemas con caracteres especiales, entonces este método recibe un objeto de tipo Pelicula, lo que significa que el método agregar_pelicula espera recibir un objeto de la clase Pelicula como argumento, y luego accede a su atributo nombre para escribirlo en el archivo de texto.
            archivo.write(pelicula.nombre + '\n') #escribe el nombre de la película en el archivo, seguido de un salto de línea
        print(f'Pelicula "{pelicula.nombre}" agregada al catálogo con éxito.') 
        print()

    @classmethod
    def listar_peliculas(cls): 
        if os.path.exists(cls.ruta_archivo):
            with open(cls.ruta_archivo, 'r', encoding='utf8') as archivo:
                contenido = archivo.read() #lee el contenido del archivo

                #Verificamos si el contenido no está vacío
                if contenido.strip(): #strip() elimina los espacios en blanco al inicio y al final de la cadena
                    print(contenido) #imprime el contenido del archivo
                else:
                    print('No hay películas en el catálogo.')
        else:
            print('No hay un catálogo de películas para mostrar.')
            

    @classmethod
    def eliminar_peliculas(cls):
        if os.path.exists(cls.ruta_archivo): #verifica si el archivo existe
            os.remove(cls.ruta_archivo) #elimina el archivo
            print('Película eliminada con éxtito.')
        else:
            print('No hay un catálogo de películas para eliminar.')
            print()




    
