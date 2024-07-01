from functions.conexion import *

class CPrestamos:

    @staticmethod
    def ingresarPrestamos(rut, isbn, dias, estado):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "INSERT INTO prestamos VALUES (NULL, %s, %s, %s, %s);"
            valores = (rut, isbn, dias, estado)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "registro ingresado")
        except mysql.connector.Error as error:
            print("Error al ingreso de datos: {}".format(error))
        finally:
            if cone.is_connected():
                cursor.close()
                cone.close()

    @staticmethod
    def mostrarPrestamos():
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            cursor.execute("SELECT * FROM prestamos")
            miResultado = cursor.fetchall()
            return miResultado
        except mysql.connector.Error as error:
            print("Error de mostrar datos: {}".format(error))
        finally:
            if cone.is_connected():
                cursor.close()
                cone.close()

    @staticmethod
    def modificarPrestamo(rut, isbn, dias, estado):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = """
            UPDATE prestamos
            SET isbn = %s, dias = %s, estado = %s
            WHERE rut = %s;
            """
            valores = (isbn, dias, estado, rut)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "registro(s) actualizado(s)")
        except mysql.connector.Error as err:
            print("Error al actualizar datos: {}".format(err))
        finally:
            if cone.is_connected():
                cursor.close()
                cone.close()
                print("Conexión cerrada")

    @staticmethod
    def eliminarPrestamo(rut):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "DELETE FROM prestamos WHERE rut = %s"
            valores = (rut,)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "registro(s) eliminado(s)")
        except mysql.connector.Error as err:
            print("Error al eliminar datos: {}".format(err))
        finally:
            if cone.is_connected():
                cursor.close()
                cone.close()
                print("Conexión cerrada")
