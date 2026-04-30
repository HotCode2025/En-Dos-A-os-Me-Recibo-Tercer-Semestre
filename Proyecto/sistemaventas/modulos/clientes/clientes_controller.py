from modulos.clientes.clientes_view import ClientesView
class ClientesController: 
    def __init__(self, contenedor_derecho):
        # Guardamos la referencia de dónde se va a mostrar
        self.contenedor = contenedor_derecho
        self.clientesVista = None

    def mostrarClientes(self):
        # 1. Limpiar el contenedor cada vez que se carga una vista nueva
        for widget in self.contenedor.winfo_children():
            widget.destroy()

        # 2. Crear la vista pasándole el contenedor como 'master'
        self.clientesVista = ClientesView(self.contenedor, self)
        
        # 3. Mostrarla ocupando todo el espacio
        self.clientesVista.pack(fill="both", expand=True)