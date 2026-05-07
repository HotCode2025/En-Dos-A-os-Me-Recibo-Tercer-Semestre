from modulos.productos.productos_view import ProductosView
from .agregar_productos_view import agregarProducto
from .productos_models import ProductosModels

class ProductosController:
    def __init__(self, contenedor_derecho):
        # Guardamos la referencia de dónde se va a mostrar
        self.contenedor = contenedor_derecho
        self.productosVista = None
        self.productosModels = ProductosModels()

    def mostrarProductos(self):
        # 1. Limpiar el contenedor cada vez que se carga una vista nueva
        for widget in self.contenedor.winfo_children():
            widget.destroy()

        # 2. Crear la vista pasándole el contenedor como 'master'
        self.productosVista = ProductosView(self.contenedor, self)
        
        # 3. Mostrarla ocupando todo el espacio
        self.productosVista.pack(fill="both", expand=True)

    # 
    def abrir_formulario_registro(self):
        listaCategoria = self.productosModels.getCategorias() 
        
        # Creamos la ventana emergente y le pasamos el método que guardará los datos
        self.ventana_formulario = agregarProducto(self.contenedor.winfo_toplevel(), self.guardar_nuevo_producto, listaCategoria)

    # 
    def guardar_nuevo_producto(self, producto):
        print(f"Guardando en BD: {producto['descripcion']} - {producto['uuid']}") 
        # Guardamos los datos en la DB, para ello debemos llamar el método del models. 
        self.productosModels.inserterProducto(producto)
        # self.mostrarProductos() # Refrescamos la tabla
        
    # 