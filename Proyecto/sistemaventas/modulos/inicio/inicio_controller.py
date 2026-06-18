from modulos.inicio.inicio_view import Inicio
from modulos.productos.productos_controller import ProductosController
from modulos.clientes.clientes_controller import ClientesController
from modulos.facturacion.facturacion_controller import FacturacionController
from modulos.dashboard.dashboard_controller import DashboardController
from modulos.configuracion.configuracion_controller import ConfiguracionController

class InicioControlador:
    def __init__(self):
        self.vistaInicio = Inicio(self)
     # Variable para rastrear qué estamos viendo (None al empezar). Sirve para no cargar nuevamente una vista si nos encontramos en ella. 
        self.vista_actual = None 
    # LE PASAMOS el frame derecho de la vista (main_view)
        self.productos_control = ProductosController(self.vistaInicio.main_view)
        self.clientesController = ClientesController(self.vistaInicio.main_view)
        self.facturacionController = FacturacionController(self.vistaInicio.main_view)
        self.dashboardController = DashboardController(self.vistaInicio.main_view)
        self.configuracionController = ConfiguracionController(self.vistaInicio.main_view)
        # cargamos el Dashboard al iniciar la App. 
        self.mostrarDashboard()
    
    # 3. Métodos para mostrar los módulos. 
    def mostrarProductos(self):
        # Si ya estamos en el productos, no hacemos nada
        if self.vista_actual == "productos":
            return
        # Le pedimos al controlador de productos que dibuje su vista
        self.productos_control.mostrarProductos()
        self.vista_actual = "productos"
        
    def mostrarClientes(self): 
        if self.vista_actual == "clientes": 
            return
        
        self.clientesController.mostrarClientes()
        self.vista_actual = "clientes"
        
    def mostrarConfiguracion(self):
        if self.vista_actual == "configuracion":
            return
        
        self.configuracionController.mostrarConfiguracion()
        self.vista_actual = "configuracion"
        
    def mostrarFacturacion(self): 
        if self.vista_actual == "facturacion": 
            return
        
        self.facturacionController.mostrarFacturacion()
        self.vista_actual = "facturacion"
        
    def mostrarDashboard(self):
        # Si ya estamos en el dashboard, no hacemos nada
        if self.vista_actual == "dashboard":
            return
        self.dashboardController.mostrarDashboard()
        self.vista_actual = "dashboard" # Actualizamos el estado
    
    def iniciar(self):
        self.vistaInicio.mainloop()