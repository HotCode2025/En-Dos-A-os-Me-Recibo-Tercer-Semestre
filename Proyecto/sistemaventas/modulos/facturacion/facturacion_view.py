# Este módulo procesa la transacción de la venta. Cuyas funciones son: 
# Permitir la búsqueda de producto y agregarlo a al venta. 
# Mostrar los productos añadidos a la venta, modificar cantidades, eliminar. 
# Mostrar datos como: vendedor, cliente, código de factura, saldo parcial y total de la venta. 
# Permitir el cierre de la venta. 
import customtkinter as ctk
class FacturacionView(ctk.CTkFrame):
     def __init__(self, master, controlador):
        super().__init__(master) 
        self.controlador = controlador
        
        # Título de la sección
        label = ctk.CTkLabel(self, text="Realizar venta", font=("Arial", 24, "bold"))
        label.pack(pady=10)