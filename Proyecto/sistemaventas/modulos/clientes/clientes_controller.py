from modulos.clientes.clientes_view import ClientesView
from modulos.clientes.clientes_models import ClientesModels
from modulos.clientes.agregar_clientes_view import AgregarCliente

class ClientesController: 
    def __init__(self, contenedor_derecho):
        # Guardamos la referencia de dónde se va a mostrar
        self.contenedor = contenedor_derecho
        self.clientesVista = None
        self.clientesModel = ClientesModels()

    def mostrarClientes(self):
        # 1. Limpiar el contenedor cada vez que se carga una vista nueva
        for widget in self.contenedor.winfo_children():
            widget.destroy()

        clientes = self.clientesModel.getClientes()

        # 2. Crear la vista pasándole el contenedor como 'master'
        self.clientesVista = ClientesView(self.contenedor, self, clientes)
        
        # 3. Mostrarla ocupando todo el espacio
        self.clientesVista.pack(fill="both", expand=True)

    def abrirFormularioRegistro(self):
        self.ventana_formulario = AgregarCliente(self.contenedor.winfo_toplevel(), self.guardarNuevoCliente)

    def guardarNuevoCliente(self, cliente):
        if self.clientesModel.inserterCliente(cliente):
            self.mostrarClientes()

    def editar_cliente(self, cliente_id):
        print(f"Editar cliente {cliente_id} aún no implementado")

    def eliminar_cliente(self, cliente_id):
        print(f"Eliminar cliente {cliente_id} aún no implementado")

    def buscarClientes(self, texto):
        texto = texto.strip()
        if texto == "":
            clientes = self.clientesModel.getClientes()
        else:
            clientes = self.clientesModel.buscarClientes(texto)

        if self.clientesVista:
            self.clientesVista.refresh(clientes)
