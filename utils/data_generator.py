import random
from utils.constants import LIGHT_COLORS

class DataGenerator:
    def __init__(self):
        # Datos iniciales para el gráfico en tiempo real
        self.realtime_data = [
            {
                "name": "pH",
                "data": [6.2, 6.3, 6.5, 6.4, 6.2, 6.1, 6.3],
                "color": LIGHT_COLORS["ph_color"]
            },
            {
                "name": "EC (mS/cm)",
                "data": [1.8, 1.7, 1.9, 2.0, 1.9, 1.8, 1.7],
                "color": LIGHT_COLORS["ec_color"]
            },
            {
                "name": "Temperatura (°C)",
                "data": [22, 23, 24, 25, 24, 23, 22],
                "color": LIGHT_COLORS["temp_color"]
            }
        ]
        
        # Datos iniciales para el gráfico histórico
        self.historical_data = [
            {
                "name": "pH Promedio",
                "data": [6.3, 6.4, 6.2, 6.3, 6.5, 6.4, 6.3],
                "color": LIGHT_COLORS["ph_color"]
            },
            {
                "name": "EC Promedio (mS/cm)",
                "data": [1.7, 1.8, 1.9, 1.8, 1.7, 1.9, 2.0],
                "color": LIGHT_COLORS["ec_color"]
            },
            {
                "name": "Temperatura Promedio (°C)",
                "data": [21, 22, 23, 24, 25, 23, 22],
                "color": LIGHT_COLORS["temp_color"]
            }
        ]
    
    def get_realtime_data(self):
        return self.realtime_data
    
    def get_historical_data(self):
        return self.historical_data
    
    def update_realtime_data(self):
        # Simular nuevos datos
        for series in self.realtime_data:
            # Eliminar el primer valor y añadir uno nuevo al final
            series["data"].pop(0)
            
            if series["name"] == "pH":
                new_value = round(random.uniform(5.8, 6.8), 1)
                series["data"].append(new_value)
            elif series["name"] == "EC (mS/cm)":
                new_value = round(random.uniform(1.5, 2.2), 1)
                series["data"].append(new_value)
            elif series["name"] == "Temperatura (°C)":
                new_value = round(random.uniform(18, 26))
                series["data"].append(new_value)
        
        return self.realtime_data
    
    def update_historical_data(self):
        # Simular nuevos datos históricos (por ejemplo, para actualización diaria)
        for series in self.historical_data:
            # Eliminar el primer valor y añadir uno nuevo al final
            series["data"].pop(0)
            
            if series["name"] == "pH Promedio":
                new_value = round(random.uniform(6.0, 6.6), 1)
                series["data"].append(new_value)
            elif series["name"] == "EC Promedio (mS/cm)":
                new_value = round(random.uniform(1.6, 2.1), 1)
                series["data"].append(new_value)
            elif series["name"] == "Temperatura Promedio (°C)":
                new_value = round(random.uniform(20, 25))
                series["data"].append(new_value)
        
        return self.historical_data