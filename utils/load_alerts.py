import sqlite3

def load_alerts():
    conn = sqlite3.connect('hydrobyte.sqlite')
    cursor = conn.cursor()
    # Ejemplo de datos de prueba
    alerts = []
    # Ejecutamos la consulta
    cursor.execute("""
    SELECT 
        alerts.id, 
        sensors.name AS sensor_name, 
        alerts.message, 
        alerts.timestamp
    FROM alerts
    JOIN sensors ON alerts.sensor_id = sensors.id
    ORDER BY alerts.timestamp DESC
    """)

    # Obtenemos los resultados en la forma que necesitas
    alerts = cursor.fetchall()

    # Cerramos la conexión
    conn.close()
    return alerts