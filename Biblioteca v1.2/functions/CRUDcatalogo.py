from functions.conexion import *


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


    def ingresarLibros(isbn, nombre, autor, genero, editorial, año):

        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "insert into catalogo values (%s, %s, %s, %s, %s, %s);"
            #La variable valores tiene que ser una tupla
            #Como minima expresion es : (valor,) la coma hace que sea una tupla
            #las tuplas son listas inmutables, eso quiere decir que no se pueden modificar
            valores = (isbn, nombre, autor, genero, editorial, año)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "registro ingresado")
            cone.close()


        except mysql.connector.Error as error:
            print("Error al ingreso de datos {}".format(error))

    def modificarCatalogo(nombre, autor, genero, editorial, año, isbn):
        try:
            with CConexion.ConexionBaseDeDatos() as cone:
                cursor = cone.cursor()
                cursor.execute("SET SQL_SAFE_UPDATES = 0;")
                sql = """UPDATE catalogo SET nombre = %s, autor = %s, genero = %s, editorial = %s, año = %s WHERE isbn = %s;"""
                valores = (nombre, autor, genero, editorial, año, isbn)
                cursor.execute(sql, valores)
                cone.commit()  # Asegúrate de hacer commit aquí.
                cursor.execute("SET SQL_SAFE_UPDATES = 1;")
                print(f"{cursor.rowcount} Registro Actualizado")
        except mysql.connector.Error as error:
            print(f"Error de actualización de datos: {error}")


    def eliminarClientes(idLibro):

        try:
            cone=CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "DELETE FROM catalogo where catalogo.isbn = %s;"
            valores = (idLibro,)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "Registro eliminado")
            cone.close()



        except mysql.connector.Error as error:
                  print("Error de eliminacion de datos {}".format(error))



