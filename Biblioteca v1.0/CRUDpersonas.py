from conexion import *

class CClientes:

    def mostrarClientes():
        try:
            cone=CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            cursor.execute ("select * from usuarios;")
            miResultado = cursor.fetchall()
            cone.commit()
            cone.close()
            return miResultado


        except mysql.connector.Error as error:
                  print("Error de mostrar datos {}".format(error))
          

    def ingresarClientes(rut, nombre, apellido, telefono, correo, direccion, sexo):

        try:
            cone=CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "insert into usuarios values (%s,%s,%s,%s,%s,%s,%s);"
            #La variable valores tiene que ser una tupla
            #Como minima expresion es: (valor,)la coma hace que sea una tupla
            #Las tuplas son listas inmutables, eso quiere decir que no se pueden modificar
            valores = (rut, nombre, apellido, telefono, correo, direccion, sexo)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "Registro ingresado")
            cone.close()

        except mysql.connector.Error as error:
                  print("Error de ingreso de datos {}".format(error))

    def modificarClientes(rut, nombre, apellido, telefono, correo, direccion, sexo):

        try:
            cone=CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "UPDATE usuarios SET usuarios.nombre = %s, usuarios.apellido = %s, usuarios.telefono = %s, usuario.correo = %s, usuarios.direccion = %s, usuario.sexo = %s WHERE usuarios.rut = %s;"
            valores = (rut, nombre, apellido, telefono, correo, direccion, sexo)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "Registro actualizado")
            cone.close()



        except mysql.connector.Error as error:
                  print("Error de actualizacion de datos {}".format(error))

    def eliminarClientes(idUsuario):

        try:
            cone=CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "DELETE FROM usuarios where usuarios.rut = %s;"
            valores = (idUsuario,)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "Registro eliminado")
            cone.close()



        except mysql.connector.Error as error:
                  print("Error de eliminacion de datos {}".format(error))



