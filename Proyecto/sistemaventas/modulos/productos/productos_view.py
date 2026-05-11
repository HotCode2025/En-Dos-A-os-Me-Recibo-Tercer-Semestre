import customtkinter as ctk


class ProductosView(ctk.CTkFrame):
    def __init__(self, master, controlador, productos):
        super().__init__(master) 
        self.controlador = controlador
        # self.productos ya no es necesario guardarlo como estado fijo si usas refresh
        
        # --- UI DE LA VISTA ---
        # Título
        ctk.CTkLabel(self, text="Inventario de Productos", font=("Arial", 24, "bold")).pack(pady=10)
        
        # Buscador y Botón Añadir
        search_frame = ctk.CTkFrame(self, fg_color="transparent")
        search_frame.pack(fill="x", padx=20, pady=10)
        
        self.entry_search = ctk.CTkEntry(search_frame, placeholder_text="Buscar producto...", width=300)
        self.entry_search.pack(side="left", padx=5)
        
        btn_add = ctk.CTkButton(search_frame, text="+ Añadir", fg_color="green", 
                                 hover_color="#006400", command=self.controlador.abrirFormularioRegistro)
        btn_add.pack(side="right", padx=5)

        # Contenedor de Tabla
        self.table_container = ctk.CTkScrollableFrame(self, fg_color="#2b2b2b", corner_radius=10)
        self.table_container.pack(fill="both", expand=True, padx=20, pady=10)
        self.table_container.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)

        # Encabezados de la tabla (Solo se crean una vez)
        headers = ["ID", "Categoría", "Código", "Descripción", "Precio", "Stock", "Obs.", "Acciones"]
        for i, header in enumerate(headers):
            lbl = ctk.CTkLabel(self.table_container, text=header, font=("Arial", 12, "bold"), text_color="gray")
            lbl.grid(row=0, column=i, padx=10, pady=5, sticky="nsew")
        
        # --- Carga Inicial de Datos, al iniciar la vista ---
        self.renderizar_tabla(productos)

    def renderizar_tabla(self, productos):
        """Limpia las filas actuales y dibuja las nuevas"""
        # 1. Limpiar filas existentes (preservando el encabezado en la fila 0)
        for widget in self.table_container.winfo_children():
            info = widget.grid_info()
            if int(info.get("row", 0)) > 0:
                widget.destroy()

        # 2. Cargar nuevos datos desde la lista de diccionarios
        for index, producto in enumerate(productos, start=1):
            self.crear_fila(index, producto)

    def crear_fila(self, num_fila, producto):
        """
        Crea una fila individual usando las llaves del diccionario 'prod'
        prod: {'id': ..., 'categoria': ..., 'codigo': ..., 'descripcion': ..., 'precio': ..., 'stock': ...}
        """
        # Se define el orden en el cual se muestran las columnas mediante un array. 
        # Todo: Me falta traer el campo obaservaciones desde la consulta. 
        columnas = ["id", "categoria", "codigo", "descripcion", "precio", "stock"]
        
        for i, columna in enumerate(columnas):
            valor = producto.get(columna, "")
            
            # Formateo especial para el precio
            if columna == "precio":
                valor = f"${valor:,.2f}"
                
            lbl = ctk.CTkLabel(self.table_container, text=str(valor))
            lbl.grid(row=num_fila, column=i, padx=10, pady=5)

            # --- Columna de Acciones (Columna 7) ---
            self.agregar_botones_accion(num_fila, producto["id"])

    def agregar_botones_accion(self, num_fila, producto_id):
        """Crea los botones de editar y eliminar para cada fila"""
        action_frame = ctk.CTkFrame(self.table_container, fg_color="transparent")
        action_frame.grid(row=num_fila, column=7, padx=5, pady=5)

        # capturamos el ID del producto para pasarle a los métodos 'producto_id=producto_id' para capturar el ID actual
        btn_edit = ctk.CTkButton(
            action_frame, text="✎", width=30, fg_color="#1f538d", 
            command=lambda producto_id=producto_id: self.controlador.editar_producto(producto_id)
        )
        btn_edit.pack(side="left", padx=2)

        btn_delete = ctk.CTkButton(
            action_frame, text="X", width=30, fg_color="#922b21", 
            command=lambda producto_id=producto_id: self.controlador.eliminar_producto(producto_id)
        )
        btn_delete.pack(side="left", padx=2)

    def refresh(self, nuevos_productos):
        """Método público para que el controlador actualice la vista"""
        self.renderizar_tabla(nuevos_productos)

        