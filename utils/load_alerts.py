import sqlite3

def load_alerts(db_path="hydrobyte.sqlite"):
    """
    Carga las alertas desde la base de datos.

    Args:
        db_path (str): Ruta a la base de datos SQLite.

    Returns:
        list: Lista de alertas como diccionarios.
    """
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, sensor_name, message, timestamp FROM alerts ORDER BY timestamp DESC")
        rows = cursor.fetchall()
        conn.close()

        alerts = [
            {"id": row[0], "sensor_name": row[1], "message": row[2], "timestamp": row[3]}
            for row in rows
        ]
        return alerts
    except sqlite3.Error as e:
        print(f"Error al cargar alertas: {e}")
        return []