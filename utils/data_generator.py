from utils.constants import LIGHT_COLORS
from utils.serial_reader import latest_data  # Datos reales sin modificar
import random
import sqlite3
from datetime import datetime

DB_PATH = "hydrobyte.sqlite"

statusSensor = {
    "ph": True,  # Comentado para prueba
    "tds": True,
    "temp": True,
    "dist": True
}

class DataGenerator:
    def generate_random_ph(self):
        if random.random() < 0.1:  # 10% de probabilidad de fallo
            print("Fallo en pH")
            return None
        print(round(random.uniform(5.5, 8.5), 2))
        return round(random.uniform(5.5, 8.5), 2)
    

    def __init__(self):
        # self.generate_random_ph()
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
                v = latest_data.get("ph")
                if v is None or v == 0:
                    series["data"].append(0)
                    statusSensor["ph"] = False
                else:
                    series["data"].append(v)
                    statusSensor["tds"] = True
                    statusSensor["ph"] = True  
            elif series["name"] == "EC (mS/cm)":
                v = latest_data.get("tds")
                if v is None or v == 0:
                    series["data"].append(0)
                    statusSensor["tds"] = False
                else:
                    series["data"].append(v)
                    statusSensor["tds"] = True
            elif series["name"] == "Temperatura (°C)":
                v = latest_data.get("temp")
                if v is None or v == 0:
                    series["data"].append(0)
                    statusSensor["temp"] = False
                else:
                    series["data"].append(v)
                    statusSensor["temp"] = True
            elif series["name"] == "Distancia (cm)":
                v = latest_data.get("dist")
                if v is None or v == 0:
                    series["data"].append(0)
                    statusSensor["dist"] = False
                else:
                    series["data"].append(v)
                    statusSensor["dist"] = True

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