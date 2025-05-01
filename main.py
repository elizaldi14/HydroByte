import sys
from PySide6.QtWidgets import QApplication
from app.main_window import HydroponicMonitor
from PySide6.QtGui import QIcon
import os

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
    
    window = HydroponicMonitor()
    # Usa .ico para Windows taskbar si existe
    ico_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'utils', 'img', 'logo_pi.ico'))
    png_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'utils', 'img', 'logo_pi.png'))
    if os.path.exists(ico_path):
        window.setWindowIcon(QIcon(ico_path))
    elif os.path.exists(png_path):
        window.setWindowIcon(QIcon(png_path))
    window.showMaximized()
    sys.exit(app.exec())