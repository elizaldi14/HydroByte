from PySide6.QtWidgets import (QWidget, QVBoxLayout, QLabel, QPushButton, QFrame, QMessageBox)
from PySide6.QtCore import Qt, QObject, Signal, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QFont, QPixmap, QPainter, QColor
import os
import threading
import time
from utils.serial_reader import PumpSerial
from utils.constants import LIGHT_COLORS
# Removed global pump_serial instance - it should be created in main.py and passed to pumps

class PumpCard(QFrame):
    """Clase base abstracta para todas las bombas"""
    def __init__(self, pump_name, theme_manager, img, description, serial_conn, parent=None, read_only=False):
        super().__init__(parent)
        self.theme_manager = theme_manager
        self.pump_name = pump_name
        self.img = img
        self.description = description
        self.serial = serial_conn
        self.thread = None
        self.stop_event = threading.Event()
        self.automation_enabled = False
        self.read_only = read_only
        self.setup_ui()
        self.apply_theme()

    
    def setup_ui(self):
        self.setObjectName("pumpCard")
        self.setFixedSize(350, 450)  # Aumentado ligeramente para mejor espaciado
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)

        # Layout principal con márgenes y espaciado mejorados
        self.layout = QVBoxLayout(self)
        self.layout.setSpacing(12)
        self.layout.setContentsMargins(20, 20, 20, 20)  # Márgenes iguales en todos los lados

        # Título
        self.title = QLabel(self.pump_name)
        self.title.setFont(QFont("Segoe UI", 18, QFont.Bold))
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setObjectName("titleLabel")
        self.layout.addWidget(self.title)
        
        # Descripción
        self.description_label = QLabel(self.description)
        self.description_label.setFont(QFont("Segoe UI", 11))
        self.description_label.setAlignment(Qt.AlignCenter)
        self.description_label.setWordWrap(True)
        self.description_label.setObjectName("descriptionLabel")
        self.layout.addWidget(self.description_label)
        
        # Espaciador
        self.layout.addSpacing(5)

        # Icono de la bomba
        iconLabel = QLabel()
        iconLabel.setFixedSize(140, 140)  # Tamaño ligeramente reducido
        iconLabel.setScaledContents(True)
        iconLabel.setAlignment(Qt.AlignCenter)
        iconLabel.setObjectName("iconLabel")
        self.iconLabel = iconLabel

        # Cargar y configurar el ícono
        iconPath = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', '..', 'utils', 'img', self.img)
        )
        if os.path.exists(iconPath):
            iconPixmap = QPixmap(iconPath)
            # Aplicar filtro de color según el tema
            if hasattr(self, 'theme_manager') and self.theme_manager.is_dark_mode:
                # Crear una imagen con filtro blanco para modo oscuro
                white_pixmap = iconPixmap
                painter = QPainter(white_pixmap)
                painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
                painter.fillRect(white_pixmap.rect(), QColor(255, 255, 255))
                painter.end()
                iconPixmap = white_pixmap
            
            iconPixmap = iconPixmap.scaled(140, 140, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            iconLabel.setPixmap(iconPixmap)
        else:
            iconLabel.setText(iconPath[0].upper())
        
        self.layout.addWidget(iconLabel, alignment=Qt.AlignCenter)
        self.layout.addSpacing(5)

        # Estado principal
        self.status_label = QLabel("Estado: Detenida")
        self.status_label.setFont(QFont("Segoe UI", 12))
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setObjectName("statusLabel")
        self.layout.addWidget(self.status_label)

        # Solo si es read_only, añadir el segundo label
        if self.read_only:
            self.status_label2 = QLabel("Modo: AUTOMÁTICO")
            self.status_label2.setFont(QFont("Segoe UI", 12))
            self.status_label2.setAlignment(Qt.AlignCenter)
            self.status_label2.setObjectName("statusLabel2")
            self.status_label.setText("Estado: Lista")
            self.layout.addWidget(self.status_label2)


        # Espaciador para empujar los botones hacia abajo
        self.layout.addStretch()

        if not self.read_only:
            self.update_button_style(False)
            self.button_layout = QVBoxLayout()
            self.button_layout.setSpacing(8)
            self.button_layout.setContentsMargins(10, 10, 10, 10)

            self.toggle_btn = QPushButton("Iniciar")
            self.toggle_btn.setFont(QFont("Segoe UI", 12, QFont.Bold))
            self.toggle_btn.setMinimumHeight(40)
            self.toggle_btn.clicked.connect(self.toggle_pump)
            self.toggle_btn.setObjectName("toggleButton")
            self.button_layout.addWidget(self.toggle_btn)

            if not hasattr(self, 'is_ph_pump'):
                self.auto_btn = QPushButton("Modo Manual")
                self.auto_btn.setFont(QFont("Segoe UI", 11))
                self.auto_btn.setMinimumHeight(36)
                self.auto_btn.clicked.connect(self.toggle_automation)
                self.auto_btn.setObjectName("autoButton")
                self.button_layout.addWidget(self.auto_btn)

            self.layout.addLayout(self.button_layout)

        
        # Inicializar estados
        self.automation_enabled = False
        self.update_button_style(False)
        
        # Aplicar el tema inicial
        self.apply_theme()

    def apply_theme(self):
        colors = self.theme_manager.get_colors()
        self.setStyleSheet(f"""
            QFrame#pumpCard {{
                background: {colors['card']};
                border: 1px solid {colors['border']};
                border-radius: 12px;
            }}
            #titleLabel {{
                color: {colors['text']};
                margin-bottom: 5px;
            }}
            #descriptionLabel {{
                color: {colors['text_secondary']};
                margin-bottom: 10px;
            }}
            #statusLabel {{
                color: {colors['text_secondary']};
                margin: 5px 0;
            }}
            #toggleButton {{
                background-color: {colors['primary']};
                color: white;
                border: none;
                border-radius: 8px;
                padding: 8px;
                font-weight: bold;
            }}
            #toggleButton:hover {{
                background-color: {colors['primary_light']};
            }}
            #toggleButton:pressed {{
                background-color: {colors['primary']};
            }}
            #autoButton {{
                background-color: {colors['card']};
                color: {colors['text_secondary']};
                border: 1px solid {colors['border']};
                border-radius: 8px;
                padding: 6px;
            }}
            #autoButton:hover {{
                background-color: {colors['background']};
                border-color: {colors['border']};
            }}
            #autoButton:pressed {{
                background-color: {colors['background']};
            }}
            #iconLabel {{
                margin: 10px 0;
            }}
        """)

    def send_command(self, command):
        """Método común para enviar comandos"""
        if self.serial.write(str(command).encode()):
            print(f"Comando {command} enviado a {self.pump_name}")
            return True
        return False
    
    # Métodos abstractos que cada bomba debe implementar
    def start_pump(self):
        raise NotImplementedError
        
    def stop_pump(self):
        raise NotImplementedError

    def toggle_pump(self, send_stop_command=True):
        if self.thread and self.thread.is_alive():
            self.stop_event.set()
            self.thread.join()
            if send_stop_command:
                self.stop_pump()
            self.status_label.setText("Estado: Detenida")
            self.toggle_btn.setText("Iniciar")
            self.update_button_style(False)
        else:
            self.stop_event.clear()
            self.thread = threading.Thread(target=self.run_pump, daemon=True)
            self.thread.start()
            self.status_label.setText("Estado: En funcionamiento")
            self.toggle_btn.setText("Detener")
            self.update_button_style(True)

    def run_pump(self):
        while not self.stop_event.is_set():
            if self.automation_enabled and hasattr(self, 'is_water_pump'):
                self.send_command(2)  # Comando automático para bomba de agua
            else:
                self.start_pump()
            
            print(f"Pump running in {'auto' if self.automation_enabled else 'manual'} mode...")
            time.sleep(1)
        self.stop_pump()
        print("Pump stopped.")

    def toggle_automation(self):
        self.automation_enabled = not self.automation_enabled
        
        # Aplicar estilos a través de la hoja de estilo principal usando selectores de estado
        if self.theme_manager.is_dark_mode:
            if self.automation_enabled:
                self.auto_btn.setStyleSheet("""
                    #autoButton {
                        background-color: #9F7AEA;
                        color: white;
                        border: 1px solid #9F7AEA;
                    }
                    #autoButton:hover {
                        background-color: #805AD5;
                        border-color: #805AD5;
                    }
                    #autoButton:pressed {
                        background-color: #6B46C1;
                    }
                """)
            else:
                self.auto_btn.setStyleSheet("""
                    #autoButton {
                        background-color: #4A5568;
                        color: #E2E8F0;
                        border: 1px solid #4A5568;
                    }
                    #autoButton:hover {
                        background-color: #2D3748;
                        border-color: #4A5568;
                    }
                    #autoButton:pressed {
                        background-color: #2D3748;
                    }
                """)
        else:
            if self.automation_enabled:
                self.auto_btn.setStyleSheet("""
                    #autoButton {
                        background-color: #9F7AEA;
                        color: white;
                        border: 1px solid #9F7AEA;
                    }
                    #autoButton:hover {
                        background-color: #805AD5;
                        border-color: #805AD5;
                    }
                    #autoButton:pressed {
                        background-color: #6B46C1;
                    }
                """)
            else:
                self.auto_btn.setStyleSheet("""
                    #autoButton {
                        background-color: #EDF2F7;
                        color: #2D3748;
                        border: 1px solid #E2E8F0;
                    }
                    #autoButton:hover {
                        background-color: #E2E8F0;
                        border-color: #CBD5E0;
                    }
                    #autoButton:pressed {
                        background-color: #CBD5E0;
                    }
                """)
        
        # Actualizar el texto del botón
        self.auto_btn.setText("Modo Automático" if self.automation_enabled else "Modo Manual")
        
        # Iniciar la bomba si no está en marcha y se activa el modo automático
        if self.automation_enabled and not (self.thread and self.thread.is_alive()):
            self.toggle_pump(send_stop_command=False)
            # No detenemos la bomba al cambiar a modo manual
            # Solo actualizamos el estado del botón si es necesario
            self.update_button_style(self.thread and self.thread.is_alive())
            
            # Si la bomba está detenida, la iniciamos en modo manual
            if not (self.thread and self.thread.is_alive()):
                self.toggle_pump(send_stop_command=False)
            if hasattr(self, 'is_water_pump'):  # Solo para bomba de agua
                self.send_command(1)  # Volver a manual pero encendida
        
        self.update_button_style(self.thread and self.thread.is_alive())

    def update_button_style(self, is_running):
        # Si el botón no existe (modo read_only), no intentar modificarlo
        if not hasattr(self, "toggle_btn"):
            return

        if not self.automation_enabled:
            color = "#EF4444" if is_running else "#22C55E"
            hover = "#DC2626" if is_running else "#16A34A"
            self.toggle_btn.setEnabled(True)
            self.toggle_btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: {color};
                    color: white;
                    border: none;
                    border-radius: 8px;
                    padding: 10px;
                    margin-top: 0px;
                }}
                QPushButton:hover {{
                    background-color: {hover};
                }}
            """)
        else:
            self.toggle_btn.setEnabled(False)
            self.toggle_btn.setStyleSheet("""
                QPushButton {
                    background-color: #9CA3AF;
                    color: white;
                    border: none;
                    border-radius: 8px;
                    padding: 10px;
                    margin-top: 0px;
                }
            """)

class WaterPump(PumpCard):
    """Bomba principal de circulación de agua"""
    def __init__(self, theme_manager, serial_conn, parent=None):
        self.is_water_pump = True  # Marcar como bomba de agua
        super().__init__(
            pump_name="Bomba de Circulación",
            theme_manager=theme_manager,
            img="pump_circulacion.png",
            description="Circula el agua en el sistema",
            serial_conn=serial_conn,
            parent=parent
        )
    
    def toggle_automation(self):
        was_auto = self.automation_enabled
        super().toggle_automation()
        if was_auto and not self.automation_enabled:
            self.send_command(1)  # Volver a manual pero encendida
    
    def start_pump(self):
        return self.send_command(1)
        
    def stop_pump(self):
        return self.send_command(0)

class PhUpPump(PumpCard):
    def __init__(self, theme_manager, serial_conn, parent=None):
        self.is_ph_pump = True
        super().__init__(
            pump_name="Bomba pH+",
            theme_manager=theme_manager,
            img="pump.png",
            description="Aumenta el pH del agua",
            serial_conn=serial_conn,
            parent=parent,
            read_only=True  # ← Aquí
        )

    
    def start_pump(self):
        return self.send_command(3)
        
    def stop_pump(self):
        return self.send_command(4)

class PhDownPump(PumpCard):
    """Bomba peristáltica para disminuir pH"""
    def __init__(self, theme_manager, serial_conn, parent=None):
        self.is_ph_pump = True
        super().__init__(
            pump_name="Bomba pH-",
            theme_manager=theme_manager,
            img="pump.png",
            description="Disminuye el pH del agua",
            serial_conn=serial_conn,
            parent=parent,
            read_only=True  # ← Aquí
        )
    
    def start_pump(self):
        return self.send_command(5)
        
    def stop_pump(self):
        return self.send_command(6)


