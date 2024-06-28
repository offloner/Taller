import tkinter
from tkinter import *
from tkinter import messagebox
from conexion import *
from bibliotecario import *
from tkinter import ttk


import pymysql

def main_menu():

    global screen
    global icon

    screen = Tk()
    screen.geometry("300x350")
    screen.title("Inicio de Sesión")

    icon = PhotoImage(file = './images/icon.png')
    screen.iconphoto(False, icon)

    Label(text="Acceso al sistema", fg="black", width="300", height="3", font=("Calibri",15)).pack()
    Label(text="").pack()

    Button(text="Iniciar Sesión", height="3", width="30",command=login).pack()
    Label(text="").pack()
    Button(text="Registrar", height="3", width="30",command=register).pack()

    screen.mainloop()

def login():

    global screen1


    screen1 = Toplevel(screen)
    screen1.geometry("300x600")
    screen1.title("Inicio de sesión")
    screen1.iconphoto(False, icon)

    Label(screen1, text="Ingrese su rut y contraseña",fg="black", width="300", height="3", font=("Calibri",15)).pack()
    Label(screen1, text="")

    global l_rut_verify
    global l_pass_verify

    l_rut_verify = StringVar()
    l_pass_verify = StringVar()

    global l_rut_entry
    global l_pass_entry

    Label(screen1, text="RUT").pack()
    l_rut_entry = Entry(screen1, textvariable= l_rut_verify)
    l_rut_entry.pack()
    Label(screen1).pack()


    Label(screen1, text="Contraseña").pack() 
    l_pass_entry = Entry(screen1, textvariable= l_pass_verify, show='*')
    l_pass_entry.pack()
    Label(screen1).pack()




    Button(screen1, text="Iniciar sesión", command=validate_data).pack()

def register():

    global screen3
    screen3 = Toplevel(screen)
    screen3.geometry("300x600")
    screen3.title("Registro")
    screen3.iconphoto(False, icon)


    global r_rut_entry
    global r_name_entry
    global r_pass_entry
    global r_adress_entry
    global r_lastname_entry
    global r_mail_entry
    global r_phone_entry
    global r_sexo_entry
    global combo


    r_rut_entry = StringVar()
    r_name_entry = StringVar()
    r_pass_entry = StringVar()
    r_lastname_entry = StringVar()
    r_mail_entry = StringVar()
    r_adress_entry = StringVar()
    r_sexo_entry = StringVar()

    Label(screen3, text="Ingrese datos para su registro",fg="black", width="300", height="3", font=("Calibri",15)).pack()

    Label(screen3, text="RUT").pack()
    r_rut_entry = Entry(screen3)
    r_rut_entry.pack()

    Label(screen3, text="Nombre").pack()
    r_name_entry = Entry(screen3)
    r_name_entry.pack()

    Label(screen3, text="Apellido").pack()
    r_lastname_entry = Entry(screen3)
    r_lastname_entry.pack()

    Label(screen3, text="Telefono").pack()
    r_phone_entry = Entry(screen3)
    r_phone_entry.pack()

    Label(screen3, text="Correo").pack()
    r_mail_entry = Entry(screen3)
    r_mail_entry.pack()

    Label(screen3, text="Dirección").pack()
    r_adress_entry = Entry(screen3)
    r_adress_entry.pack()

    Label(screen3, text="Contraseña").pack()
    r_pass_entry = Entry(screen3, show='*')
    r_pass_entry.pack()

    Label(screen3, text='Sexo').pack()
    r_sexo_entry = ttk.Combobox(screen3)
    r_sexo_entry['values']=(
        'Femenino',
        'Masculino'
    )
    r_sexo_entry.pack()
    Label(screen3).pack()

    Button(screen3, text="Registrarse", command=insert_data).pack()

    
def insert_data():
    bd = pymysql.connect(
        host="b1yuhymgnump7qdljjoe-mysql.services.clever-cloud.com",
        user="uj6mkddz7d4eaxis",
        passwd="1w7I0nvVdbHlTym1JSEz",
        db="b1yuhymgnump7qdljjoe",
        port=3306
        )

    fcursor = bd.cursor()
    sql = "INSERT INTO usuarios (rut, nombre, apellido, telefono, correo, direccion, sexo, clave) VALUES ('{0}','{1}','{2}',{3},'{4}','{5}','{6}','{7}')".format(
        r_rut_entry.get(), r_name_entry.get(), r_lastname_entry.get(), r_phone_entry.get(), r_mail_entry.get(), r_adress_entry.get(), r_sexo_entry.get(), r_pass_entry.get()
        )
    

    try:
        fcursor.execute(sql)
        bd.commit()
        messagebox.showinfo(message="Registro Exitoso", title="Aviso")
    except:
        bd.rollback()
        messagebox.showinfo(message="No Registrado", title="Aviso")

def validate_data():
    bd = pymysql.connect(
        host="b1yuhymgnump7qdljjoe-mysql.services.clever-cloud.com",
        user="uj6mkddz7d4eaxis",
        passwd="1w7I0nvVdbHlTym1JSEz",
        db="b1yuhymgnump7qdljjoe",
        port=3306
        )
    
    fcursor = bd.cursor()
    fcursor.execute("SELECT clave FROM usuarios WHERE rut='"+l_rut_verify.get()+"' AND clave='"+l_pass_verify.get()+"'")

#   BIBLIOTECARIO
    if l_rut_verify.get()=="15040090-1" and l_pass_verify.get()=="Barroso@76":
        messagebox.showinfo(title="Inicio de sesion correcto", message="RUT y Contraseña correcta\nBibliotecario Identificado")
        screen1.destroy()
        screen.withdraw()
        InterfazBibliotecario()



#   ALUMNO
    elif fcursor.fetchall():
        messagebox.showinfo(title="Inicio de sesion correcto", message="Usuario y Contraseña correcta")
        screen1.destroy()
        screen.withdraw()
    #Intefaz docente

    else:
        messagebox.showinfo(title="Inicio de sesion Incorrecto", message="Usuario y Contraseña incorrecta")
    
    bd.close()


main_menu()