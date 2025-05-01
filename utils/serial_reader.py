# serial_reader.py

import serial
import time

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
        ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
        time.sleep(2)

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
            time.sleep(5)

    except serial.SerialException as e:
        print(f"Error al abrir el puerto serial: {e}")