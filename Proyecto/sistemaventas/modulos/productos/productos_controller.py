import tkinter.messagebox as messagebox
from modulos.productos.productos_view import ProductosView
from .agregar_productos_view import agregarProducto
from .productos_models import ProductosModels
from .categoria_view import CategoriasView

class ProductosController:
    def __init__(self, contenedor_derecho):
        # Guardamos la referencia de dónde se va a mostrar
        self.contenedor = contenedor_derecho
        self.productosVista = None
        self.productosModels = ProductosModels()
        
    # Métodos para gestionar las Categorías
    
    def abrir_categorias(self):
        categorias = self.productosModels.getCategorias()
        CategoriasView(self.contenedor.winfo_toplevel(), self, categorias)
        
    def guardar_categoria(self, datos, vista_categoria):
        if datos.get("id"):
            exito, mensaje = self.productosModels.actualizarCategoria(datos["id"], datos["descripcion"], datos["observacion"])
        else:
            exito, mensaje = self.productosModels.insertarCategoria(datos["descripcion"], datos["observacion"])
            
        if exito:
            messagebox.showinfo("Éxito", mensaje)
            # Refrescar vista
            vista_categoria.refresh(self.productosModels.getCategorias())
        else:
            messagebox.showerror("Error", mensaje)

    def eliminar_categoria(self, id_categoria, vista_categoria):
        exito, mensaje = self.productosModels.eliminarCategoria(id_categoria)
        if exito:
            messagebox.showinfo("Éxito", mensaje)
            vista_categoria.refresh(self.productosModels.getCategorias())
        else:
            messagebox.showerror("Error", mensaje)
        
    # métodos para gestionar los productos. 
    def mostrarProductos(self):
        # 1. Limpiar el contenedor cada vez que se carga una vista nueva
        for widget in self.contenedor.winfo_children():
            widget.destroy()

        # traemos los productos del modelo
        productos = self.obtener_lista_productos()
 
        # 2. Crear la vista pasándole el contenedor como 'master'
        self.productosVista = ProductosView(self.contenedor, self, productos)
        # 3. Mostrarla ocupando todo el espacio
        self.productosVista.pack(fill="both", expand=True)

    
    def abrirFormularioRegistro(self):
        listaCategoria = self.productosModels.getCategorias() 
        
        # Creamos la ventana emergente y le pasamos el método que guardará los datos
        self.ventana_formulario = agregarProducto(self.contenedor.winfo_toplevel(), self.guardarNuevoProducto, listaCategoria)

    def editar_producto(self, producto):
        print(producto)
        print("producto a editar")
        
    def eliminar_producto(self, producto):
        print(producto)
        print("eliminar producto")
        
    
        
    # Métodos rest. 
    def guardarNuevoProducto(self, producto):
        print(f"Guardando en BD: {producto['descripcion']} - {producto['uuid']}") 
        # Guardamos los datos en la DB, para ello debemos llamar el método del models. 
        self.productosModels.inserterProducto(producto)
        # aquí se debería llamar al método para refrestar la tabla
    
    def obtener_lista_productos(self):
        """Método centralizado para obtener datos"""
        # Aquí en un futuro se puede añadir lógica extra (filtros, logs, validaciones)
        return self.productosModels.getProductos()
    
    def buscarProductos(self, texto):
        texto = texto.strip()  # saca espacios al principio y al final
        
        if texto == "":
            # Si el campo está vacío, mostrar todos
            productos = self.obtener_lista_productos()
        else:
            productos = self.productosModels.buscarProductos(texto)
        
        # Refrescar la tabla con los resultados
        if self.productosVista:
            self.productosVista.refresh(productos)
    