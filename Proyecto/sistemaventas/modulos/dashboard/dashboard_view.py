# Módulo para mostrar un resumen del negocio: total de productos, ventas realizadas, capital, etc. 
import customtkinter as ctk

class DashboardView(ctk.CTkFrame):
    def __init__(self, master, controlador, estadisticas):
        super().__init__(master, fg_color="transparent") 
        self.controlador = controlador
        
        # Título principal del Dashboard
        self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.header_frame.pack(fill="x", padx=20, pady=(20, 10))
        
        label_titulo = ctk.CTkLabel(
            self.header_frame, 
            text="Resumen del Negocio", 
            font=("Arial", 28, "bold")
        )
        label_titulo.pack(side="left")

        # Contenedor para las tarjetas (Cards)
        self.cards_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.cards_frame.pack(fill="x", padx=20, pady=20)
        
        # Hacemos que las columnas se expandan por igual para que las tarjetas se adapten
        self.cards_frame.grid_columnconfigure(0, weight=1)
        self.cards_frame.grid_columnconfigure(1, weight=1)
        self.cards_frame.grid_columnconfigure(2, weight=1)

        # Formatear valores. Esto se hace para valores altos y sean legibles de manera adecuada los números. 
        ventas_str = f"{estadisticas['ventas']:,}"
        clientes_str = f"{estadisticas['clientes']:,}"
        productos_str = f"{estadisticas['productos']:,}"

        # Crear tarjeta 1: Cantidad de Ventas
        self.crear_tarjeta(
            master=self.cards_frame, 
            row=0, 
            column=0, 
            titulo="Cantidad de Ventas", 
            valor=ventas_str, 
            color_borde="#2ecc71" # Verde
        )

        # Crear tarjeta 2: Total de Clientes
        self.crear_tarjeta(
            master=self.cards_frame, 
            row=0, 
            column=1, 
            titulo="Total de Clientes", 
            valor=clientes_str, 
            color_borde="#3498db" # Azul
        )

        # Crear tarjeta 3: Total Productos
        self.crear_tarjeta(
            master=self.cards_frame, 
            row=0, 
            column=2, 
            titulo="Productos en Stock", 
            valor=productos_str, 
            color_borde="#f1c40f" # Amarillo
        )

    def crear_tarjeta(self, master, row, column, titulo, valor, color_borde):
        # Frame principal de la tarjeta (fondo oscuro)
        card = ctk.CTkFrame(master, corner_radius=15, fg_color="#2b2b2b")
        card.grid(row=row, column=column, padx=15, pady=10, sticky="nsew")
        
        # Línea de color superior para darle un toque moderno
        linea_color = ctk.CTkFrame(card, height=4, fg_color=color_borde, corner_radius=0)
        linea_color.pack(fill="x", side="top", padx=10, pady=(10, 0))

        # Título de la tarjeta
        lbl_titulo = ctk.CTkLabel(
            card, 
            text=titulo, 
            font=("Arial", 16, "bold"), 
            text_color="#aaaaaa"
        )
        lbl_titulo.pack(pady=(15, 5))

        # Valor gigante en el centro
        lbl_valor = ctk.CTkLabel(
            card, 
            text=valor, 
            font=("Arial", 40, "bold"), 
            text_color="#ffffff"
        )
        lbl_valor.pack(pady=(0, 20))