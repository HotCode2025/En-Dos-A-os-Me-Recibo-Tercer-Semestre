import datetime
import tkinter as tk
import tkinter.messagebox as messagebox
import tkinter.ttk as ttk
import customtkinter as ctk

class FacturacionView(ctk.CTkFrame):
    def __init__(self, master, controlador, productos, clientes):
        super().__init__(master)
        self.controlador = controlador
        self.productos = productos
        self.clientes = clientes
        self.carrito = []
        self.total_venta = 0.0
        self.producto_map = {str(p['id']): p for p in productos}
        self.cliente_map = {str(c['id']): c for c in clientes}

        fecha_texto = datetime.date.today().strftime("%d/%m/%Y")

        title_frame = ctk.CTkFrame(self, fg_color="transparent")
        title_frame.pack(fill="x", pady=(10, 20), padx=20)
        title_frame.grid_columnconfigure(0, weight=1)
        title_frame.grid_columnconfigure(1, weight=1)

        label = ctk.CTkLabel(title_frame, text="Realizar venta", font=("Arial", 26, "bold"))
        label.grid(row=0, column=0, sticky="w")

        fecha_label = ctk.CTkLabel(title_frame, text=f"Fecha: {fecha_texto}", font=("Arial", 16, "bold"))
        fecha_label.grid(row=0, column=1, sticky="e")

        form_frame = ctk.CTkFrame(self, fg_color="transparent")
        form_frame.pack(fill="x", pady=(0, 20), padx=20)

        ctk.CTkLabel(form_frame, text="Cliente:", font=("Arial", 14)).grid(row=0, column=0, sticky="w", pady=8)
        ctk.CTkLabel(form_frame, text="Tipo de factura:", font=("Arial", 14)).grid(row=1, column=0, sticky="w", pady=8)
        ctk.CTkLabel(form_frame, text="Producto:", font=("Arial", 14)).grid(row=2, column=0, sticky="w", pady=8)
        ctk.CTkLabel(form_frame, text="Cantidad:", font=("Arial", 14)).grid(row=3, column=0, sticky="w", pady=8)

        cliente_values = [f"{c['id']} - {c['razon_social']}" for c in clientes] if clientes else ["No hay clientes"]
        producto_values = [f"{p['id']} - {p['descripcion']} (${p['precio']:.2f})" for p in productos] if productos else ["No hay productos"]

        self.cliente_var = tk.StringVar(value=cliente_values[0] if clientes else "")
        self.producto_var = tk.StringVar(value=producto_values[0] if productos else "")

        self.cliente_menu = ctk.CTkOptionMenu(form_frame, variable=self.cliente_var, values=cliente_values, width=360)
        self.cliente_menu.grid(row=0, column=1, sticky="w", padx=10)

        self.factura_tipo_var = tk.StringVar(value="A")
        self.factura_tipo_menu = ctk.CTkOptionMenu(form_frame, variable=self.factura_tipo_var, values=["A", "B", "X"], width=120)
        self.factura_tipo_menu.grid(row=1, column=1, sticky="w", padx=10)

        self.producto_menu = ctk.CTkOptionMenu(form_frame, variable=self.producto_var, values=producto_values, width=360)
        self.producto_menu.grid(row=2, column=1, sticky="w", padx=10)

        self.cantidad_entry = ctk.CTkEntry(form_frame, placeholder_text="1", width=120)
        self.cantidad_entry.grid(row=3, column=1, sticky="w", padx=10)

        self.agregar_btn = ctk.CTkButton(form_frame, text="Agregar producto", command=self.agregar_producto)
        self.agregar_btn.grid(row=4, column=1, sticky="w", pady=(10, 0), padx=10)

        carrito_frame = ctk.CTkFrame(self, fg_color="transparent")
        carrito_frame.pack(fill="both", expand=True, pady=(0, 20), padx=20)

        self.tree = ttk.Treeview(carrito_frame, columns=("producto", "precio", "cantidad", "subtotal"), show="headings", height=14)
        self.tree.heading("producto", text="Producto")
        self.tree.heading("precio", text="Precio unitario")
        self.tree.heading("cantidad", text="Cantidad")
        self.tree.heading("subtotal", text="Subtotal")
        self.tree.column("producto", width=420)
        self.tree.column("precio", width=140, anchor="center")
        self.tree.column("cantidad", width=120, anchor="center")
        self.tree.column("subtotal", width=140, anchor="center")
        self.tree.pack(fill="both", expand=True, side="left")

        scrollbar = ttk.Scrollbar(carrito_frame, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=scrollbar.set)

        footer_frame = ctk.CTkFrame(self, fg_color="transparent")
        footer_frame.pack(fill="x", pady=(0, 20), padx=20)

        self.total_label = ctk.CTkLabel(footer_frame, text="Total: $0.00", font=("Arial", 18, "bold"))
        self.total_label.pack(side="left")

        self.finalizar_btn = ctk.CTkButton(footer_frame, text="Finalizar venta", command=self.finalizar_venta)
        self.finalizar_btn.pack(side="right")

        if not clientes:
            self.cliente_menu.configure(values=["No hay clientes"], state="disabled")
        if not productos:
            self.producto_menu.configure(values=["No hay productos"], state="disabled")
            self.agregar_btn.configure(state="disabled")

    def _seleccionar_cliente_id(self):
        valor = self.cliente_var.get()
        if not valor or " - " not in valor:
            return None
        return valor.split(" - ")[0]

    def _seleccionar_producto(self):
        valor = self.producto_var.get()
        if not valor or " - " not in valor:
            return None
        producto_id = valor.split(" - ")[0]
        return self.producto_map.get(producto_id)

    def agregar_producto(self):
        producto = self._seleccionar_producto()
        if not producto:
            messagebox.showerror("Error", "Debe seleccionar un producto válido.")
            return

        cantidad_texto = self.cantidad_entry.get().strip() or "1"
        if not cantidad_texto.isdigit() or int(cantidad_texto) <= 0:
            messagebox.showerror("Error", "Ingrese una cantidad válida.")
            return

        cantidad = int(cantidad_texto)
        if producto.get("stock", 0) < cantidad:
            messagebox.showerror("Error", f"Stock insuficiente. Hay {producto.get('stock', 0)} disponibles.")
            return

        subtotal = cantidad * float(producto["precio"])

        item_existente = next((item for item in self.carrito if item["id"] == producto["id"]), None)
        if item_existente:
            item_existente["cantidad"] += cantidad
            item_existente["subtotal"] = item_existente["cantidad"] * float(item_existente["precio"])
        else:
            self.carrito.append({
                "id": producto["id"],
                "descripcion": producto["descripcion"],
                "precio": producto["precio"],
                "cantidad": cantidad,
                "subtotal": subtotal,
            })

        self._actualizar_carrito()
        self.cantidad_entry.delete(0, tk.END)
        self.cantidad_entry.insert(0, "1")

    def _actualizar_carrito(self):
        self.tree.delete(*self.tree.get_children())
        self.total_venta = 0.0
        for item in self.carrito:
            self.tree.insert("", "end", values=(
                item["descripcion"],
                f"${item['precio']:.2f}",
                item["cantidad"],
                f"${item['subtotal']:.2f}"
            ))
            self.total_venta += item["subtotal"]

        self.total_label.configure(text=f"Total: ${self.total_venta:.2f}")

    def finalizar_venta(self):
        cliente_id = self._seleccionar_cliente_id()
        if not cliente_id:
            messagebox.showerror("Error", "Debe seleccionar un cliente antes de cerrar la venta.")
            return

        if not self.carrito:
            messagebox.showerror("Error", "Debe agregar productos antes de cerrar la venta.")
            return

        factura_tipo = self.factura_tipo_var.get()
        success, mensaje = self.controlador.guardar_venta(int(cliente_id), self.carrito, self.total_venta, factura_tipo)
        if success:
            messagebox.showinfo("Venta registrada", f"{mensaje} Tipo de factura: {factura_tipo}")
            self.carrito = []
            self._actualizar_carrito()
        else:
            messagebox.showerror("Error", mensaje)
