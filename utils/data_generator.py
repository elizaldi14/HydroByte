from utils.constants import LIGHT_COLORS
from utils.serial_reader import latest_data  # Datos reales sin modificar
import random
import sqlite3
from utils.alerts import *

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

        for series in self.realtime_data:
            if series["name"] == "pH":
                v = self.generate_random_ph()
                if v is None or v == 0:
                    series["data"].append(0)
                    statusSensor["ph"] = False
                else:
                    series["data"].append(v)
                    statusSensor["ph"] = True  
                    if v < 5.5 or v > 6.2:
                        enviarAlertaPH(v) # Enviar alerta si el pH está fuera de rango
            elif series["name"] == "EC (mS/cm)":
                v = self.generate_random_ce()
                if v is None or v == 0:
                    series["data"].append(0)
                    statusSensor["tds"] = False
                else:
                    series["data"].append(v)
                    statusSensor["tds"] = True
                    if v < 1.2:
                        enviarAlertaBajoTDS(v) # Enviar alerta si el pH está fuera de rango
                    elif v > 1.6:
                        enviarAlertaAltoTDS(v) # Enviar alerta si el pH está fuera de rango
            elif series["name"] == "Temperatura (°C)":
                v = self.generate_random_temp()
                if v is None or v == 0:
                    series["data"].append(0)
                    statusSensor["temp"] = False
                else:
                    series["data"].append(v)
                    statusSensor["temp"] = True
                    if v < 18:
                        enviarAlertaBajaTemp(v)
                    elif v > 22:
                        enviarAlertaAltaTemp(v)
            elif series["name"] == "Distancia (cm)":
                v = self.generate_random_dist()
                if v is None or v == 0:
                    series["data"].append(0)
                    statusSensor["dist"] = False
                else:
                    series["data"].append(v)
                    statusSensor["dist"] = True
                    if v < 35:
                        enviarAlertaBajaDist(v)
                    elif v > 50:
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