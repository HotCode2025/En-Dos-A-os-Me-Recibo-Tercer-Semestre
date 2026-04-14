#MANEJO DE CONTEXTO WITH: sintaxis simplificad (no es necesario el bloque try y finally)
#with open("prueba.txt", "r",encoding="utf8") as archivo:
#    print(archivo.read())
#En el contexto de with lo qye se ejecuta de manera automatica son los metodos
#utiliza diferentes metodos: __enter__ este es el que abre
#ahora el siguiente metodo es el que cierra: __exit__
from manejoArchivo import ManejoArchivos

with ManejoArchivos("prueba.txt") as archivo:
    print(archivo.read())