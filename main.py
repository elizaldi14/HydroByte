import sys
import os
import platform
import serial
import time
import serial.tools.list_ports
import threading

# Configuración para escalado DPI multiplataforma (esto va ANTES de QApplication)
os.environ["QT_SCALE_FACTOR"] = "1"  # Escala base (puedes ajustar si es necesario)
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

from PySide6.QtGui import QIcon
from app.main_window import HydroponicMonitor
from utils.serial_reader import PumpSerial, read_serial_data
from utils.mock_serial import MockSerial

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

    # Estilos globales
    app.setStyleSheet("""
        QFrame {
            border-radius: 12px;
        }

        QFrame#chartFrame, QFrame#sensorCard {
            background-color: white;
            border: 1px solid #E2E8F0;
            margin: 2px;
        }
    """)

    # Inicializar puerto serial
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

    pump_serial = PumpSerial(serial_conn)

    # Iniciar hilo de lectura
    serial_thread = threading.Thread(target=read_serial_data, args=(serial_conn,), daemon=True)
    serial_thread.start()

    # Crear y mostrar ventana
    window = HydroponicMonitor(pump_serial)

    if isinstance(serial_conn, MockSerial):
        window.mostrar_notificacion(
            title="Serial Desconectado",
            message="No se pudo conectar al puerto serial. Usando modo simulado.",
            status="error"
        )
    elif isinstance(serial_conn, serial.Serial) and serial_conn.is_open:
        window.mostrar_notificacion(
            title="Serial Conectado",
            message="Se ha conectado correctamente a los sensores.",
            status="success"
        )

    # Icono de ventana
    ico_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'utils', 'img', 'logo_pi.ico'))
    png_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'utils', 'img', 'logo_pi.png'))
    if os.path.exists(ico_path):
        window.setWindowIcon(QIcon(ico_path))
    elif os.path.exists(png_path):
        window.setWindowIcon(QIcon(png_path))

    window.showMaximized()
    sys.exit(app.exec())
