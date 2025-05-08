import sqlite3

DB_PATH = "hydrobyte.sqlite"


def enviarAlertaPH(v):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Insertar la alerta en la tabla
    cursor.execute('''
        INSERT INTO alerts (sensor_id, message) VALUES (?, ?)
    ''', (1, "El pH está fuera de rango: " + str(v)))

    # Guardar los cambios y cerrar la conexión
    conn.commit()
    conn.close()
    

def enviarAlertaBajoTDS(v):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Insertar la alerta en la tabla
    cursor.execute('''
        INSERT INTO alerts (sensor_id, message) VALUES (?, ?)
    ''', (2, "Los nutrientes estan bajos: " + str(v)))

    # Guardar los cambios y cerrar la conexión
    conn.commit()
    conn.close()

def enviarAlertaAltoTDS(v):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Insertar la alerta en la tabla
    cursor.execute('''
        INSERT INTO alerts (sensor_id, message) VALUES (?, ?)
    ''', (2, "Los nutrientes estan altos: " + str(v)))

    # Guardar los cambios y cerrar la conexión
    conn.commit()
    conn.close()

def enviarAlertaBajaTemp(v):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # Insertar la alerta en la tabla
    cursor.execute('''
        INSERT INTO alerts (sensor_id, message) VALUES (?, ?)
    ''', (3, "La temperatura es muy baja: " + str(v)))

    # Guardar los cambios y cerrar la conexión
    conn.commit()
    conn.close()

def enviarAlertaAltaTemp(v):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # Insertar la alerta en la tabla
    cursor.execute('''
        INSERT INTO alerts (sensor_id, message) VALUES (?, ?)
    ''', (3, "La temperatura es muy alta: " + str(v)))

    # Guardar los cambios y cerrar la conexión
    conn.commit()
    conn.close()

def enviarAlertaBajaDist(v):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # Insertar la alerta en la tabla
    cursor.execute('''
        INSERT INTO alerts (sensor_id, message) VALUES (?, ?)
    ''', (4, "El nivel de agua es muy alto: " + str(v)))

    # Guardar los cambios y cerrar la conexión
    conn.commit()
    conn.close()

def enviarAlertaAltaDist(v):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # Insertar la alerta en la tabla
    cursor.execute('''
        INSERT INTO alerts (sensor_id, message) VALUES (?, ?)
    ''', (4, "El nivel de agua es muy bajo: " + str(v)))

    # Guardar los cambios y cerrar la conexión
    conn.commit()
    conn.close()
    
    