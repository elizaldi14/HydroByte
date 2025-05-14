import serial  # type: ignore
import time
import sqlite3
import threading
from PySide6.QtCore import QObject, Signal

# Últimos datos leídos
latest_data = {
    "ph": None,
    "tds": None,
    "temp": None,
    "dist": None
}

# Clase para controlar la bomba
class PumpSerial(QObject):
    status_changed = Signal(str)

    def __init__(self, serial_conn):
        super().__init__()
        self.serial_conn = serial_conn
        if self.serial_conn and self.serial_conn.is_open:
            self.status_changed.emit(f"✅ Conectado a {self.serial_conn.port}")
        else:
            self.status_changed.emit(f"❌ Puerto no disponible.")

    def write(self, data: bytes) -> bool:
        if self.serial_conn and self.serial_conn.is_open:
            try:
                self.serial_conn.write(data)
                return True
            except (serial.SerialException, OSError) as e:
                print(f"Error al enviar datos: {e}")
                self.serial_conn = None
        return False

    def close(self):
        if self.serial_conn and self.serial_conn.is_open:
            self.serial_conn.close()

# Función para guardar en base de datos
def save_to_db():
    try:
        conn = sqlite3.connect('hydrobyte.sqlite')
        cursor = conn.cursor()

        cursor.execute("INSERT INTO sensor_readings (sensor_id, value) VALUES (1, ?)", (latest_data["ph"],))
        cursor.execute("INSERT INTO sensor_readings (sensor_id, value) VALUES (2, ?)", (latest_data["tds"],))
        cursor.execute("INSERT INTO sensor_readings (sensor_id, value) VALUES (3, ?)", (latest_data["temp"],))
        cursor.execute("INSERT INTO sensor_readings (sensor_id, value) VALUES (4, ?)", (latest_data["dist"],))

        conn.commit()
        print("✅ Datos guardados.")
    except sqlite3.Error as e:
        print(f"Error al guardar: {e}")
    finally:
        conn.close()

# Función de lectura continua
def read_serial_data(shared_serial):
    global latest_data

    try:
        time.sleep(2)
        last_insert_time = time.time()
        def es_float(valor):
            try:
                float(valor)
                return True
            except ValueError:
                return False

        while True:
            data_lines = []
            for _ in range(4):
                try:
                    line = shared_serial.readline().decode('utf-8').strip()
                    if line:
                        data_lines.append(line)
                except UnicodeDecodeError:
                    print("Error de decodificación.")
                    continue

            print("Líneas recibidas:", data_lines)

            if len(data_lines) == 4 and all(es_float(linea) for linea in data_lines):
                latest_data["ph"] = float(data_lines[0])
                latest_data["tds"] = float(data_lines[1])
                latest_data["temp"] = float(data_lines[2])
                latest_data["dist"] = float(data_lines[3])
                print(latest_data)
            else:
                print("Datos inválidos, se descartaron:", data_lines)


            if time.time() - last_insert_time >= 20:
                save_to_db()
                last_insert_time = time.time()


    except serial.SerialException as e:
        print(f"Error en lectura serial: {e}")