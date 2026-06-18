import customtkinter as ctk

class agregarProducto(ctk.CTkToplevel):
    def __init__(self, parent, callback_guardar, categorias, producto_edicion=None):
        super().__init__(parent)
        self.producto_edicion = producto_edicion
        self.title("Añadir Producto" if not producto_edicion else "Editar Producto")
        self.callback_guardar = callback_guardar # Función para devolver los datos
        self.categorias = categorias
        print("categorias", self.categorias)
      

        # centrar la venta del formulario. 
         # 1. Definir tamaño de la ventana
        ancho_ventana = 400
        alto_ventana = 500
        
        # 2. Obtener dimensiones de la pantalla
        # (O podrías usar parent.winfo_width() si querés centrarla respecto a la principal)
        ancho_pantalla = self.winfo_screenwidth()
        alto_pantalla = self.winfo_screenheight()

        # 3. Calcular coordenadas X e Y
        x = (ancho_pantalla // 2) - (ancho_ventana // 2)
        y = (alto_pantalla // 2) - (alto_ventana // 2)

        # 4. Aplicar la geometría: "ancho x alto + x + y"
        self.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
        
        # Evitar que se oculte detrás de la principal
        self.after(100, self.lift) 
        
        # Hacer que la ventana sea modal (opcional)
        self.grab_set() 
        
        # Habilitamos el scroll vertical de los componentes. 
        # 1. Crear el Frame con Scroll que ocupa toda la ventana
        # fg_color="transparent" para que se vea igual que el fondo de la ventana
        self.main_container = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.main_container.pack(fill="both", expand=True, padx=5, pady=5)
        # IMPORTANTE: Configura la columna para que se expanda
        # Configuramos la columna del SCROLLABLE FRAME para que se expanda
        self.main_container.grid_columnconfigure(0, weight=1)

        # Descripción producto
        self.labelDescripcion = ctk.CTkLabel(self.main_container, text="Descripción del Producto:", anchor="w")
        self.labelDescripcion.grid(row=0, column=0, padx=20, pady=(20, 0), sticky="ew")
        
        self.entryDescripcion = ctk.CTkEntry(self.main_container, placeholder_text="Ej: Teclado Mecánico")
        # sticky="ew" hace que se estire a los bordes, padx da el margen
        self.entryDescripcion.grid(row=1, column=0, padx=20, pady=5, sticky="ew")
        
        # Código del producto
        self.labelCodigo = ctk.CTkLabel(self.main_container, text="Código del Producto:", anchor="w")
        self.labelCodigo.grid(row=2, column=0, padx=20, pady=(20, 0), sticky="ew")
        
        self.entryCodigo = ctk.CTkEntry(self.main_container, placeholder_text="Ej: 25498879")
        self.entryCodigo.grid(row=3, column=0, padx=20, pady=5, sticky="ew")
        
        # Categorías. 
        # Guardamos las categorías y creamos una lista solo con los nombres para el combo
        self.mapaCategorias = {}

        for cat in self.categorias:
            # Caso 1: diccionario
            if isinstance(cat, dict):
                self.mapaCategorias[cat["descripcion"]] = cat["id"]

            # Caso 2: tupla o lista (id, descripcion)
            elif isinstance(cat, (tuple, list)) and len(cat) >= 2:
                self.mapaCategorias[cat[1]] = cat[0]
        descripcionCategorias = list(self.mapaCategorias.keys())

        # UI - Categoría
        self.label_cat = ctk.CTkLabel(self.main_container, text="Categoría:", anchor="w")
        self.label_cat.grid(row=4, column=0, padx=20, pady=(20, 0), sticky="ew")

        self.selector_cat = ctk.CTkOptionMenu(self.main_container, values=descripcionCategorias)
        self.selector_cat.grid(row=5, column=0, padx=20, pady=5, sticky="ew")
        
        # Precio
        self.label_precio = ctk.CTkLabel(self.main_container, text="Precio:", anchor="w")
        self.label_precio.grid(row=6, column=0, padx=20, pady=(10, 0), sticky="ew")
        
        self.entry_precio = ctk.CTkEntry(self.main_container, placeholder_text="0.00")
        self.entry_precio.grid(row=7, column=0, padx=20, pady=5, sticky="ew")
        
        # Stock
        self.labelStock = ctk.CTkLabel(self.main_container, text="Stock:", anchor="w")
        self.labelStock.grid(row=8, column=0, padx=20, pady=(10, 0), sticky="ew")
        
        self.entryStock = ctk.CTkEntry(self.main_container, placeholder_text="10")
        self.entryStock.grid(row=9, column=0, padx=20, pady=5, sticky="ew")
        
        # Observación
        self.labelObservacion = ctk.CTkLabel(self.main_container, text="Observaciones:", anchor="w")
        self.labelObservacion.grid(row=10, column=0, padx=20, pady=(10, 0), sticky="ew")

        # Campo de texto multilínea (AreaText)
        self.txtObservacion = ctk.CTkTextbox(self.main_container, height=100, corner_radius=10, border_width=2)
        self.txtObservacion.grid(row=11, column=0, padx=20, pady=5, sticky="ew")
        
        # Botón Guardar
        self.btn_guardar = ctk.CTkButton(self.main_container, text="Guardar Producto", command=self.enviar_datos)
        self.btn_guardar.grid(row=12, column=0, padx=20, pady=20, sticky="ew")

        # mensaje que se muestra en caso que haya un campo requerido vacio. 
        self.labelError = ctk.CTkLabel(self.main_container, text="", text_color="red")
        self.labelError.grid(row=13, column=0, pady=5) 
        
        if self.producto_edicion:
            self.entryDescripcion.insert(0, self.producto_edicion.get("descripcion", ""))
            self.entryCodigo.insert(0, self.producto_edicion.get("codigo", ""))
            self.entry_precio.insert(0, str(self.producto_edicion.get("precio", "")))
            self.entryStock.insert(0, str(self.producto_edicion.get("stock", "")))
            self.txtObservacion.insert("1.0", self.producto_edicion.get("observacion", "") or "")
            
            id_cat = self.producto_edicion.get("id_categoria")
            for cat in self.categorias:
                if cat["id"] == id_cat:
                    self.selector_cat.set(cat["descripcion"])
                    break
                
    def enviar_datos(self):
        
        # validamos los datos antes de enviar. 
        if not self.entryDescripcion.get().strip():
            self.labelError.configure(text="¡La descripción es obligatoria!")
            self.entryDescripcion.configure(border_color="red")
            return 
    
        producto = {
            "descripcion": self.entryDescripcion.get(),
            "uuid": self.entryCodigo.get(),
            "id_categoria": self.mapaCategorias.get(self.selector_cat.get()),
            "precio": float(self.entry_precio.get() or 0),
            "stock": int(self.entryStock.get() or 0),
            "observacion": self.txtObservacion.get("1.0", "end-1c")
            }
        if self.producto_edicion:
            producto["id"] = self.producto_edicion["id"]
        self.callback_guardar(producto) # Enviamos datos al controlador
        self.destroy() # Cerramos la ventana