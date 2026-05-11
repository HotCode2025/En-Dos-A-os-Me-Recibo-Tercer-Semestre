import tkinter as tk
from tkinter import messagebox
import json
import os

ARCHIVO = "empresa.json"

# ===========================
# PERSISTENCIA
# ===========================
def cargar_datos():
    if not os.path.exists(ARCHIVO):
        return {
            "nombre": "",
            "direccion": "",
            "telefono": "",
            "email": "",
            "cuit": ""
        }
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_datos(datos):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

# ===========================
# INTERFAZ
# ===========================
root = tk.Tk()
root.title("Configuración de Empresa")
root.geometry("1100x650")
root.configure(bg="#1f1f1f")

# SIDEBAR
sidebar = tk.Frame(root, bg="#252525", width=220)
sidebar.pack(side="left", fill="y")

def boton(texto, activo=False):
    return tk.Button(
        sidebar,
        text=texto,
        bg="#388e3c" if activo else "#1976d2",
        fg="white",
        relief="flat",
        height=2
    )

boton("Inicio").pack(fill="x", padx=15, pady=5)
boton("Empresa", activo=True).pack(fill="x", padx=15, pady=5)
boton("Reportes").pack(fill="x", padx=15, pady=5)

# CONTENIDO
contenido = tk.Frame(root, bg="#2b2b2b")
contenido.pack(fill="both", expand=True, padx=25, pady=25)

tk.Label(
    contenido,
    text="Configuración de Empresa",
    font=("Arial", 20, "bold"),
    bg="#2b2b2b",
    fg="white"
).pack(pady=25)

form = tk.Frame(contenido, bg="#2b2b2b")
form.pack(fill="x", padx=320)

datos = cargar_datos()

def campo(etiqueta, valor):
    tk.Label(
        form,
        text=etiqueta,
        bg="#2b2b2b",
        fg="white"
    ).pack(anchor="w", pady=(10, 0))

    entry = tk.Entry(
        form,
        bg="#3c3f41",
        fg="white",
        insertbackground="white"
    )
    entry.insert(0, valor)
    entry.pack(fill="x")
    return entry

entry_nombre = campo("Nombre de la Empresa", datos["nombre"])
entry_direccion = campo("Dirección", datos["direccion"])
entry_telefono = campo("Teléfono", datos["telefono"])
entry_email = campo("Email", datos["email"])
entry_cuit = campo("CUIT / RUC", datos["cuit"])

def guardar():
    guardar_datos({
        "nombre": entry_nombre.get(),
        "direccion": entry_direccion.get(),
        "telefono": entry_telefono.get(),
        "email": entry_email.get(),
        "cuit": entry_cuit.get()
    })
    messagebox.showinfo("Empresa", "Datos guardados correctamente")

tk.Button(
    contenido,
    text="Guardar Datos",
    bg="#2e7d32",
    fg="white",
    font=("Arial", 13),
    relief="flat",
    command=guardar
).pack(pady=40)

root.mainloop()
