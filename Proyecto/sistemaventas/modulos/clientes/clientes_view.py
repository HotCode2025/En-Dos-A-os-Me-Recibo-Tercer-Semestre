import customtkinter as ctk

class ClientesView(ctk.CTkFrame): 
    def __init__(self, master, controlador): # Recibe 'master' (el contenedor de la derecha)
        super().__init__(master) 
        self.controlador = controlador
        
        # Título de la sección
        label = ctk.CTkLabel(self, text="Gestión de Clientes", font=("Arial", 24, "bold"))
        label.pack(pady=10)
        
        # --- Buscador y Botón Nuevo Cliente ---
        top_frame = ctk.CTkFrame(self, fg_color="transparent")
        top_frame.pack(fill="x", padx=20, pady=10)
        
        self.entry_search = ctk.CTkEntry(top_frame, placeholder_text="Buscar cliente por nombre o documento...", width=350)
        self.entry_search.pack(side="left", padx=5)
        
        btn_nuevo = ctk.CTkButton(top_frame, text="+ Nuevo Cliente", fg_color="green", hover_color="#006400")
        btn_nuevo.pack(side="right", padx=5)

        # --- TABLA DE CLIENTES ---
        self.table_container = ctk.CTkScrollableFrame(self, fg_color="#2b2b2b", corner_radius=10)
        self.table_container.pack(fill="both", expand=True, padx=20, pady=10)

        # Encabezados (9 columnas incluyendo Acciones)
        self.headers = ["ID", "Nombre", "Documento", "Email", "Teléfono", "Dirección", "Compras", "Obs.", "Acciones"]
        
        for i, header in enumerate(self.headers):
            lbl = ctk.CTkLabel(self.table_container, text=header, font=("Arial", 12, "bold"), text_color="gray")
            lbl.grid(row=0, column=i, padx=10, pady=5, sticky="nsew")

        # Configuramos las columnas para que se distribuyan bien
        self.table_container.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), weight=1)

        # Ejemplo de carga de un cliente
        self.agregar_cliente_ejemplo(1)

    def agregar_cliente_ejemplo(self, num_fila):
        # Datos de prueba
        datos = ["101", "Juan Pérez", "20-35444111-9", "juan@mail.com", "11 4455-6677", "Av. Siempre Viva 123", "5", "Cliente VIP", ""]
        
        for i, dato in enumerate(datos[:-1]): # Recorremos todo menos 'Acciones'
            lbl = ctk.CTkLabel(self.table_container, text=dato, font=("Arial", 11))
            lbl.grid(row=num_fila, column=i, padx=10, pady=5)

        # Columna de Acciones
        action_frame = ctk.CTkFrame(self.table_container, fg_color="transparent")
        action_frame.grid(row=num_fila, column=8, padx=5, pady=5)

        btn_edit = ctk.CTkButton(action_frame, text="✎", width=30, fg_color="#1f538d", hover_color="#14375e")
        btn_edit.pack(side="left", padx=2)

        btn_delete = ctk.CTkButton(action_frame, text="X", width=30, fg_color="#922b21", hover_color="#641e16")
        btn_delete.pack(side="left", padx=2)