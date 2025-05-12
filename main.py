import sys
from PySide6.QtWidgets import QApplication
from app.main_window import HydroponicMonitor
from PySide6.QtGui import QIcon
import os
import serial
import time

# Initialize pumps with the serial connection
from utils.serial_reader import PumpSerial
from utils.serial_reader import read_serial_data
import threading

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
    
    # Create serial connection
    try:
        serial_conn = serial.Serial('COM4', 9600, timeout=1)
        time.sleep(2)  # Wait for connection to stabilize
        print(f"Connected to {serial_conn.port}")
    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
        sys.exit(1)
    
    # Create PumpSerial instance
    pump_serial = PumpSerial(serial_conn)
    
    # Start serial reader thread
    serial_thread = threading.Thread(target=read_serial_data, args=(serial_conn,), daemon=True)
    serial_thread.start()
    
    # Create and show main window with serial connection
    window = HydroponicMonitor(pump_serial)
    # Usa .ico para Windows taskbar si existe
    ico_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'utils', 'img', 'logo_pi.ico'))
    png_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'utils', 'img', 'logo_pi.png'))
    if os.path.exists(ico_path):
        window.setWindowIcon(QIcon(ico_path))
    elif os.path.exists(png_path):
        window.setWindowIcon(QIcon(png_path))

    window.showMaximized()
    sys.exit(app.exec())