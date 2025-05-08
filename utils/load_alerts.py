import sqlite3

def load_alerts():
    conn = sqlite3.connect('hydrobyte.sqlite')
    cursor = conn.cursor()
    # Ejemplo de datos de prueba
    alerts = []
    # Ejecutamos la consulta
    cursor.execute("SELECT id, sensor_id, message, timestamp FROM alerts ORDER BY timestamp DESC")

    # Obtenemos los resultados en la forma que necesitas
    alerts = cursor.fetchall()

    # Cerramos la conexión
    conn.close()
    return alerts