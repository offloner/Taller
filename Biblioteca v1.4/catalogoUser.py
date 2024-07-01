import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from functions.conexion import *
from functions.CRUDcatalogo import *

class CatalogoLibros:
    global tree2
    tree2 = None

def Catalogo():
    global tree2

    def copiar_isbn():
        try:
            item_seleccionado = tree2.focus()
            if item_seleccionado:
                values = tree2.item(item_seleccionado)['values']
                isbn = values[0]  # Asumiendo que el ISBN es la primera columna
                interfazCatalogo.clipboard_clear()
                interfazCatalogo.clipboard_append(isbn)
                messagebox.showinfo("Información", f"ISBN copiado: {isbn}")
            else:
                messagebox.showwarning("Advertencia", "Por favor, seleccione un libro para copiar el ISBN.")
        except Exception as error:
            messagebox.showerror("Error", f"Error al copiar el ISBN: {error}")

    try:
        interfazCatalogo = Tk()
        interfazCatalogo.geometry("1280x450")
        interfazCatalogo.title("Catalogo de libros")
        interfazCatalogo.iconbitmap('./images/icon.ico')

        # Botones en la parte superior
        copy_button = Button(interfazCatalogo, text="Copiar ISBN", command=copiar_isbn)
        copy_button.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        close_button = Button(interfazCatalogo, text="Cerrar", command=interfazCatalogo.destroy)
        close_button.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        catalogo_frame = ttk.LabelFrame(interfazCatalogo, text="Información del Catálogo", padding=(20, 10))
        catalogo_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        tree2 = ttk.Treeview(catalogo_frame, columns=("isbn", "Nombre", "Autor", "Genero", "Editorial", "Año de publicación"), show='headings', height=18)

        tree2.column("# 1", anchor=CENTER)
        tree2.heading("# 1", text="ISBN")

        tree2.column("# 2", anchor=CENTER)
        tree2.heading("# 2", text="Nombre")

        tree2.column("# 3", anchor=CENTER)
        tree2.heading("# 3", text="Autor")

        tree2.column("# 4", anchor=CENTER)
        tree2.heading("# 4", text="Genero")

        tree2.column("# 5", anchor=CENTER)
        tree2.heading("# 5", text="Editorial")

        tree2.column("# 6", anchor=CENTER)
        tree2.heading("# 6", text="Año de publicación")

        # Agregar datos a la tabla
        for row in CCatalogo.mostrarCatalogo():
            tree2.insert("", "end", values=row)

        tree2.pack(fill=BOTH, expand=1)

        # Asegurar que el treeview se expanda para llenar el espacio disponible
        interfazCatalogo.grid_rowconfigure(1, weight=1)
        interfazCatalogo.grid_columnconfigure(0, weight=1)
        interfazCatalogo.grid_columnconfigure(1, weight=1)

        interfazCatalogo.mainloop()

    except ValueError as error:
        print("Error al ingresar los datos, error: {}".format(error))

if __name__ == "__main__":
    Catalogo()
