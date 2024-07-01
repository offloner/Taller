import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from functions.CRUDprestamos import CPrestamos

class PrestamosApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1200x400')
        self.root.title('Solicitar Prestamo')

        self.root.iconbitmap('./images/icon.ico')


        self.create_widgets()

    def create_widgets(self):
        groupbox = ttk.LabelFrame(self.root, text='Asignacion prestamo', padding=(10, 5))
        groupbox.grid(row=0, column=0, padx=10, pady=10)

        ttk.Label(groupbox, text='RUT Cliente: ', width=12, font=('arial', 12)).grid(row=0, column=0)
        self.textBoxRut = ttk.Entry(groupbox)
        self.textBoxRut.grid(row=0, column=1)

        ttk.Label(groupbox, text='ISBN Libro: ', width=12, font=('arial', 12)).grid(row=1, column=0)
        self.textBoxIsbn = ttk.Entry(groupbox)
        self.textBoxIsbn.grid(row=1, column=1)

        ttk.Label(groupbox, text='Dias de uso: ', width=12, font=('arial', 12)).grid(row=2, column=0)
        self.textBoxDias = ttk.Entry(groupbox)
        self.textBoxDias.grid(row=2, column=1)

        ttk.Button(groupbox, text='Guardar', width=10, command=self.guardar_registros).grid(row=3, column=0)
        ttk.Button(groupbox, text='Cerrar', command=self.root.destroy).grid(row=3, column=1)

        catalogo_frame = ttk.LabelFrame(self.root, text="Información Prestamos", padding=(20, 10))
        catalogo_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        self.tree3 = ttk.Treeview(catalogo_frame, columns=("ID", "RUT", "ISBN", "Dias de uso", "Estado"), show='headings', height=2)
        self.tree3.grid(row=0, column=0, sticky="nsew")
        for col in self.tree3["columns"]:
            self.tree3.heading(col, text=col)
            self.tree3.column(col, anchor='center')

    def guardar_registros(self):
        try:
            rut = self.textBoxRut.get()
            isbn = self.textBoxIsbn.get()
            dias = self.textBoxDias.get()
            estado = "Solicitado"

            CPrestamos.ingresarPrestamos(rut, isbn, dias, estado)
            messagebox.showinfo("Información", "Los datos fueron guardados")
            self.limpiar_campos()
            self.mostrar_ultimo_prestamo(rut)
        except Exception as error:
            messagebox.showerror("Error", f"Error al ingresar los datos: {error}")

    def mostrar_ultimo_prestamo(self, rut):
        try:
            for row in self.tree3.get_children():
                self.tree3.delete(row)

            prestamos = CPrestamos.mostrarPrestamos()
            ultimo_prestamo = next((p for p in prestamos if p[1] == rut), None)
            if ultimo_prestamo:
                self.tree3.insert("", "end", values=ultimo_prestamo)
        except Exception as error:
            messagebox.showerror("Error", f"Error al actualizar la tabla: {error}")

    def seleccionar_registro(self, event):
        try:
            item_seleccionado = self.tree3.focus()
            if item_seleccionado:
                values = self.tree3.item(item_seleccionado)['values']
                self.textBoxRut.delete(0, tk.END)
                self.textBoxRut.insert(0, values[1])
                self.textBoxIsbn.delete(0, tk.END)
                self.textBoxIsbn.insert(0, values[2])
                self.textBoxDias.delete(0, tk.END)
                self.textBoxDias.insert(0, values[3])
        except Exception as error:
            messagebox.showerror("Error", f"Error al seleccionar el registro: {error}")

    def limpiar_campos(self):
        self.textBoxRut.delete(0, tk.END)
        self.textBoxIsbn.delete(0, tk.END)
        self.textBoxDias.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = PrestamosApp(root)
    root.mainloop()
