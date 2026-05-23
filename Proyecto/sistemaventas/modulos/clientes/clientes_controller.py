from modulos.clientes.clientes_view import ClientesView
from modulos.clientes.clientes_models import ClientesModels
from modulos.clientes.agregar_clientes_view import AgregarCliente
from tkinter import messagebox

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
        clientes = self.clientesModel.getClientes()

        cliente = next((c for c in clientes if c["id"] == cliente_id), None)

        if cliente:
            self.ventana_formulario = AgregarCliente(
                self.contenedor.winfo_toplevel(),
                lambda datos: self._guardar_edicion(cliente_id, datos),
                cliente
            )

    def _guardar_edicion(self, cliente_id, datos):
        if self.clientesModel.actualizarCliente(cliente_id, datos):
            self.mostrarClientes()


    def eliminar_cliente(self, cliente_id):
        confirm = messagebox.askyesno("Confirmar", f"¿Eliminar cliente {cliente_id}?")

        if confirm:
            if self.clientesModel.eliminarCliente(cliente_id):
                messagebox.showinfo("Éxito", "Cliente eliminado correctamente")
                self.mostrarClientes()

    def buscarClientes(self, texto):
        texto = texto.strip()
        if texto == "":
            clientes = self.clientesModel.getClientes()
        else:
            clientes = self.clientesModel.buscarClientes(texto)

        if self.clientesVista:
            self.clientesVista.refresh(clientes)
