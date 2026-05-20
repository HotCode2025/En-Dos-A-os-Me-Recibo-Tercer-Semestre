import customtkinter as ctk
class FacturacionView(ctk.CTkFrame):
     def __init__(self, master, controlador):
        super().__init__(master) 
        self.controlador = controlador
        
        # Título de la sección
        label = ctk.CTkLabel(self, text="Realizar venta", font=("Arial", 24, "bold"))
        label.pack(pady=10)