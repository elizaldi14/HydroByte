import sys
from PySide6.QtWidgets import QApplication
from app.main_window import HydroponicMonitor
from PySide6.QtGui import QIcon
import os
import serial
import time
import platform


# Initialize pumps with the serial connection
from utils.serial_reader import PumpSerial
from utils.serial_reader import read_serial_data
import threading

from utils.mock_serial import MockSerial
import serial.tools.list_ports

def find_serial_port():
    system_platform = platform.system()

    ports = serial.tools.list_ports.comports()
    for port in ports:
        if system_platform == "Windows":
            if "COM" in port.device:
                return port.device
        elif system_platform == "Linux":
            if "/dev/ttyUSB" in port.device or "/dev/ttyACM" in port.device:
                return port.device

    return None


if __name__ == "__main__":

    app = QApplication(sys.argv)
    
    # Aplicar estilo global para sombras y efectos
    app.setStyleSheet("""
        QFrame {
            border-radius: 12px;
        }
        
        QFrame#chartFrame, QFrame#sensorCard {
            background-color: white;
            border: 1px solid #E2E8F0;
        }
        
        /* Hack para simular sombras en Qt */
        QFrame#chartFrame, QFrame#sensorCard {
            border: 1px solid #E2E8F0;
            margin: 2px;
        }
    """)
    
    # Crear conexión serial
    try:
        port = find_serial_port()
        if port:
            serial_conn = serial.Serial(port, 9600, timeout=1)
            print(f"[INFO] Conectado al puerto serial real: {port}")
        else:
            raise Exception("No se detectó un puerto serial.")
    except Exception as e:
        print(f"[ADVERTENCIA] {e} Usando conexión serial simulada.")
        serial_conn = MockSerial()
    
    # Crear instancia de PumpSerial
    pump_serial = PumpSerial(serial_conn)
    
    # Iniciar hilo para leer datos del serial
    serial_thread = threading.Thread(target=read_serial_data, args=(serial_conn,), daemon=True)
    serial_thread.start()
    
    # Crear y mostrar la ventana principal con la conexión serial
    window = HydroponicMonitor(pump_serial)
    
    # Mostrar notificación del estado de la conexión
    if isinstance(serial_conn, MockSerial):
        window.mostrar_notificacion(
            title="Serial Desconectado",
            message="No se pudo conectar al puerto serial. Usando modo simulado.",
            status="error"
        )
    elif isinstance(serial_conn, serial.Serial):
        if serial_conn.is_open:
            window.mostrar_notificacion(
                title="Serial Conectado",
                message="Se ha conectado correctamente a los sensores.",
                status="success"
            )
        else:
            window.mostrar_notificacion(
                title="Serial Desconectado",
                message="No se pudo conectar al puerto serial. Usando modo simulado.",
                status="error"
            )
    
    # Usa .ico para Windows taskbar si existe
    ico_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'utils', 'img', 'logo_pi.ico'))
    png_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'utils', 'img', 'logo_pi.png'))
    if os.path.exists(ico_path):
        window.setWindowIcon(QIcon(ico_path))
    elif os.path.exists(png_path):
        window.setWindowIcon(QIcon(png_path))

    window.showMaximized()
    sys.exit(app.exec())