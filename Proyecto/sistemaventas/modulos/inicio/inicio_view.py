import customtkinter as ctk

# Configuración estética global
ctk.set_appearance_mode("dark")  # Modos: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Temas: "blue" (standard), "green", "dark-blue"
ctk.set_widget_scaling(1.2)  # 1.5 es 50% más grande
# ctk.set_window_scaling(1.5)  # Escala la ventana también


class Inicio(ctk.CTk):
     def __init__(self, controlador):
        super().__init__()
        self.controlador = controlador
        self.title("Sistema de Ventas v 1.0 - En dos años me recibo" )
        self.geometry("1100x600")
        
        # Configurar el layout de la cuadrícula (1 fila, 2 columnas)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- PANEL LATERAL (SIDEBAR) ---
        # --- PANEL LATERAL (SIDEBAR) ---
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        # Corregido: 'column=0' con signo igual, no dos puntos
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew") 
        self.sidebar_frame.grid_rowconfigure(6, weight=1) # Espaciador para empujar botones abajo si quieres
        

        # Botones de navegación
        self.btn_inicio = ctk.CTkButton(self.sidebar_frame, text="Dashboard", command=self.controlador.mostrarDashboard)
        self.btn_inicio.grid(row=1, column=0, padx=20, pady=10)

        self.btn_productos = ctk.CTkButton(self.sidebar_frame, text="Productos", command=self.controlador.mostrarProductos)
        self.btn_productos.grid(row=2, column=0, padx=20, pady=10)

        self.btn_clientes = ctk.CTkButton(self.sidebar_frame, text="Clientes", command=self.controlador.mostrarClientes)
        self.btn_clientes.grid(row=3, column=0, padx=20, pady=10)

        self.btn_configuracion = ctk.CTkButton(self.sidebar_frame, text="Configuración", command=self.controlador.mostrarConfiguracion)
        self.btn_configuracion.grid(row=4, column=0, padx=20, pady=10)

        self.btn_ventas = ctk.CTkButton(self.sidebar_frame, text="Nueva Venta", command=self.controlador.mostrarFacturacion)
        self.btn_ventas.grid(row=5, column=0, padx=20, pady=10)

        # --- ÁREA DE CONTENIDO PRINCIPAL ---
        self.main_view = ctk.CTkFrame(self, corner_radius=10, fg_color="transparent")
        self.main_view.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        self.main_view.grid_columnconfigure(0, weight=1)
        self.main_view.grid_rowconfigure(0, weight=1)
        
      
       