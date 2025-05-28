from utils.constants import LIGHT_COLORS
from utils.serial_reader import latest_data  # Datos reales sin modificar
import random
import sqlite3
from utils.alerts import *
from app.widgets.pump_control import send_command

DB_PATH = "hydrobyte.sqlite"

statusSensor = {
    "ph": True,  # Comentado para prueba
    "tds": True,
    "temp": True,
    "dist": True
}

class DataGenerator:
    def generate_random_ph(self):
        min_ph = 5.5 * 0.8
        max_ph = 6.2 * 1.2
        return round(random.uniform(min_ph, max_ph), 1)

    def generate_random_ce(self):
        # CE en mS/cm
        min_ce = 1.2 * 0.8   # 0.96
        max_ce = 1.6 * 1.2   # 1.92
        return round(random.uniform(min_ce, max_ce), 1)

    def generate_random_temp(self):
        min_temp = 18 * 0.8
        max_temp = 22 * 1.2
        return round(random.uniform(min_temp, max_temp), 1)

    def generate_random_dist(self):
        min_dist = 40 * 0.8
        max_dist = 40 * 1.2
        return round(random.uniform(min_dist, max_dist), 1)    

    def __init__(self):
        self.generate_random_ph()
        self.realtime_data = [
            {
                "name": "pH",
                "data": [],
                "color": LIGHT_COLORS["ph_color"]
            },
            {
                "name": "EC (mS/cm)",
                "data": [],
                "color": LIGHT_COLORS["ec_color"]
            },
            {
                "name": "Temperatura (°C)",
                "data": [],
                "color": LIGHT_COLORS["temp_color"]
            },
            {
                "name": "Distancia (cm)",
                "data": [],
                "color": LIGHT_COLORS["dist_color"]
            }
        ]

        self.historical_data = []
        self.load_historical_data_from_db()

    def get_realtime_data(self):
        return self.realtime_data

    def get_historical_data(self):
        return self.historical_data

    def update_realtime_data(self):
        global latest_data

        # Cargar rangos óptimos desde la base de datos
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT id, optimal_min, optimal_max FROM sensors")
        ranges = {row[0]: (row[1], row[2]) for row in cursor.fetchall()}
        conn.close()

        for series in self.realtime_data:
            if series["name"] == "pH":
                v = self.generate_random_ph()
                min_ph, max_ph = ranges.get(1, (5.5, 6.5))  # ID 1 para pH
                if v is None or v == 0:
                    series["data"].append(0)
                    statusSensor["ph"] = False
                else:
                    series["data"].append(v)
                    statusSensor["ph"] = True  
                    if v < 5:
                        send_command(8)
                        print("Subir")
                    elif v > 10:
                        send_command(9)
                        print("Bajar")

            elif series["name"] == "EC (mS/cm)":
                v = latest_data.get("tds")
                min_ce, max_ce = ranges.get(2, (1.2, 1.6))  # ID 2 para EC
                if v is None or v == 0:
                    series["data"].append(0)
                    statusSensor["tds"] = False
                else:
                    series["data"].append(v)
                    statusSensor["tds"] = True
                    if v < min_ce:
                        enviarAlertaBajoTDS(v)  # Enviar alerta si el EC está fuera de rango
                    elif v > max_ce:
                        enviarAlertaAltoTDS(v)
            elif series["name"] == "Temperatura (°C)":
                v = latest_data.get("temp")
                min_temp, max_temp = ranges.get(3, (18, 22))  # ID 3 para Temperatura
                if v is None or v == 0:
                    series["data"].append(0)
                    statusSensor["temp"] = False
                else:
                    series["data"].append(v)
                    statusSensor["temp"] = True
                    if v < min_temp:
                        enviarAlertaBajaTemp(v)
                    elif v > max_temp:
                        enviarAlertaAltaTemp(v)
            elif series["name"] == "Distancia (cm)":
                v = latest_data.get("dist")
                min_dist, max_dist = ranges.get(4, (35, 50))  # ID 4 para Distancia
                if v is None or v == 0:
                    series["data"].append(0)
                    statusSensor["dist"] = False
                else:
                    series["data"].append(v)
                    statusSensor["dist"] = True
                    if v < min_dist:
                        enviarAlertaBajaDist(v)
                    elif v > max_dist:
                        enviarAlertaAltaDist(v)

            # Limitar la lista a los últimos 7 datos
            if len(series["data"]) > 7:
                series["data"].pop(0)

        return self.realtime_data

    def load_historical_data_from_db(self):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        sensor_names = {
            1: "pH Promedio",
            2: "EC Promedio (mS/cm)",
            3: "Temperatura Promedio (°C)",
            4: "Distancia (cm)"
        }

        sensor_data = {name: [] for name in sensor_names.values()}
        fechas = []

        for sensor_id, name in sensor_names.items():
            cursor.execute("""
                SELECT DATE(timestamp) as day, MAX(value)
                FROM sensor_readings
                WHERE sensor_id = ?
                AND timestamp >= DATE('now', '-30 day')
                AND value > 0
                GROUP BY day
                ORDER BY day ASC
            """, (sensor_id,))
            
            rows = cursor.fetchall()
            valores = [round(row[1], 2) for row in rows]
            fechas = [row[0] for row in rows]
            sensor_data[name] = valores

        conn.close()

        self.historical_labels = fechas  # Últimas 30 fechas como etiquetas

        self.historical_data = [
            {
                "name": name,
                "data": sensor_data[name],
                "color": LIGHT_COLORS[key]
            }
            for key, name in zip(
                ["ph_color", "ec_color", "temp_color", "dist_color"],
                ["pH Promedio", "EC Promedio (mS/cm)", "Temperatura Promedio (°C)", "Distancia (cm)"]
            )
        ]