from dominio.Pelicula import Pelicula
from servicio.CatalogoPeliculas import CatalogoPeliculas

def menu():
    opcion = 0
    while opcion != 4:
        print('Opciones:')
        print('1. Agregar película')
        print('2. Listar películas')
        print('3. Eliminar catálogo de películas')
        print('4. Salir')
        opcion = int(input('Seleccione una opción: '))
        if opcion == 1:
            nombre_pelicula = input('Ingrese el nombre de la película: ')
            pelicula = Pelicula(nombre_pelicula)
            CatalogoPeliculas.agregar_pelicula(pelicula)
        elif opcion == 2:
            print()
            print(' --- Catálogo de películas ---')
            CatalogoPeliculas.listar_peliculas()
        elif opcion == 3:
            CatalogoPeliculas.eliminar_peliculas()
        elif opcion == 4:
            print('Saliendo del programa...')
        else:
            print('Opción inválida')


if __name__ == '__main__':
    menu()


