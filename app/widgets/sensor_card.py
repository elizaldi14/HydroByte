from PySide6.QtWidgets import (
    QFrame, QVBoxLayout, QLabel, QSizePolicy, QHBoxLayout, QGraphicsDropShadowEffect
)
from PySide6.QtGui import QFont, QColor
from PySide6.QtCore import Qt
import sqlite3

class SensorCard(QFrame):
    def __init__(self, title, sensor_id, unit, color, theme_manager, db_path, parent=None):
        super().__init__(parent)
        self.title = title
        self.sensor_id = sensor_id  # Cambiado de name a sensor_id
        self.unit = unit
        self.color = color
        self.theme_manager = theme_manager
        self.db_path = db_path  # Ruta de la base de datos
        self.optimal_range = self.get_optimal_range()  # Obtiene el rango óptimo desde la base de datos
        
        self.setup_ui()
        self.apply_theme()
        self.add_shadow()

    def setup_ui(self):
        self.setFrameShape(QFrame.StyledPanel)
        self.setMinimumHeight(150)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setObjectName("sensorCard")
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(10)
        
        # Icono y título
        header_layout = QHBoxLayout()
        
        icon_label = QLabel()
        icon_label.setFixedSize(32, 32)
        icon_label.setAlignment(Qt.AlignCenter)
        icon_label.setText(self.title[0] if self.title else "S")
        icon_label.setObjectName("iconLabel")
        self.icon_label = icon_label

        self.title_label = QLabel(self.title)
        self.title_label.setFont(QFont("Segoe UI", 14, QFont.Bold))
        
        header_layout.addWidget(icon_label)
        header_layout.addWidget(self.title_label)
        header_layout.addStretch()
        
        # Valor
        value_layout = QHBoxLayout()
        value_layout.setAlignment(Qt.AlignCenter)
        
        self.value_label = QLabel("0")  # Valor inicial
        self.value_label.setFont(QFont("Segoe UI", 32, QFont.Bold))
        self.value_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        
        self.unit_label = QLabel(self.unit)
        self.unit_label.setFont(QFont("Segoe UI", 18))
        self.unit_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        
        value_layout.addStretch()
        value_layout.addWidget(self.value_label)
        value_layout.addWidget(self.unit_label)
        value_layout.addStretch()
        
        # Rango óptimo
        self.range_label = QLabel(f"Rango óptimo: {self.optimal_range}")
        self.range_label.setFont(QFont("Segoe UI", 10))
        self.range_label.setAlignment(Qt.AlignCenter)
        
        # Estado Activo/Inactivo
        self.status_label = QLabel()
        self.status_label.setFont(QFont("Segoe UI", 11, QFont.Bold))
        self.status_label.setAlignment(Qt.AlignCenter)
        self.set_status()  # Por defecto Activo, puedes cambiarlo luego
        
        # Añadir todo al layout principal
        layout.addLayout(header_layout)
        layout.addLayout(value_layout)
        layout.addWidget(self.range_label)
        layout.addWidget(self.status_label)

    def reload_optimal_range(self):
        """Recarga el rango óptimo desde la base de datos y actualiza la etiqueta."""
        self.optimal_range = self.get_optimal_range()
        self.range_label.setText(f"Rango óptimo: {self.optimal_range}")

    def get_optimal_range(self):
        """Obtiene el rango óptimo desde la base de datos."""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT optimal_min, optimal_max FROM sensors WHERE id = ?", (self.sensor_id,))
            result = cursor.fetchone()
            conn.close()
            if result:
                return f"{result[0]} - {result[1]}"
            else:
                return "No definido"
        except sqlite3.Error as e:
            print(f"Error al obtener el rango óptimo para el sensor con ID {self.sensor_id}: {e}")
            return "Error"

    def add_shadow(self):
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(15)
        shadow.setOffset(0, 6)
        shadow.setColor(QColor(0, 0, 0, 80))  # sombra suave
        self.setGraphicsEffect(shadow)

    def update_value(self, new_value):
        self.value_label.setText(f"{new_value}")

    def apply_theme(self):
        colors = self.theme_manager.get_colors()
        self.setStyleSheet(f"""
            QFrame#sensorCard {{
                background-color: {colors['card']};
                border: 1px solid {colors['border']};
                border-radius: 16px;
                font-weight: bold;
                font-size: 16px;
            }}
        """)
        self.title_label.setStyleSheet(f"color: {colors['text']}; background-color: transparent;")
        self.value_label.setStyleSheet(f"color: {self.color}; background-color: transparent;")
        self.unit_label.setStyleSheet(f"color: {colors['text_secondary']}; background-color: transparent;")
        self.range_label.setStyleSheet(f"color: {colors['text_secondary']}; background-color: transparent;")
        # El status_label mantiene su color por estado, pero sí le quitamos fondo
        self.status_label.setStyleSheet(self.status_label.styleSheet() + "background: transparent;")

    def set_status(self):
        # Aquí puedes implementar la lógica para determinar si el sensor está activo o inactivo
        self.status_label.setText("Activo")
        self.status_label.setStyleSheet("color: #22C55E; background: transparent;")  # Verde