from conexion import *


class CCatalogo:

    def mostrarCatalogo():
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            cursor.execute ("select * from catalogo")
            miResultado = cursor.fetchall()
            cone.commit()
            cone.close()
            return miResultado


        except mysql.connector.Error as error:
            print("Error de mostrar datos {}".format(error))


    def ingresarLibros(ISBN, nombre, autor, genero, editorial, año):

        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "insert into catalogo values (%s, %s, %s, %s, %s, %s);"
            #La variable valores tiene que ser una tupla
            #Como minima expresion es : (valor,) la coma hace que sea una tupla
            #las tuplas son listas inmutables, eso quiere decir que no se pueden modificar
            valores = (ISBN, nombre, autor, genero, editorial, año)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "registro ingresado")
            cone.close()


        except mysql.connector.Error as error:
            print("Error al ingreso de datos {}".format(error))
