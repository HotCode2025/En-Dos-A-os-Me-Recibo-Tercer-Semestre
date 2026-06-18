from modulos.inicio.inicio_controller import InicioControlador
from core.schema import crearTablasDB
if __name__ == "__main__":

    # creamos las tablas sistema. 
    crearTablasDB()
    
    app = InicioControlador()
    app.iniciar()