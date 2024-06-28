# pip install mysql-connector-python
import mysql.connector 

class CConexion:

    def ConexionBaseDeDatos():
        try:
            conexion = mysql.connector.connect(
                host = "b1yuhymgnump7qdljjoe-mysql.services.clever-cloud.com",
                user = "uj6mkddz7d4eaxis",
                password = "1w7I0nvVdbHlTym1JSEz",
                database = "b1yuhymgnump7qdljjoe",
                port="3306"
            )
            print("Conexion exitosa")

            return conexion
        
        except mysql.connector.Error as error:
            print("Error al conectarte a la base de datos {}".format(error))
            
            return conexion


