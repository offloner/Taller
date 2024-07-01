import tkinter as tk
import mysql.connector

from tkinter import messagebox

# Conectar a MySQL
def mysql_connection():
    return mysql.connector.connect(
        host="localhost",
        user="tu_usuario",
        passwd="tu_contraseña",
        database="tu_base_de_datos"
    )

# Función para solicitar préstamo
def solicitar_prestamo():
    user_id = entry_user_id.get()
    book_id = entry_book_id.get()
    conn = mysql_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM catalogo WHERE isbn = %s AND estado = 'disponible'", (book_id,))
        book = cursor.fetchone()
        if book:
            cursor.execute("UPDATE catalogo SET estado = 'prestado' WHERE id = %s", (book_id,))
            conn.commit()
            messagebox.showinfo("Éxito", "Préstamo realizado con éxito")
        else:
            messagebox.showerror("Error", "Libro no disponible o no existe")
    except Exception as e:
        messagebox.showerror("Error", f"Se produjo un error: {e}")
    finally:
        cursor.close()
        conn.close()

# Interfaz de usuario
root = tk.Tk()
root.title("Sistema de Préstamos")

tk.Label(root, text="ID del Usuario:").pack()
entry_user_id = tk.Entry(root)
entry_user_id.pack()

tk.Label(root, text="ID del Libro:").pack()
entry_book_id = tk.Entry(root)
entry_book_id.pack()

tk.Button(root, text="Solicitar Préstamo", command=solicitar_prestamo).pack()

root.mainloop()
