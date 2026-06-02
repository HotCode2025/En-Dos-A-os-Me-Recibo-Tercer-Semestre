from modulos.facturacion.facturacion_view import FacturacionView
from modulos.facturacion.facturacion_models import FacturacionModels
from modulos.productos.productos_models import ProductosModels
from modulos.clientes.clientes_models import ClientesModels
from modulos.configuracion.configuracion_models import ConfiguracionModels

class FacturacionController:

    def __init__(self, contenedor_derecho):
        # Guardamos la referencia de dónde se va a mostrar
        self.contenedor = contenedor_derecho
        self.facturacionVista = None
        self.productosModel = ProductosModels()
        self.clientesModel = ClientesModels()
        self.facturacionModel = FacturacionModels()
        self.configuracionModel = ConfiguracionModels()

    def obtener_productos(self):
        return self.productosModel.getProductos()

    def obtener_clientes(self):
        return self.clientesModel.getClientes()

    def mostrarFacturacion(self):
        # 1. Limpiar el contenedor cada vez que se carga una vista nueva
        for widget in self.contenedor.winfo_children():
            widget.destroy()

        productos = self.obtener_productos()
        clientes = self.obtener_clientes()

        # 2. Crear la vista pasándole el contenedor como 'master'
        self.facturacionVista = FacturacionView(self.contenedor, self, productos, clientes)
        
        # 3. Mostrarla ocupando todo el espacio
        self.facturacionVista.pack(fill="both", expand=True)

    def guardar_venta(self, cliente_id, carrito, total, factura_tipo="A"):
        if not cliente_id:
            return False, "Debe seleccionar un cliente antes de guardar la venta."
        if not carrito:
            return False, "Debe agregar al menos un producto a la venta."

        success, id_venta, uuid_venta = self.facturacionModel.crear_venta(cliente_id, carrito, total, factura_tipo)
        if not success:
            return False, "No se pudo registrar la venta. Intente nuevamente."

        cliente = self.clientesModel.getClientePorId(cliente_id)
        empresa = self.configuracionModel.getEmpresa()
        pdf_success, pdf_result = self.facturacionModel.generar_pdf_venta(
            empresa,
            cliente,
            carrito,
            total,
            factura_tipo,
            id_venta,
        )

        if pdf_success:
            return True, f"Venta registrada correctamente (Factura {factura_tipo}). PDF generado en: {pdf_result}"

        return True, f"Venta registrada correctamente (Factura {factura_tipo}). No se pudo generar PDF: {pdf_result}"
