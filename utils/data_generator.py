from utils.constants import LIGHT_COLORS
from utils.serial_reader import latest_data  # Datos reales sin modificar


class DataGenerator:
    def __init__(self):
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
        # Añade datos reales al final, sin modificar
        for series in self.realtime_data:
            if series["name"] == "pH":
                series["data"].append(latest_data.get("ph"))
            elif series["name"] == "EC (mS/cm)":
                series["data"].append(latest_data.get("tds"))
            elif series["name"] == "Temperatura (°C)":
                series["data"].append(latest_data.get("temp"))
            elif series["name"] == "Distancia (cm)":
                series["data"].append(latest_data.get("dist"))

            # Limitar la lista a los últimos 7 datos
            if len(series["data"]) > 7:
                series["data"].pop(0)

        return self.realtime_data

    def update_historical_data(self):
        # Solo si quieres mantener un histórico básico para gráficas históricas
        for series in self.historical_data:
            if series["name"] == "pH Promedio":
                series["data"].append(latest_data.get("ph"))
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
