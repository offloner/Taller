from functions.conexion import *

class CClientes:

    global clave
    clave = ''

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
          

    def ingresarClientes(rut, nombre, apellido, telefono, correo, direccion, sexo,clave):

        

        try:


            cone=CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "INSERT INTO usuarios (rut, nombre, apellido, telefono, correo, direccion, sexo, clave) VALUES ('{0}','{1}','{2}',{3},'{4}','{5}','{6}','{7}')".format(
            rut, nombre, apellido, telefono, correo, direccion, sexo, clave
            )
            #La variable valores tiene que ser una tupla
            #Como minima expresion es: (valor,)la coma hace que sea una tupla
            #Las tuplas son listas inmutables, eso quiere decir que no se pueden modificar
            cursor.execute(sql)
            cone.commit()
            print(cursor.rowcount, "Registro ingresado")
            cone.close()



        except mysql.connector.Error as error:
                  print("Error de ingreso de datos {}".format(error))

    def modificarClientes(idUsuario, nombre, apellido, telefono, correo, direccion, sexo, clave):

        try:
            cone=CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "UPDATE usuarios SET usuarios.nombre = %s, usuarios.apellido = %s, usuarios.telefono = %s, usuarios.correo = %s, usuarios.direccion = %s, usuarios.sexo = %s WHERE usuarios.rut = %s;"
            valores = (nombre, apellido, telefono, correo, direccion, sexo, idUsuario)
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



