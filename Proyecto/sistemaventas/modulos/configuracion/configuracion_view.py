import customtkinter as ctk


class ConfiguracionView(ctk.CTkFrame):
    def __init__(self, master, controlador, empresa):
        super().__init__(master)
        self.controlador = controlador

        titulo = ctk.CTkLabel(self, text="Configuración de Empresa", font=("Arial", 24, "bold"))
        titulo.pack(pady=12)

        form_frame = ctk.CTkFrame(self, fg_color="transparent")
        form_frame.pack(fill="x", padx=24, pady=10)
        form_frame.grid_columnconfigure(1, weight=1)

        self.entry_razon = self._crear_campo(form_frame, "Razón social:", 0)
        self.entry_documento = self._crear_campo(form_frame, "DNI/CUIT:", 1)
        self.entry_direccion = self._crear_campo(form_frame, "Dirección:", 2)
        self.entry_email = self._crear_campo(form_frame, "Email:", 3)
        self.entry_telefono = self._crear_campo(form_frame, "Teléfono:", 4)

        if empresa:
            self._cargar_datos(empresa)

        btn_guardar = ctk.CTkButton(self, text="Guardar datos", width=180, command=self.guardar_configuracion)
        btn_guardar.pack(pady=18)

        self.mensaje_label = ctk.CTkLabel(self, text="", font=("Arial", 12), text_color="green")
        self.mensaje_label.pack(pady=(0, 10))

    def _crear_campo(self, container, texto, fila):
        label = ctk.CTkLabel(container, text=texto, anchor="w")
        label.grid(row=fila, column=0, sticky="w", padx=(0, 10), pady=8)

        entry = ctk.CTkEntry(container, width=400)
        entry.grid(row=fila, column=1, sticky="ew", padx=(0, 10), pady=8)
        return entry

    def _cargar_datos(self, empresa):
        self.entry_razon.delete(0, "end")
        self.entry_razon.insert(0, empresa.get("razon_social", ""))

        self.entry_direccion.delete(0, "end")
        self.entry_direccion.insert(0, empresa.get("direccion", ""))

        self.entry_email.delete(0, "end")
        self.entry_email.insert(0, empresa.get("email", ""))

        self.entry_telefono.delete(0, "end")
        self.entry_telefono.insert(0, empresa.get("telefono", ""))
        
        # documento (DNI/CUIT)
        try:
            self.entry_documento.delete(0, "end")
            self.entry_documento.insert(0, empresa.get("documento", ""))
        except Exception:
            pass

    def guardar_configuracion(self):
        datos_empresa = {
            "razon_social": self.entry_razon.get().strip(),
            "documento": self.entry_documento.get().strip(),
            "direccion": self.entry_direccion.get().strip(),
            "email": self.entry_email.get().strip(),
            "telefono": self.entry_telefono.get().strip(),
        }

        if datos_empresa["razon_social"] == "":
            self.mostrar_mensaje("La razón social es obligatoria.", False)
            return

        self.controlador.guardarEmpresa(datos_empresa)

    def mostrar_mensaje(self, texto, exito=True):
        self.mensaje_label.configure(
            text=texto,
            text_color="green" if exito else "red",
        )
