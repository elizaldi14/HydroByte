from PySide6.QtWidgets import (
    QFrame, QVBoxLayout, QLabel, QSizePolicy, QHBoxLayout, QGraphicsDropShadowEffect
)
from PySide6.QtGui import QFont, QColor
from PySide6.QtCore import Qt
from utils.data_generator import statusSensor

class SensorCard(QFrame):
    def __init__(self, title, name, unit, optimal_range, color, theme_manager, parent=None):
        super().__init__(parent)
        self.title = title
        self.name = name
        self.value = 0  # Valor fijo temporal
        self.unit = unit
        self.optimal_range = optimal_range
        self.color = color
        self.theme_manager = theme_manager
        
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
        
        self.value_label = QLabel(f"{self.value}")
        self.value_label.setFont(QFont("Segoe UI", 32, QFont.Bold))
        self.value_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        
        self.unit_label = QLabel(f"{self.unit}")
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

    def add_shadow(self):
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(15)
        shadow.setOffset(0, 6)
        shadow.setColor(QColor(0, 0, 0, 80))  # sombra suave
        self.setGraphicsEffect(shadow)

    def update_value(self, new_value):
        self.value = new_value
        self.value_label.setText(f"{self.value}")

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
        is_active = statusSensor.get(self.name, False)
        
        if is_active:
            self.status_label.setText("Activo")
            self.status_label.setStyleSheet("color: #22C55E; background: transparent;")  # Verde
        else:
            self.status_label.setText("Inactivo")
            self.status_label.setStyleSheet("color: #EF4444; background: transparent;")  # Rojo