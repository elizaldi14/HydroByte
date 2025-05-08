from PySide6.QtWidgets import QFrame, QVBoxLayout, QLabel, QSizePolicy, QGraphicsDropShadowEffect
from PySide6.QtGui import QFont, QColor, QPalette
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
        self.fecha = QLabel(f"{alert[3]}")
        self.fecha.setFont(QFont("Segoe UI", 10))
        self.layout.addWidget(self.pregunta)
        self.layout.addWidget(self.sensor)
        self.layout.addWidget(self.fecha)

    def apply_theme(self):
        colors = self.theme_manager.get_colors()
        
        # Apply styles without box-shadow
        self.setStyleSheet(f"""
            QFrame#alertCard {{
                background: {colors.get('card', '#FFFFFF')};
                border-radius: 14px;
                border: 2px solid {colors.get('border', '#E2E8F0')};
            }}
        """)
        
        # Create and apply drop shadow effect
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setXOffset(0)
        shadow.setYOffset(4)
        shadow.setColor(QColor(0, 0, 0, 25))  # Semi-transparent black
        self.setGraphicsEffect(shadow)
        
        self.pregunta.setStyleSheet(f"color: {colors.get('text', '#1E293B')};")
        self.sensor.setStyleSheet(f"color: {colors.get('text_secondary', '#64748B')};")
        self.fecha.setStyleSheet(f"color: {colors.get('text_secondary', '#64748B')};")
