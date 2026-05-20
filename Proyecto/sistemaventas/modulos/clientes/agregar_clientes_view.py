import customtkinter as ctk


class AgregarCliente(ctk.CTkToplevel):
    def __init__(self, parent, callback_guardar):
        super().__init__(parent)
        self.title("Añadir Cliente")
        self.callback_guardar = callback_guardar

        ancho_ventana = 450
        alto_ventana = 520
        ancho_pantalla = self.winfo_screenwidth()
        alto_pantalla = self.winfo_screenheight()
        x = (ancho_pantalla // 2) - (ancho_ventana // 2)
        y = (alto_pantalla // 2) - (alto_ventana // 2)
        self.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
        self.after(100, self.lift)
        self.grab_set()

        self.main_container = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.main_container.pack(fill="both", expand=True, padx=12, pady=12)
        self.main_container.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(self.main_container, text="Datos del Cliente", font=("Arial", 18, "bold")).grid(row=0, column=0, pady=(0, 15), sticky="w")

        self.entry_nombre = self._crear_campo("Razón social:", 1)
        self.entry_documento = self._crear_campo("Documento:", 2)
        self.entry_email = self._crear_campo("Email:", 3)
        self.entry_telefono = self._crear_campo("Teléfono:", 4)
        self.entry_direccion = self._crear_campo("Dirección:", 5)

        # Observaciones: colocado después del último campo para evitar solapamientos
        ctk.CTkLabel(self.main_container, text="Observaciones:", anchor="w").grid(row=11, column=0, padx=12, pady=(10, 0), sticky="w")
        self.txt_observacion = ctk.CTkTextbox(self.main_container, height=100, corner_radius=10, border_width=2)
        self.txt_observacion.grid(row=12, column=0, padx=12, pady=5, sticky="ew")

        self.btn_guardar = ctk.CTkButton(self.main_container, text="Guardar Cliente", command=self.enviar_datos)
        self.btn_guardar.grid(row=13, column=0, pady=18, padx=12, sticky="ew")

        self.label_error = ctk.CTkLabel(self.main_container, text="", text_color="red")
        self.label_error.grid(row=14, column=0, padx=12, pady=(0, 10), sticky="w")

    def _crear_campo(self, texto, fila):
        ctk.CTkLabel(self.main_container, text=texto, anchor="w").grid(row=fila * 2 - 1, column=0, padx=12, pady=(10, 0), sticky="w")
        entry = ctk.CTkEntry(self.main_container, width=420)
        entry.grid(row=fila * 2, column=0, padx=12, pady=5, sticky="ew")
        return entry

    def enviar_datos(self):
        nombre = self.entry_nombre.get().strip()
        documento = self.entry_documento.get().strip()
        email = self.entry_email.get().strip()
        telefono = self.entry_telefono.get().strip()
        direccion = self.entry_direccion.get().strip()
        observacion = self.txt_observacion.get("1.0", "end-1c").strip()

        if nombre == "":
            self.label_error.configure(text="La razón social es obligatoria.")
            return

        cliente = {
            "razon_social": nombre,
            "documento": documento,
            "email": email,
            "telefono": telefono,
            "direccion": direccion,
            "observacion": observacion,
        }
        self.callback_guardar(cliente)
        self.destroy()
