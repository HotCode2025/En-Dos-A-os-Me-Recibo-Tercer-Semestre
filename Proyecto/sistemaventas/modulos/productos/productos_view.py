import customtkinter as ctk


class ProductosView(ctk.CTkFrame):
    def __init__(self, master, controlador): # Recibe 'master' (el contenedor de la derecha)
        super().__init__(master) 
        self.controlador = controlador
        
        label = ctk.CTkLabel(self, text="Inventario de Productos", font=("Arial", 24))
        label.pack(pady=10)
        
        search_frame = ctk.CTkFrame(self, fg_color="transparent")
        search_frame.pack(fill="x", padx=20, pady=10)
     
        
        btn_add = ctk.CTkButton(search_frame, text="+ Añadir", fg_color="green")
        btn_add.pack(side="right", padx=5)

        