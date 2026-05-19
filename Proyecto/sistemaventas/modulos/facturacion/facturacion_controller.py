from modulos.facturacion.facturacion_view import FacturacionView

class FacturacionController:

    def __init__(self, contenedor_derecho):
        # Guardamos la referencia de dónde se va a mostrar
        self.contenedor = contenedor_derecho
        self.facturacionVista = None

    def mostrarFacturacion(self):
        # 1. Limpiar el contenedor cada vez que se carga una vista nueva
        for widget in self.contenedor.winfo_children():
            widget.destroy()

        # 2. Crear la vista pasándole el contenedor como 'master'
        self.facturacionVista = FacturacionView(self.contenedor, self)
        
        # 3. Mostrarla ocupando todo el espacio
        self.facturacionVista.pack(fill="both", expand=True)