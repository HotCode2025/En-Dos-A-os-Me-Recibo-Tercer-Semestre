
archivo = open("prueba.txt", "r", encoding="utf8") #Las letras son: "r", "w", "a", "x"
#print(archivo.read())
#print(archivo.read(15))
#print(archivo.read(5)) # Continua desde la linea anterior
#print(archivo.readline())

#vamos a iterar el archivo

#for linea in archivo:
    #print(linea)
#print(archivo.readlines()[12]) #accedemos al archivo como si fuera una lista

#Anexamos informacion, copiamos a otro
archivo2 = open("copia.txt","a",encoding="utf8")
archivo2.write(archivo.read())
archivo.close() # cerramos el primer archivo
archivo2.close() # cerramos el segundo archivo

print("Se ha terminado el proceso de leer y copiar")

