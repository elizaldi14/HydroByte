from utils.constants import LIGHT_COLORS
from utils.serial_reader import latest_data  # Datos reales sin modificar
import random

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

        self.historical_data = [
            {
                "name": "pH Promedio",
                "data": [],
                "color": LIGHT_COLORS["ph_color"]
            },
            {
                "name": "EC Promedio (mS/cm)",
                "data": [],
                "color": LIGHT_COLORS["ec_color"]
            },
            {
                "name": "Temperatura Promedio (°C)",
                "data": [],
                "color": LIGHT_COLORS["temp_color"]
            },
            {
                "name": "Distancia (cm)",
                "data": [],
                "color": LIGHT_COLORS["dist_color"]
            }
        ]

    def get_realtime_data(self):
        return self.realtime_data

    def get_historical_data(self):
        return self.historical_data

    def update_realtime_data(self):
        global latest_data
        # Si latest_data está vacío o todos sus valores son None, todos los sensores están inactivos
        # if not latest_data or all(v is None for v in latest_data.values()):
        #     for k in statusSensor:
        #         statusSensor[k] = False
        #     for series in self.realtime_data:
        #         series["data"].append(0)
        #         if len(series["data"]) > 7:
        #             series["data"].pop(0)
        #     return self.realtime_data

        for series in self.realtime_data:
            if series["name"] == "pH":
                l = self.generate_random_ph()
                if l is None:
                    series["data"].append(0)
                    statusSensor["ph"] = False
                else:
                    series["data"].append(l)
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

    def update_historical_data(self):
        # Solo si quieres mantener un histórico básico para gráficas históricas
        for series in self.historical_data:
            if series["name"] == "pH Promedio":
                series["data"].append(self.generate_random_ph())
            elif series["name"] == "EC Promedio (mS/cm)":
                series["data"].append(latest_data.get("tds"))
            elif series["name"] == "Temperatura Promedio (°C)":
                series["data"].append(latest_data.get("temp"))
            elif series["name"] == "Distancia (cm)":
                series["data"].append(latest_data.get("dist"))

            # Limitar la lista a 7 entradas
            if len(series["data"]) > 7:
                series["data"].pop(0)

        return self.historical_data
