from PySide6.QtWidgets import QLabel, QWidget, QVBoxLayout
from PySide6.QtCore import QTimer, Qt, QPoint, QPropertyAnimation, QEasingCurve

class Notification(QWidget):
    def __init__(self, parent, message, type):
        super().__init__(parent)

        if not isinstance(parent, QWidget):
            print(f"Error: Parent is not a QWidget (got {type(parent)})")
            return

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_ShowWithoutActivating)

        # Estilizar mensaje
        self.message_label = QLabel(message, self)
        self.message_label.setStyleSheet(self.get_style(type))

        layout = QVBoxLayout(self)
        layout.addWidget(self.message_label)
        self.setLayout(layout)

        self.adjustSize()
        self.setFixedWidth(300)  # Hacerla más grande
        self.position_notification(parent)
        self.fade_in()  # Animación de aparición

        # Animación de desaparición
        QTimer.singleShot(3000, self.fade_out) 

    def get_style(self, type):
        styles = {
            "success": """
                background-color: #4CAF50; 
                color: white; 
                padding: 15px; 
                border-radius: 8px;
                font-family: 'Segoe UI';
                font-size: 14px;
            """,
            "warning": """
                background-color: #FFC107; 
                color: black; 
                padding: 15px;
                border-radius: 8px;
                font-family: 'Segoe UI';
                font-size: 14px;
            """,
            "error": """
                background-color: #F44336; 
                color: white; 
                padding: 15px;
                border-radius: 8px;
                font-family: 'Segoe UI';
                font-size: 14px;
            """
        }
        return styles.get(type.lower(), """
            background-color: #555; 
            color: white; 
            padding: 15px;
            border-radius: 8px;
            font-family: 'Segoe UI';
            font-size: 14px;
        """)

    def position_notification(self, parent):
        if not parent.isVisible():
            QTimer.singleShot(100, lambda: self.position_notification(parent))
            return

        # Get the available geometry of the parent window (excluding any slide menus)
        available_geo = parent.rect()
        print(f"Parent rect: {available_geo}")
        print(f"Notification width: {self.width()}")
        
        # Calculate position relative to parent's visible area
        x = available_geo.right() - self.width() - 20
        y = available_geo.top() + 20

        # Convert to global coordinates
        global_pos = parent.mapToGlobal(QPoint(x, y))
        
        self.move(global_pos)
        self.show()
        self.raise_()

    def fade_in(self):
        """Animación de entrada suave con deslizamiento"""
        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(300)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        
        # Animación de posición (deslizamiento desde el borde)
        self.pos_animation = QPropertyAnimation(self, b"pos")
        self.pos_animation.setDuration(400)
        self.pos_animation.setEasingCurve(QEasingCurve.OutBack)
        
        start_pos = QPoint(self.x() + 50 if self.parent().width() > 800 else self.x() + 20, 
                          self.y())
        self.pos_animation.setStartValue(start_pos)
        self.pos_animation.setEndValue(QPoint(self.x(), self.y()))
        
        self.animation.start()
        self.pos_animation.start()
    
    def fade_out(self):
        """Animación de salida con desvanecimiento y deslizamiento"""
        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(500)
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        
        # Animación de posición al salir
        self.pos_animation = QPropertyAnimation(self, b"pos")
        self.pos_animation.setDuration(500)
        self.pos_animation.setEasingCurve(QEasingCurve.InBack)
        
        end_pos = QPoint(self.x() + 100 if self.parent().width() > 800 else self.x() + 50, 
                        self.y())
        self.pos_animation.setStartValue(QPoint(self.x(), self.y()))
        self.pos_animation.setEndValue(end_pos)
        
        # Conectar señal de finalización para cerrar la notificación
        self.animation.finished.connect(self.close)
        
        self.animation.start()
        self.pos_animation.start()
