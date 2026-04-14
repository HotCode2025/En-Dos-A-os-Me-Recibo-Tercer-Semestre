#Declaramos una variable
try:
    archivo = open("prueba.txt", "w", encoding='utf8') #La W es de write que significa escribir
    archivo.write("Programamos con diferentes tipos de archivos, ahora en txt.\n")
    archivo.write("Los acentos son importantes para las palabras \n")
    archivo.write("como por ejemplo: acción, ejecución y producción \n")
    archivo.write("Las letras son:\nr: leer, \nw: escribe , \na: anexa, \nx: crea un archivo")
    archivo.write("\nt: esta es para texto o text, \nb: archivo binario, \nw+: leer y escribir, \nr+: lo mismo que la anterior")
    archivo.write("Saludos a todos los alumnos de la tecnicatura")
    archivo.write("\nCon esto terminamos")
except Exception as e:
    print(e)
finally: #Siempre se ejecuta
    archivo.close() # Con esto se debe cerrar el archivo
#archivo.write("Todo quedó perfecto") error que se suele cometer, ya que el archivo ya cerró
