from modulos.inicio.inicio_view import Inicio
from modulos.productos.productos_controller import ProductosController
from modulos.clientes.clientes_controller import ClientesController
class InicioControlador:
    def __init__(self):
        self.vistaInicio = Inicio(self)
    # LE PASAMOS el frame derecho de la vista (main_view)
        self.productos_control = ProductosController(self.vistaInicio.main_view)
        self.clientesController = ClientesController(self.vistaInicio.main_view)
    # 3. Métodos para mostrar los módulos. 
    def mostrarProductos(self):
        # Le pedimos al controlador de productos que dibuje su vista
        self.productos_control.mostrarProductos()
        
    def mostrarClientes(self): 
        self.clientesController.mostrarClientes()
    
    def iniciar(self):
        self.vistaInicio.mainloop()
        
        
        



    
