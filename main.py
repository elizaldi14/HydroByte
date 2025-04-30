import sys
from PySide6.QtWidgets import QApplication
from app.main_window import HydroponicMonitor

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
    window.showMaximized()
    sys.exit(app.exec())