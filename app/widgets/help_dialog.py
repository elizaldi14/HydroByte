from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QLabel, QDialogButtonBox, QTextEdit
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class HelpDialog(QDialog):
    """Diálogo de ayuda que muestra información sobre un sensor específico."""
    
    # Información de ayuda para cada tipo de sensor
    SENSOR_INFO = {
        1: {
            "title": "Sensor de pH",
            "description": (
                "El pH mide la acidez o alcalinidad del agua en una escala de 0 a 14.\n\n"
                "• Rango óptimo: 5.5 - 6.5\n"
                "• pH < 7: Solución ácida\n"
                "• pH = 7: Solución neutra\n"
                "• pH > 7: Solución alcalina\n\n"
                "Un pH inadecuado puede afectar la absorción de nutrientes por las plantas."
            )
        },
        2: {
            "title": "Sensor de Conductividad Eléctrica (CE)",
            "description": (
                "La CE mide la concentración de sales disueltas en el agua, indicando la cantidad de nutrientes.\n\n"
                "• Rango óptimo: 1.2 - 1.8 mS/cm\n"
                "• Valores bajos: Falta de nutrientes\n"
                "• Valores altos: Exceso de nutrientes\n\n"
                "Una CE inadecuada puede causar deficiencias o toxicidad en las plantas."
            )
        },
        3: {
            "title": "Sensor de Temperatura",
            "description": (
                "Mide la temperatura del agua de la solución nutritiva.\n\n"
                "• Rango óptimo: 18°C - 25°C\n"
                "• < 18°C: Crecimiento lento\n"
                "• > 25°C: Bajo oxígeno, riesgo de hongos\n\n"
                "La temperatura afecta la absorción de oxígeno y nutrientes."
            )
        },
        4: {
            "title": "Sensor de Nivel de Agua",
            "description": (
                "Mide la altura del agua en el depósito.\n\n"
                "• Rango óptimo: 30 - 50 cm\n"
                "• Nivel bajo: Riesgo de sequía\n"
                "• Nivel alto: Riesgo de desborde\n\n"
                "Mantener un nivel adecuado asegura el suministro constante de nutrientes."
            )
        }
    }
    
    def __init__(self, sensor_id, parent=None):
        super().__init__(parent)
        self.sensor_id = sensor_id
        self.setWindowTitle("Información del Sensor")
        self.setMinimumSize(400, 300)
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        
        # Título
        title_label = QLabel(self.SENSOR_INFO[self.sensor_id]["title"])
        title_label.setFont(QFont("Segoe UI", 16, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        
        # Descripción
        description = QTextEdit()
        description.setReadOnly(True)
        description.setPlainText(self.SENSOR_INFO[self.sensor_id]["description"])
        description.setFont(QFont("Segoe UI", 11))
        description.setStyleSheet("""
            QTextEdit {
                background: transparent;
                border: 1px solid #E2E8F0;
                border-radius: 8px;
                padding: 10px;
            }
        """)
        
        # Botones
        button_box = QDialogButtonBox(QDialogButtonBox.Ok)
        button_box.accepted.connect(self.accept)
        
        layout.addWidget(title_label)
        layout.addWidget(description)
        layout.addWidget(button_box)
        
        # Estilos para el diálogo de ayuda
        self.setStyleSheet("""
            QDialog {
                background: #2D3748;
                border-radius: 10px;
            }
            QLabel {
                color: #FFFFFF;
            }
            QTextEdit {
                background: #4A5568;
                border: 1px solid #4A5568;
                border-radius: 8px;
                padding: 15px;
                color: #FFFFFF;
                font-size: 13px;
            }
            QTextEdit QScrollBar:vertical {
                background: #4A5568;
                width: 12px;
                margin: 0px;
            }
            QTextEdit QScrollBar::handle:vertical {
                background: #718096;
                min-height: 20px;
                border-radius: 6px;
            }
            QTextEdit QScrollBar::add-line:vertical, 
            QTextEdit QScrollBar::sub-line:vertical {
                height: 0px;
            }
            QPushButton {
                background: #4299E1;
                color: white;
                border: none;
                padding: 8px 20px;
                border-radius: 6px;
                font-weight: bold;
                min-width: 100px;
                font-size: 13px;
            }
            QPushButton:hover {
                background: #3182CE;
            }
        """)
