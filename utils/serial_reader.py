import serial
import time
import sqlite3

# Diccionario global para guardar los últimos datos leídos
latest_data = {
    "ph": None,
    "tds": None,
    "temp": None,
    "dist": None
}

def read_serial_data():
    global latest_data

    try:
        ser = serial.Serial('COM3', 9600, timeout=1)
        time.sleep(2)

        # Guardamos el tiempo de la última inserción
        last_insert_time = time.time()

        while True:
            data_lines = []
            for _ in range(4):
                line = ser.readline().decode('utf-8').strip()
                if line:
                    data_lines.append(line)

            if len(data_lines) == 4:
                try:
                    latest_data["ph"] = float(data_lines[0])
                    latest_data["tds"] = float(data_lines[1])
                    latest_data["temp"] = float(data_lines[2])
                    latest_data["dist"] = float(data_lines[3])
                except (IndexError, ValueError):
                    print("Error al procesar los datos recibidos.")

            print(latest_data)

            # Verificamos si pasaron 5 minutos (300 segundos)
            current_time = time.time()
            if current_time - last_insert_time >= 20:
                save_to_db()
                last_insert_time = current_time

            time.sleep(5)

    except serial.SerialException as e:
        print(f"Error al abrir el puerto serial: {e}")

def save_to_db():
    conn = sqlite3.connect('hydrobyte.sqlite')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO sensor_readings (sensor_id, value) VALUES (1, ?)", (latest_data["ph"],))
    cursor.execute("INSERT INTO sensor_readings (sensor_id, value) VALUES (2, ?)", (latest_data["tds"],))
    cursor.execute("INSERT INTO sensor_readings (sensor_id, value) VALUES (3, ?)", (latest_data["temp"],))
    cursor.execute("INSERT INTO sensor_readings (sensor_id, value) VALUES (4, ?)", (latest_data["dist"],))

    conn.commit()
    conn.close()
    print("✅ Datos guardados en la base de datos.")