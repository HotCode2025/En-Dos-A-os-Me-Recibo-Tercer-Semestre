from modulos.dashboard.dashboard_view import DashboardView

class DashboardController:

    def __init__(self, contenedor_derecho):
        # Guardamos la referencia de dónde se va a mostrar
        self.contenedor = contenedor_derecho
        self.dashboardVista = None

    def mostrarDashboard(self):
        # 1. Limpiar el contenedor cada vez que se carga una vista nueva
        for widget in self.contenedor.winfo_children():
            widget.destroy()

        # 2. Crear la vista pasándole el contenedor como 'master'
        self.dashboardVista = DashboardView(self.contenedor, self)
        
        # 3. Mostrarla ocupando todo el espacio
        self.dashboardVista.pack(fill="both", expand=True)