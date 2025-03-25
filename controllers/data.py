from controllers.conexion import ConexionDB

db = ConexionDB()

def ph_data():
    con = db.conectar()
    if not con:
        return None  # Evitar errores si la conexión falla

    cursor = con.cursor()

    cursor.execute("SELECT value FROM sensor_readings WHERE sensor_id = 1 ORDER BY id DESC LIMIT 1 ")
    ph_value = cursor.fetchone()

    db.cerrar(con)  # Pasar la conexión para cerrarla

    return ph_value[0] 
