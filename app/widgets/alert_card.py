from PySide6.QtWidgets import QFrame, QVBoxLayout, QLabel, QSizePolicy
from PySide6.QtGui import QFont, QColor
from PySide6.QtCore import Qt

class AlertCard(QFrame):
    def __init__(self, alert, theme_manager, parent=None):
        super().__init__(parent)
        self.theme_manager = theme_manager
        self.alert = alert
        self.setObjectName("alertCard")
        self.setMinimumSize(260, 90)
        self.setMaximumSize(320, 110)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(18, 12, 18, 12)
        self.layout.setSpacing(5)
        self.pregunta = QLabel(f"{alert[2]}")  # Mensaje
        self.pregunta.setFont(QFont("Segoe UI", 13, QFont.Bold))
        self.pregunta.setWordWrap(True)
        self.sensor = QLabel(f"Sensor: {alert[1]}")
        self.sensor.setFont(QFont("Segoe UI", 11))
        self.estado = QLabel(f"Estado: {alert[3]}")
        self.estado.setFont(QFont("Segoe UI", 11, QFont.Bold))
        self.fecha = QLabel(f"{alert[4]}")
        self.fecha.setFont(QFont("Segoe UI", 10))
        self.layout.addWidget(self.pregunta)
        self.layout.addWidget(self.sensor)
        self.layout.addWidget(self.estado)
        self.layout.addWidget(self.fecha)
        self.apply_theme()

    def apply_theme(self):
        colors = self.theme_manager.get_colors()
        estado_color = '#ef4444' if self.alert[3].lower() == 'activo' else '#22c55e' if self.alert[3].lower() == 'solucionado' else colors.get('text', '#1E293B')
        self.setStyleSheet(f"""
            QFrame#alertCard {{
                background: {colors.get('card', '#FFFFFF')};
                border-radius: 14px;
                border: 2px solid {colors.get('border', '#E2E8F0')};
                box-shadow: 0 4px 18px rgba(0,0,0,0.10);
            }}
        """)
        self.pregunta.setStyleSheet(f"color: {colors.get('text', '#1E293B')};")
        self.sensor.setStyleSheet(f"color: {colors.get('text_secondary', '#64748B')};")
        self.estado.setStyleSheet(f"color: {estado_color};")
        self.fecha.setStyleSheet(f"color: {colors.get('text_secondary', '#64748B')};")
