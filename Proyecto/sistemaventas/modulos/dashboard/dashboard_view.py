# Módulo para mostrar un resumen del negocio: total de productos, ventas realizadas, capital, etc. 
import customtkinter as ctk

class DashboardView(ctk.CTkFrame):
     def __init__(self, master, controlador):
        super().__init__(master) 
        self.controlador = controlador
        
        # Título de la sección
        label = ctk.CTkLabel(self, text="Vista Dashboard", font=("Arial", 24, "bold"))
        label.pack(pady=10)