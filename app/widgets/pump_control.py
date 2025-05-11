from PySide6.QtWidgets import (QWidget, QVBoxLayout, QLabel, QPushButton, QFrame, QMessageBox)
from PySide6.QtCore import Qt, QObject, Signal
from PySide6.QtGui import QFont, QPixmap
import serial
import time
import threading
import os

class PumpSerial(QObject):
    # Señal para notificar cambios de estado
    status_changed = Signal(str)
    
    def __init__(self, port='COM4', baudrate=9600, timeout=1):
        super().__init__()
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_conn = None
        self.connect()
    
    def connect(self):
        try:
            self.serial_conn = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
            self.status_changed.emit(f"Conectado a {self.port}")
            return True
        except (serial.SerialException, OSError) as e:
            self.serial_conn = None
            self.status_changed.emit(f"Error: No se pudo conectar a {self.port}")
            return False
    
    def write(self, data):
        if self.serial_conn and self.serial_conn.is_open:
            try:
                self.serial_conn.write(data)
                return True
            except (serial.SerialException, OSError):
                self.serial_conn = None
                return False
        return False
    
    def close(self):
        if self.serial_conn and self.serial_conn.is_open:
            self.serial_conn.close()

# Instancia global del controlador serial
pump_serial = PumpSerial()

class PumpCard(QFrame):
    """Clase base abstracta para todas las bombas"""
    def __init__(self, pump_name, theme_manager, img, description, parent=None):
        super().__init__(parent)
        self.theme_manager = theme_manager
        self.pump_name = pump_name
        self.img = img
        self.description = description
        self.thread = None
        self.stop_event = threading.Event()
        self.automation_enabled = False
        self.setup_ui()
        self.apply_theme()
    
    def setup_ui(self):
        self.setObjectName("pumpCard")
        self.setFixedSize(350, 400)

        self.layout = QVBoxLayout(self)
        self.layout.setSpacing(15)

        self.title = QLabel(self.pump_name)
        self.title.setFont(QFont("Segoe UI", 16, QFont.Bold))
        self.title.setAlignment(Qt.AlignCenter) 
        self.layout.addWidget(self.title)
        
        self.description_label = QLabel(self.description)
        self.description_label.setFont(QFont("Segoe UI", 12))
        self.description_label.setAlignment(Qt.AlignCenter) 
        self.layout.addWidget(self.description_label)

         # Icono de la bomba
        iconLabel = QLabel()
        iconLabel.setFixedSize(150, 150)
        iconLabel.setScaledContents(True)
        iconLabel.setAlignment(Qt.AlignCenter)
        iconLabel.setObjectName("iconLabel")
        self.iconLabel = iconLabel

        iconPath = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', '..', 'utils', 'img', self.img)
        )
        print(iconPath)
        if os.path.exists(iconPath):
            iconPixmap = QPixmap(iconPath)
            iconPixmap = iconPixmap.scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            iconLabel.setPixmap(iconPixmap)
        else:
            iconLabel.setText(iconPath[0].upper())
        
        self.layout.addWidget(iconLabel, alignment=Qt.AlignCenter)

        self.status_label = QLabel("Estado: Detenida")
        self.status_label.setFont(QFont("Segoe UI", 14))
        self.layout.addWidget(self.status_label)

        # Create button layout
        self.button_layout = QVBoxLayout()
        
        # Toggle button
        self.toggle_btn = QPushButton("Iniciar")
        self.toggle_btn.setFont(QFont("Segoe UI", 12, QFont.Bold))
        self.toggle_btn.clicked.connect(self.toggle_pump)
        self.button_layout.addWidget(self.toggle_btn)
        
        # Solo agregar botón de automático si no es una bomba de pH
        if not hasattr(self, 'is_ph_pump'):
            self.auto_btn = QPushButton("Modo Manual")
            self.auto_btn.setFont(QFont("Segoe UI", 10))
            self.auto_btn.clicked.connect(self.toggle_automation)
            self.auto_btn.setStyleSheet("""
                QPushButton {
                    background-color: #3B82F6;
                    color: white;
                    border: none;
                    border-radius: 8px;
                    padding: 8px;
                    margin-top: 5px;
                }
                QPushButton:hover {
                    background-color: #2563EB;
                }
            """)
            self.button_layout.addWidget(self.auto_btn)
        
        self.layout.addLayout(self.button_layout)
        
        self.automation_enabled = False
        self.update_button_style(False)

    def apply_theme(self):
        if self.theme_manager.is_dark_mode:
            self.setStyleSheet("""
                QFrame#pumpCard {
                    background: #2D3748;
                    border: 1px solid #4A5568;
                }
                QLabel {
                    color: #E2E8F0;
                }
            """)
        else:
            self.setStyleSheet("""
                QFrame#pumpCard {
                    background: #FFFFFF;
                    border: 1px solid #E2E8F0;
                }
                QLabel {
                    color: #1E293B;
                }
            """)

    def send_command(self, command):
        """Método común para enviar comandos"""
        if pump_serial.write(str(command).encode()):
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
        if self.automation_enabled:
            self.auto_btn.setText("Modo Automático")
            self.auto_btn.setStyleSheet("""
                QPushButton {
                    background-color: #8B5CF6;
                    color: white;
                    border: none;
                    border-radius: 8px;
                    padding: 8px;
                    margin-top: 5px;
                }
                QPushButton:hover {
                    background-color: #7C3AED;
                }
            """)
            # Iniciar la bomba si no está en marcha
            if not (self.thread and self.thread.is_alive()):
                self.toggle_pump(send_stop_command=False)
        else:
            self.auto_btn.setText("Modo Manual")
            self.auto_btn.setStyleSheet("""
                QPushButton {
                    background-color: #3B82F6;
                    color: white;
                    border: none;
                    border-radius: 8px;
                    padding: 8px;
                    margin-top: 5px;
                }
                QPushButton:hover {
                    background-color: #2563EB;
                }
            """)
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
    def __init__(self, theme_manager, parent=None):
        self.is_water_pump = True  # Marcar como bomba de agua
        super().__init__(
            pump_name="Bomba de Circulación",
            theme_manager=theme_manager,
            img="pump_circulacion.png",
            description="Circula el agua en el sistema",
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
    """Bomba peristáltica para aumentar pH"""
    def __init__(self, theme_manager, parent=None):
        self.is_ph_pump = True  # Marcar como bomba de pH
        super().__init__(
            pump_name="Bomba pH+",
            theme_manager=theme_manager,
            img="pump_peristaltica.png",
            description="Aumenta el pH del agua",
            parent=parent
        )
    
    def start_pump(self):
        return self.send_command(3)
        
    def stop_pump(self):
        return self.send_command(4)

class PhDownPump(PumpCard):
    """Bomba peristáltica para disminuir pH"""
    def __init__(self, theme_manager, parent=None):
        self.is_ph_pump = True  # Marcar como bomba de pH
        super().__init__(
            pump_name="Bomba pH-",
            theme_manager=theme_manager,
            img="pump_peristaltica.png",
            description="Disminuye el pH del agua",
            parent=parent
        )
    
    def start_pump(self):
        return self.send_command(5)
        
    def stop_pump(self):
        return self.send_command(6)
