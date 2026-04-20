class Pelicula:
    def __init__(self, nombre):
        #Constructor 
        self.nombre = nombre 
    #Str 
    def __str__(self):
        return f'Pelicula: {self.nombre}'

        #Métodos
    @property #decorador
    def get_nombre(self): #getter
        return self.nombre
        
    

    

    
