from PySide6.QtWidgets import (
    QFrame, QVBoxLayout, QLabel, QSizePolicy, QHBoxLayout, 
    QGraphicsDropShadowEffect, QPushButton
)
from PySide6.QtGui import QFont, QColor, QPixmap, QIcon
from PySide6.QtCore import Qt, QSize
import sqlite3
import os

from .help_dialog import HelpDialog

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
        
        # Icono, título y botón de ayuda
        header_layout = QHBoxLayout()
        
        # Icono
        icon_label = QLabel()
        icon_label.setFixedSize(32, 32)
        icon_label.setAlignment(Qt.AlignCenter)
        icon_label.setPixmap(self.get_icon_for_sensor())
        icon_label.setObjectName("iconLabel")
        self.icon_label = icon_label

        # Título (hazlo clickeable)
        self.title_label = QLabel(self.title)
        self.title_label.setFont(QFont("Segoe UI", 14, QFont.Bold))
        self.title_label.setCursor(Qt.PointingHandCursor)
        self.title_label.setToolTip(f"Haz clic para más información sobre {self.title.lower()}")
        
        # Estilos para el título
        self.title_label.setStyleSheet(f"""
            QLabel {{
                color: {self.color};
            }}
            QLabel:hover {{
                color: {self.color};
                text-decoration: underline;
            }}
        """)
        
        # Hacer que el QLabel sea clickeable
        self.title_label.mousePressEvent = self.on_title_clicked
        
        # Botón de ayuda (ahora oculto ya que el título es clickeable)
        self.help_button = QPushButton()
        self.help_button.setIcon(QIcon(self._get_help_icon_path()))
        self.help_button.setIconSize(QSize(20, 20))
        self.help_button.setFixedSize(24, 24)
        self.help_button.setFlat(True)
        self.help_button.setCursor(Qt.PointingHandCursor)
        self.help_button.clicked.connect(self.show_help)
        self.help_button.setToolTip("Ayuda")
        self.help_button.setObjectName("helpButton")
        self.help_button.hide()  # Ocultamos el botón ya que el título es clickeable
        
        header_layout.addWidget(icon_label)
        header_layout.addWidget(self.title_label)
        header_layout.addStretch()
        header_layout.addWidget(self.help_button)
        
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
            
            if result and result[0] is not None and result[1] is not None:
                # Asegurarse de que los valores sean numéricos
                min_val = float(result[0])
                max_val = float(result[1])
                return f"{min_val} - {max_val}"
            else:
                # Valores por defecto para cada tipo de sensor si no están definidos
                default_ranges = {
                    1: "5.5 - 6.5",    # pH
                    2: "1.2 - 1.8",    # EC (mS/cm)
                    3: "18.0 - 25.0",  # Temperatura (°C)
                    4: "30.0 - 50.0"   # Distancia (cm)
                }
                return default_ranges.get(self.sensor_id, "No definido")
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
        self._update_value_color(float(new_value))
    
    def _update_value_color(self, value):
        try:
            # Obtener el rango óptimo
            if " - " in self.optimal_range:
                min_val, max_val = map(float, self.optimal_range.split(" - "))
                
                # Verificar si el valor está dentro del rango óptimo
                if min_val <= value <= max_val:
                    # Verde: Dentro del rango óptimo
                    self.value_label.setStyleSheet("color: #10B981; background-color: transparent;")
                # Verificar si está fuera por 1 o 2 unidades
                elif (min_val - 2 <= value < min_val) or (max_val < value <= max_val + 2):
                    # Naranja: Fuera por 1 o 2 unidades
                    self.value_label.setStyleSheet("color: #F59E0B; background-color: transparent;")
                else:
                    # Rojo: Fuera por más de 2 unidades
                    self.value_label.setStyleSheet("color: #EF4444; background-color: transparent;")
        except (ValueError, AttributeError) as e:
            print(f"Error al actualizar el color del valor: {e}")
            # En caso de error, mantener el color por defecto
            self.value_label.setStyleSheet(f"color: {self.color}; background-color: transparent;")

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
            #helpButton {{
                background: transparent;
                border: none;
                border-radius: 12px;
                padding: 2px;
            }}
            #helpButton:hover {{
                background: {colors['border']};
            }}
            QLabel[text*="<a"] {{
                color: {self.color};
            }}
            QLabel[text*="<a"]:hover {{
                text-decoration: underline;
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

    def _get_help_icon_path(self):
        """Devuelve la ruta del ícono de ayuda según el tema actual."""
        theme = "dark" if self.theme_manager.is_dark_mode else "light"
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../assets/img"))
        return os.path.join(base_path, f"help_{theme}.svg")

    def get_icon_for_sensor(self):
        """Devuelve el ícono correspondiente al sensor."""
        theme = "white" if self.theme_manager.is_dark_mode else "black"
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../assets/img"))
        icon_map = {
            1: f"ph_{theme}.png",    # Ícono para pH
            2: f"ec_{theme}.png",     # Ícono para EC
            3: f"temp_{theme}.png",   # Ícono para Temperatura
            4: f"water_{theme}.png"   # Ícono para Nivel de Agua
        }
        icon_path = os.path.join(base_path, icon_map.get(self.sensor_id, ""))
        
        if os.path.exists(icon_path):
            pixmap = QPixmap(icon_path)
            if pixmap.isNull():
                print(f"Error: No se pudo cargar el ícono desde {icon_path}")
            return pixmap
        else:
            print(f"Advertencia: No se encontró el ícono en la ruta {icon_path}")
            return QPixmap()
    
    def on_title_clicked(self, event):
        """Maneja el evento de clic en el título del sensor."""
        if event.button() == Qt.LeftButton:
            self.show_help()
    
    def show_help(self):
        """Muestra el diálogo de ayuda para este sensor."""
        from app.widgets.help_dialog import HelpDialog
        dialog = HelpDialog(self.sensor_id, self.theme_manager, self)
        
        # Aplicar tema oscuro si es necesario
        if hasattr(self.theme_manager, 'is_dark_mode') and self.theme_manager.is_dark_mode:
            dialog.setStyleSheet("""
                QDialog {
                    background-color: #2D3748;
                    color: #E2E8F0;
                }
                QLabel, QTextEdit {
                    color: #E2E8F0;
                }
                QTextEdit {
                    background-color: #4A5568;
                    border: 1px solid #4A5568;
                    border-radius: 6px;
                    padding: 10px;
                }
                QPushButton {
                    background-color: #4299E1;
                    color: white;
                    border: none;
                    padding: 8px 16px;
                    border-radius: 4px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #3182CE;
                }
            """)
        
        dialog.exec()