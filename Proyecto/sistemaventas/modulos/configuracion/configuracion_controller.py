from modulos.configuracion.configuracion_view import ConfiguracionView
from modulos.configuracion.configuracion_models import ConfiguracionModels


class ConfiguracionController:
    def __init__(self, contenedor_derecho):
        self.contenedor = contenedor_derecho
        self.configuracionVista = None
        self.configuracionModel = ConfiguracionModels()

    def mostrarConfiguracion(self):
        for widget in self.contenedor.winfo_children():
            widget.destroy()

        empresa = self.configuracionModel.getEmpresa()
        self.configuracionVista = ConfiguracionView(self.contenedor, self, empresa)
        self.configuracionVista.pack(fill="both", expand=True)

    def guardarEmpresa(self, datos_empresa):
        success = self.configuracionModel.guardarEmpresa(datos_empresa)
        if self.configuracionVista:
            self.configuracionVista.mostrar_mensaje(
                "Datos guardados correctamente." if success else "Error al guardar los datos.",
                success,
            )
        return success
