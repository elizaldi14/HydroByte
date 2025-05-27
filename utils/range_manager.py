class RangeManager:
    def __init__(self):
        # Valores iniciales de los rangos óptimos
        self.ranges = {
            "pH": (5.5, 6.5),
            "Temperatura": (18.0, 24.0),
            "Conductividad Eléctrica": (1.5, 2.2),
            "Nivel de Agua": (70.0, 90.0),
        }

    def get_range(self, sensor):
        """Obtiene el rango óptimo de un sensor."""
        return self.ranges.get(sensor, (None, None))

    def set_range(self, sensor, min_value, max_value):
        """Establece un nuevo rango óptimo para un sensor."""
        if sensor in self.ranges:
            self.ranges[sensor] = (min_value, max_value)
        else:
            raise ValueError(f"Sensor desconocido: {sensor}")
