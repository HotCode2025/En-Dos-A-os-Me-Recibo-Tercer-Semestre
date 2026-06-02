from logger_base import log

class Persona:
    # Constructor
    def __init__(self, id_persona=None, nombre=None, apellido=None, email=None):
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._email = email

    # ToString
    def __str__(self):
        return f'''
        Id Persona: {self._id_persona}
        Nombre: {self._nombre}
        Apellido: {self._apellido}
        Email: {self._email}
        '''
    
    # Getters y Setters
    @property
    def id_persona(self):
        return self._id_persona
    
    @id_persona.setter
    def id_persona(self, id_persona):
        self._id_persona = id_persona    

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido    

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        self._email = email

if __name__ == "__main__":
    persona1 = Persona(1, "Ramiro", "Muñoz", "ramiromunoz2712@gmail.com")
    log.debug(persona1)
    persona2 = Persona(nombre="Jose", apellido="Perez", email="joseperezgmail.com")
    log.debug(persona2)
    persona3 = Persona(id_persona= 1)
    log.debug(persona3)


'''
EXPLICACIÓN DEL CÓDIGO - CLASE PERSONA (CAPA DE DOMINIO)

1. IMPORTACIÓN:
   - 'from logger_base import log': Importa el configurador de bitácora para 
     mostrar mensajes en consola y archivo en lugar de usar print().

2. DEFINICIÓN DE CLASE Y ENCAPSULAMIENTO:
   - 'class Persona': Define el molde para crear objetos de tipo persona.
   - 'self._id_persona': El uso del guion bajo (_) indica que el atributo es 
     "protegido" (encapsulado). No se debe acceder a él directamente desde afuera.

3. CONSTRUCTOR (__init__):
   - Se ejecuta al crear el objeto (ej: persona1 = Persona(...)).
   - Usa parámetros con '=None' para que los argumentos sean opcionales. Esto 
     permite crear objetos solo con ID, solo con nombre, o completos.

4. MÉTODO __str__ (ToString):
   - Es un método especial (dunder method).
   - Define qué se muestra cuando hacemos 'log.debug(persona1)'. 
   - Sin este método, Python mostraría una dirección de memoria ilegible.

5. DECORADORES @property (GETTERS):
   - Permiten leer los atributos protegidos como si fueran públicos.
   - Ejemplo: 'print(persona.nombre)' llama internamente a este método.
   - IMPORTANTE: Debe retornar 'self._nombre' (con guion bajo) para evitar 
     que la función se llame a sí misma infinitamente.

6. SETTERS (@nombre.setter):
   - Permiten modificar los atributos protegidos con validación o lógica extra.
   - Ejemplo: 'persona.nombre = "Nuevo"' llama a este método.

7. BLOQUE DE PRUEBA (if __name__ == "__main__"):
   - 'persona1': Instancia usando argumentos posicionales (en orden).
   - 'persona2': Instancia usando argumentos nombrados (key=value).
   - 'persona3': Instancia mínima (solo ID), útil para búsquedas o eliminaciones.
'''