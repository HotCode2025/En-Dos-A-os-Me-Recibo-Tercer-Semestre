#Un error o una excepcion es cuando nuestro programa termina de manera abrupta e inesperada.
#Para evitar esto, podemos usar el manejo de excepciones, que nos permite controlar los errores y evitar que nuestro programa termine de manera inesperada.
#El manejo de excepciones se realiza con la palabra reservada "try" y "except". El bloque de código que puede generar un error se coloca dentro del bloque "try", y el bloque de código que se ejecuta si ocurre un error se coloca dentro del bloque "except".

from NumerosIgualesException import NumerosIgualesException

resultado = None

try: # Bloque de código que puede generar un error
    a = int(input("Ingrese un número: "))
    b = int(input("Ingrese otro número: "))
    if a == b:
        raise NumerosIgualesException("Los números ingresados son iguales") # Si los números son iguales, se lanza una excepción personalizada. La palabra reservada "raise" se utiliza para lanzar una excepción.
    resultado = a / b
except TypeError as e: # Bloque de código que se ejecuta si ocurre un error de tipo TypeError
    print(f"TypeError: {type(e)}")
except ZeroDivisionError as e: # Bloque de código que se ejecuta si ocurre un error de tipo ZeroDivisionError
    print(f"ZeroDivisionError: {type(e)}")
except Exception as e: # Bloque de código que se ejecuta si ocurre un error de tipo Exception (clase base de todas las excepciones)
    print(f"Exception: {type(e)}")
else: # Bloque de código que se ejecuta si no ocurre ningún pygame.freetype.get_error() 
    print("No se produjo ningún error/excepción")
finally: # Bloque de código que se ejecuta siempre, independientemente de si se produjo un error o no
    print("Se ejecutó el bloque finally")


print(f"El resultado es: {resultado}")
