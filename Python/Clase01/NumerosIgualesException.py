class NumerosIgualesException(Exception): # Creamos una clase que hereda de Exception para crear nuestra propia excepción personalizada
    def __init__(self, mensaje):
        self.mensaje = mensaje