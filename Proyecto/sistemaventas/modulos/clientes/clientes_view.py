import customtkinter as ctk

class ClientesView(ctk.CTkFrame):
    def __init__(self, master, controlador, clientes):
        super().__init__(master)
        self.controlador = controlador

        ctk.CTkLabel(self, text="Gestión de Clientes", font=("Arial", 24, "bold")).pack(pady=10)

        top_frame = ctk.CTkFrame(self, fg_color="transparent")
        top_frame.pack(fill="x", padx=20, pady=10)

        self.entry_search = ctk.CTkEntry(top_frame, placeholder_text="Buscar cliente por razón social o DNI/CIUT...", width=350)
        self.entry_search.pack(side="left", padx=5)
        self.entry_search.bind("<Return>", lambda event: self._buscar())

        btn_buscar = ctk.CTkButton(top_frame, text="🔍 Buscar", width=100, command=self._buscar)
        btn_buscar.pack(side="left", padx=5)

        btn_nuevo = ctk.CTkButton(top_frame, text="+ Nuevo Cliente", fg_color="green", hover_color="#006400", command=self.controlador.abrirFormularioRegistro)
        btn_nuevo.pack(side="right", padx=5)

        self.table_container = ctk.CTkScrollableFrame(self, fg_color="#2b2b2b", corner_radius=10)
        self.table_container.pack(fill="both", expand=True, padx=20, pady=10)
        self.table_container.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), weight=1)

        self.headers = ["ID", "Razón social", "DNI/CIUT", "Email", "Teléfono", "Dirección", "Compras", "Obs.", "Acciones"]
        for i, header in enumerate(self.headers):
            lbl = ctk.CTkLabel(self.table_container, text=header, font=("Arial", 12, "bold"), text_color="gray")
            lbl.grid(row=0, column=i, padx=10, pady=5, sticky="nsew")

        self.refresh(clientes)

    def _buscar(self):
        texto = self.entry_search.get()
        self.controlador.buscarClientes(texto)

    def refresh(self, clientes):
        for widget in self.table_container.winfo_children():
            info = widget.grid_info()
            if int(info.get("row", 0)) > 0:
                widget.destroy()

        if not clientes:
            mensaje = ctk.CTkLabel(self.table_container, text="No hay clientes para mostrar.", text_color="gray")
            mensaje.grid(row=1, column=0, columnspan=9, padx=10, pady=10)
            return

        for index, cliente in enumerate(clientes, start=1):
            self._crear_fila(index, cliente)

    def _crear_fila(self, fila, cliente):
        columnas = ["id", "razon_social", "documento", "email", "telefono", "direccion", "compras", "observacion"]
        for i, clave in enumerate(columnas):
            valor = cliente.get(clave, "")
            lbl = ctk.CTkLabel(self.table_container, text=str(valor))
            lbl.grid(row=fila, column=i, padx=10, pady=5)

        action_frame = ctk.CTkFrame(self.table_container, fg_color="transparent")
        action_frame.grid(row=fila, column=8, padx=5, pady=5)

        btn_edit = ctk.CTkButton(action_frame, text="✎", width=30, fg_color="#1f538d", hover_color="#14375e", command=lambda id_cliente=cliente.get("id"): self.controlador.editar_cliente(id_cliente))
        btn_edit.pack(side="left", padx=2)

        btn_delete = ctk.CTkButton(action_frame, text="X", width=30, fg_color="#922b21", hover_color="#641e16", command=lambda id_cliente=cliente.get("id"): self.controlador.eliminar_cliente(id_cliente))
        btn_delete.pack(side="left", padx=2)
