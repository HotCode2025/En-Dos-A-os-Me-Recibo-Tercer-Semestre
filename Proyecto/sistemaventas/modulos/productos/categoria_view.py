import customtkinter as ctk
import tkinter.messagebox as messagebox

class CategoriasView(ctk.CTkToplevel):
    def __init__(self, parent, controlador, categorias):
        super().__init__(parent)
        self.controlador = controlador
        self.categorias = categorias
        
        self.title("Gestión de Categorías")
        self.geometry("600x500")
        self.after(100, self.lift) 
        self.grab_set() 
        
        # Formulario para agregar / editar
        self.form_frame = ctk.CTkFrame(self)
        self.form_frame.pack(fill="x", padx=10, pady=10)
        
        self.categoria_edicion_id = None
        
        ctk.CTkLabel(self.form_frame, text="Descripción:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_desc = ctk.CTkEntry(self.form_frame, width=150)
        self.entry_desc.grid(row=0, column=1, padx=5, pady=5)
        
        self.btn_guardar = ctk.CTkButton(self.form_frame, text="Agregar", width=80, command=self.guardar_categoria)
        self.btn_guardar.grid(row=0, column=2, padx=10, pady=5)

        self.btn_cancelar = ctk.CTkButton(self.form_frame, text="Cancelar", width=80, fg_color="gray", command=self.limpiar_formulario)
        self.btn_cancelar.grid(row=1, column=2, padx=10, pady=5)
        self.btn_cancelar.grid_remove() # Oculto por defecto
        
        # Lista de categorías
        self.table_frame = ctk.CTkScrollableFrame(self)
        self.table_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.renderizar_lista()
        
    def renderizar_lista(self):
        for widget in self.table_frame.winfo_children():
            widget.destroy()
            
        headers = ["ID", "Descripción", "Observación", "Acciones"]
        for i, header in enumerate(headers):
            ctk.CTkLabel(self.table_frame, text=header, font=("Arial", 12, "bold")).grid(row=0, column=i, padx=10, pady=5, sticky="w")
            
        for index, cat in enumerate(self.categorias, start=1):
            ctk.CTkLabel(self.table_frame, text=str(cat.get("id"))).grid(row=index, column=0, padx=10, pady=5, sticky="w")
            ctk.CTkLabel(self.table_frame, text=cat.get("descripcion", "")).grid(row=index, column=1, padx=10, pady=5, sticky="w")
            ctk.CTkLabel(self.table_frame, text=cat.get("observacion", "")).grid(row=index, column=2, padx=10, pady=5, sticky="w")
            
            action_frame = ctk.CTkFrame(self.table_frame, fg_color="transparent")
            action_frame.grid(row=index, column=3, padx=5, pady=5)
            
            btn_edit = ctk.CTkButton(action_frame, text="✎", width=30, fg_color="#1f538d", command=lambda c=cat: self.editar_categoria(c))
            btn_edit.pack(side="left", padx=2)
            
            btn_delete = ctk.CTkButton(action_frame, text="X", width=30, fg_color="#922b21", command=lambda cid=cat["id"]: self.eliminar_categoria(cid))
            btn_delete.pack(side="left", padx=2)
            
    def editar_categoria(self, cat):
        self.categoria_edicion_id = cat["id"]
        self.entry_desc.delete(0, "end")
        self.entry_desc.insert(0, cat.get("descripcion", ""))
        self.entry_obs.delete(0, "end")
        self.entry_obs.insert(0, cat.get("observacion", "") or "")
        
        self.btn_guardar.configure(text="Actualizar")
        self.btn_cancelar.grid()
        
    def limpiar_formulario(self):
        self.categoria_edicion_id = None
        self.entry_desc.delete(0, "end")
        self.entry_obs.delete(0, "end")
        self.btn_guardar.configure(text="Agregar")
        self.btn_cancelar.grid_remove()

    def guardar_categoria(self):
        desc = self.entry_desc.get().strip()
        obs = self.entry_obs.get().strip()
        
        if not desc:
            messagebox.showwarning("Atención", "La descripción es obligatoria")
            return
            
        datos = {
            "id": self.categoria_edicion_id,
            "descripcion": desc,
            "observacion": ""
        }
        
        self.controlador.guardar_categoria(datos, self)
        
    def eliminar_categoria(self, id_categoria):
        if messagebox.askyesno("Confirmar", "¿Seguro que desea eliminar esta categoría?"):
            self.controlador.eliminar_categoria(id_categoria, self)
            
    def refresh(self, nuevas_categorias):
        self.categorias = nuevas_categorias
        self.renderizar_lista()
        self.limpiar_formulario()