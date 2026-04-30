import customtkinter as ctk


class ProductosView(ctk.CTkFrame):
    def __init__(self, master, controlador): # Recibe 'master' (el contenedor de la derecha)
        super().__init__(master) 
        self.controlador = controlador
        
        # Título
        label = ctk.CTkLabel(self, text="Inventario de Productos", font=("Arial", 24, "bold"))
        label.pack(pady=10)
        
        # --- Buscador y Botón Añadir ---
        search_frame = ctk.CTkFrame(self, fg_color="transparent")
        search_frame.pack(fill="x", padx=20, pady=10)
        
        self.entry_search = ctk.CTkEntry(search_frame, placeholder_text="Buscar producto...", width=300)
        self.entry_search.pack(side="left", padx=5)
        
        btn_add = ctk.CTkButton(search_frame, text="+ Añadir", fg_color="green", hover_color="#006400")
        btn_add.pack(side="right", padx=5)

        # --- TABLA DE PRODUCTOS ---
        # Contenedor para la tabla con scroll
        self.table_container = ctk.CTkScrollableFrame(self, fg_color="#2b2b2b", corner_radius=10)
        self.table_container.pack(fill="both", expand=True, padx=20, pady=10)

        # Encabezados
        self.headers = ["ID", "Categoría", "Código", "Descripción", "Precio", "Stock", "Obs.", "Acciones"]
        for i, header in enumerate(self.headers):
            lbl = ctk.CTkLabel(self.table_container, text=header, font=("Arial", 12, "bold"), text_color="gray")
            lbl.grid(row=0, column=i, padx=10, pady=5, sticky="nsew")

        # Configurar anchos de columnas
        self.table_container.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)

        # Ejemplo de cómo cargar una fila (esto después lo harás con un bucle)
        self.agregar_fila_ejemplo(1)

    def agregar_fila_ejemplo(self, num_fila):
        # Datos de ejemplo
        datos = ["1", "Bebidas", "BEB-001", "Coca Cola 1.5L", "$1500", "50", "Fría", ""]
        
        for i, dato in enumerate(datos[:-1]): # Excluimos la última columna de acciones
            lbl = ctk.CTkLabel(self.table_container, text=dato)
            lbl.grid(row=num_fila, column=i, padx=10, pady=5)

        # Columna de Acciones (Botones)
        action_frame = ctk.CTkFrame(self.table_container, fg_color="transparent")
        action_frame.grid(row=num_fila, column=7, padx=5, pady=5)

        btn_edit = ctk.CTkButton(action_frame, text="✎", width=30, fg_color="#1f538d", hover_color="#14375e")
        btn_edit.pack(side="left", padx=2)

        btn_delete = ctk.CTkButton(action_frame, text="X", width=30, fg_color="#922b21", hover_color="#641e16")
        btn_delete.pack(side="left", padx=2)

        