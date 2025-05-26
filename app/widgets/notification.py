from PySide6.QtWidgets import QLabel, QWidget, QVBoxLayout, QApplication, QGraphicsDropShadowEffect
from PySide6.QtCore import QTimer, Qt, QPoint, QPropertyAnimation, QEasingCurve, QEvent
from PySide6.QtGui import QColor

class Notification(QWidget):
    def __init__(self, parent, title, message, status, *args, **kwargs):
        """
        Crea una notificación con título, mensaje y estado.
        
        Args:
            parent (QWidget): Widget padre (ventana principal)
            title (str): Título de la notificación
            message (str): El mensaje a mostrar en la notificación
            status (str): Estado de la notificación ('success', 'warning', 'error', 'info')
        """
        super().__init__(parent, *args, **kwargs)
        self.parent_window = parent
        self.is_application_active = True  # Track application active state
        
        # Configuración básica de la ventana
        self.setWindowFlags(
            Qt.Window |
            Qt.FramelessWindowHint |
            Qt.Tool |
            Qt.WindowStaysOnTopHint |
            Qt.WindowDoesNotAcceptFocus
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_ShowWithoutActivating)
        self.setAttribute(Qt.WA_QuitOnClose, False)
        
        # Conectar señales de la ventana principal
        parent.installEventFilter(self)
        
        # Monitorear cambios de estado de la aplicación
        QApplication.instance().applicationStateChanged.connect(self.on_application_state_changed)
        
        # Configurar el estilo base
        status_color = self._get_status_color(status)
        
        # Crear un widget contenedor principal
        container = QWidget(self)
        container.setObjectName("container")
        
        # Configurar el layout principal
        layout = QVBoxLayout(container)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(8)
        
        # Crear y configurar el título
        self.title_label = QLabel(title, container)
        self.title_label.setStyleSheet(self._get_title_style(status))
        
        # Crear y configurar el mensaje
        self.message_label = QLabel(message, container)
        self.message_label.setStyleSheet(self._get_message_style())
        self.message_label.setWordWrap(True)
        
        # Añadir widgets al layout
        layout.addWidget(self.title_label)
        layout.addWidget(self.message_label)
        
        # Configurar el layout principal
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(container)
        
        # Ajustar tamaño
        self.adjustSize()
        self.setFixedWidth(320)
        self.setMinimumHeight(80)
        
        # Estilo del contenedor principal
        self.setStyleSheet(f"""
            #container {{
                background-color: #FFFFFF;
                border-radius: 8px;
                border-left: 4px solid {status_color};
                padding: 0px;
            }}
            
            QLabel#title {{
                font-weight: bold;
                font-size: 14px;
                color: #333333;
                margin: 0;
                padding: 0;
            }}
            
            QLabel#message {{
                color: #555555;
                font-size: 13px;
                margin: 0;
                padding: 4px 0 0 0;
            }}
        """)
        
        # Sombra
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setColor(QColor(0, 0, 0, 60))
        shadow.setOffset(0, 2)
        self.setGraphicsEffect(shadow)
        
        # Posicionar y mostrar con animación
        self._position_notification()
        self.fade_in()

        # Configuración del estilo base
        status_color = self._get_status_color(status)
        
        # Crear un widget contenedor principal
        container = QWidget(self)
        container.setObjectName("container")
        
        # Configurar el layout principal
        layout = QVBoxLayout(container)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(8)
        
        # Crear y configurar el título
        self.title_label = QLabel(title, container)
        self.title_label.setStyleSheet(self._get_title_style(status))
        
        # Crear y configurar el mensaje
        self.message_label = QLabel(message, container)
        self.message_label.setStyleSheet(self._get_message_style())
        self.message_label.setWordWrap(True)
        
        # Añadir widgets al layout
        layout.addWidget(self.title_label)
        layout.addWidget(self.message_label)
        
        # Configurar el layout principal
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(container)
        
        # Ajustar tamaño
        self.adjustSize()
        self.setFixedWidth(320)
        self.setMinimumHeight(80)
        
        # Estilo del contenedor principal
        self.setStyleSheet(f"""
            #container {{
                background-color: #FFFFFF;
                border-radius: 8px;
                border-left: 4px solid {status_color};
                padding: 0px;
            }}
            
            QLabel#title {{
                font-weight: bold;
                font-size: 14px;
                color: #333333;
                margin: 0;
                padding: 0;
            }}
            
            QLabel#message {{
                color: #555555;
                font-size: 13px;
                margin: 0;
                padding: 4px 0 0 0;
            }}
        """)
        
        # Sombra
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setColor(QColor(0, 0, 0, 60))
        shadow.setOffset(0, 2)
        self.setGraphicsEffect(shadow)
        
        # Posicionar y mostrar con animación
        # Cerrar automáticamente después de 5 segundos
        QTimer.singleShot(5000, self.fade_out)

    def _get_status_color(self, status):
        """Obtiene el color correspondiente al estado"""
        colors = {
            'success': '#4CAF50',
            'warning': '#FFC107',
            'error': '#F44336',
            'info': '#2196F3'
        }
        return colors.get(status, '#2196F3')
    
    def _get_title_style(self, status):
        """Obtiene el estilo para el título basado en el estado"""
        styles = {
            'success': 'color: #4CAF50;',
            'warning': 'color: #FFC107;',
            'error': 'color: #F44336;',
            'info': 'color: #2196F3;'
        }
        return styles.get(status, 'color: #2196F3;')
    
    def _get_message_style(self) -> str:
        """Devuelve el estilo CSS para el mensaje"""
        return """
            color: #333333;
            font-family: 'Segoe UI', Arial, sans-serif;
            font-size: 13px;
            margin: 0;
            padding: 0;
            padding-top: 4px;
        """

    def _position_notification(self):
        """Posiciona la notificación en la esquina superior derecha de la ventana principal"""
        if not self.parent_window:
            return
            
        # Obtener la geometría de la ventana principal
        parent_rect = self.parent_window.frameGeometry()
        
        # Calcular la posición X (20px desde el borde derecho de la ventana principal)
        x = parent_rect.right() - self.width() - 20
        
        # Calcular la posición Y (20px desde el borde superior de la ventana principal)
        y = parent_rect.top() + 20
        
        # Convertir las coordenadas a coordenadas globales
        global_pos = self.parent_window.mapToGlobal(QPoint(x, y))
        
        # Mover la notificación a la posición calculada
        self.move(global_pos)
        
        # Mostrar la notificación si no está visible
        if not self.isVisible():
            self.show()
        
        # Asegurarse de que la notificación esté en la parte superior
        self.raise_()
        self.activateWindow()
    
    def eventFilter(self, obj, event):
        """Maneja los eventos de la ventana principal"""
        if obj == self.parent_window:
            if event.type() in [QEvent.Move, QEvent.Resize, QEvent.WindowStateChange]:
                self._position_notification()
                
                # Ocultar notificaciones si la ventana se minimiza
                if event.type() == QEvent.WindowStateChange:
                    if self.parent_window.isMinimized():
                        self.hide()
                    elif self.is_application_active:
                        self.show()
                        
        return super().eventFilter(obj, event)
        
    def on_application_state_changed(self, state):
        """Maneja los cambios de estado de la aplicación"""
        # Verificar si la aplicación está activa (en primer plano)
        is_active = state == Qt.ApplicationActive
        
        if is_active != self.is_application_active:
            self.is_application_active = is_active
            
            if is_active:
                # Si la aplicación vuelve a estar activa, mostrar la notificación
                if not self.parent_window.isMinimized():
                    self.show()
                    self._position_notification()
            else:
                # Si la aplicación pierde el foco, ocultar la notificación
                self.hide()

    def fade_in(self):
        """Animación de entrada con desvanecimiento"""
        if not self.is_application_active or (self.parent_window and self.parent_window.isMinimized()):
            return
            
        self._position_notification()
        self.show()
        self.raise_()
        
        # Configurar la animación de opacidad
        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(300)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        
        # Animación de posición (deslizamiento desde la derecha)
        self.pos_animation = QPropertyAnimation(self, b"pos")
        self.pos_animation.setDuration(400)
        self.pos_animation.setEasingCurve(QEasingCurve.OutBack)
        
        # Posición inicial fuera de la pantalla a la derecha
        start_x = self.x() + 50
        self.pos_animation.setStartValue(QPoint(start_x, self.y()))
        self.pos_animation.setEndValue(QPoint(self.x(), self.y()))
        
        # Iniciar animaciones
        self.animation.start()
        self.pos_animation.start()
    
    def fade_out(self):
        """Animación de salida con desvanecimiento"""
        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(500)
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        
        # Animación de posición al salir
        self.pos_animation = QPropertyAnimation(self, b"pos")
        self.pos_animation.setDuration(500)
        self.pos_animation.setEasingCurve(QEasingCurve.InBack)
        
        end_pos = QPoint(self.x() + 100, self.y())
        self.pos_animation.setStartValue(QPoint(self.x(), self.y()))
        self.pos_animation.setEndValue(end_pos)
        
        # Cerrar la notificación cuando termine la animación
        self.animation.finished.connect(self.close)
        
        self.animation.start()
        self.pos_animation.start()

# Ejemplo de uso
if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
    
    def show_notification():
        notification = Notification("¡Operación completada con éxito!", "success")
    
    app = QApplication(sys.argv)
    
    # Crear ventana de prueba
    window = QWidget()
    layout = QVBoxLayout()
    
    btn = QPushButton("Mostrar notificación")
    btn.clicked.connect(show_notification)
    
    layout.addWidget(btn)
    window.setLayout(layout)
    window.show()
    
    sys.exit(app.exec())
