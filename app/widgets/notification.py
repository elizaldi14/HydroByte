from PySide6.QtWidgets import QLabel, QWidget, QVBoxLayout, QApplication, QGraphicsDropShadowEffect
from PySide6.QtCore import QTimer, Qt, QPoint, QPropertyAnimation, QEasingCurve, QEvent, Signal
from PySide6.QtGui import QColor


class NotificationManager:
    """Maneja una cola de notificaciones para mostrarlas en orden."""
    def __init__(self):
        self.queue = []
        self.is_showing = False

    def add_notification(self, notification):
        """Añade una notificación a la cola."""
        self.queue.append(notification)
        if not self.is_showing:
            self.show_next()

    def show_next(self):
        """Muestra la siguiente notificación en la cola."""
        if self.queue:
            self.is_showing = True
            notification = self.queue.pop(0)
            notification.finished.connect(self.on_notification_finished)
            notification.show_notification()
        else:
            self.is_showing = False

    def on_notification_finished(self):
        """Llamado cuando una notificación termina de mostrarse."""
        self.show_next()


class Notification(QWidget):
    finished = Signal()  # Señal para indicar que la notificación terminó

    def __init__(self, parent, title, message, status, theme_manager, *args, **kwargs):
        """
        Crea una notificación con título, mensaje y estado.
        """
        super().__init__(parent, *args, **kwargs)
        self.parent_window = parent
        self.theme_manager = theme_manager
        self.status = status
        self.is_application_active = True

        # Configurar flags y atributos
        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.WindowTransparentForInput |
            Qt.WindowDoesNotAcceptFocus
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_ShowWithoutActivating)
        self.setAttribute(Qt.WA_QuitOnClose, False)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)

        # Asegurar que el widget esté en la parte superior
        self.setWindowModality(Qt.NonModal)
        self.setParent(parent)
        parent.installEventFilter(self)

        # Crear widget contenedor y layout
        self.container = QWidget(self)
        self.container.setObjectName("container")
        layout = QVBoxLayout(self.container)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(8)

        # Título
        self.title_label = QLabel(title, self.container)
        self.title_label.setObjectName("title")
        layout.addWidget(self.title_label)

        # Mensaje
        self.message_label = QLabel(message, self.container)
        self.message_label.setObjectName("message")
        self.message_label.setWordWrap(True)
        layout.addWidget(self.message_label)

        # Layout principal
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(self.container)

        # Configurar tamaño
        self.setFixedWidth(320)
        self.setMinimumHeight(80)
        self.setMaximumHeight(120)

        # Asegurar que el widget tenga el tamaño correcto
        self.ensurePolished()
        self.adjustSize()
        # self.raise_()  # Asegurar que esté en la parte superior
        # self.show()  # Mostrar explícitamente

        self.apply_color()

    def apply_color(self):
        """Aplica el tema actual (claro u oscuro) a la notificación."""
        colors = self.theme_manager.get_colors()
        status_color = self._get_status_color(self.status)
        self.setStyleSheet(f"""
            #container {{
                background-color: {colors['notification']};
                border-radius: 8px;
                border-left: 4px solid {status_color};
            }}
            QLabel#title {{
                font-weight: bold;
                font-size: 14px;
                color: {colors['text']};
                margin: 0;
                padding: 0;
            }}
            QLabel#message {{
                color: {colors['text_secondary']};
                font-size: 13px;
                margin: 0;
                padding: 4px 0 0 0;
            }}
        """)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setColor(QColor(0, 0, 0, 60))
        shadow.setOffset(0, 2)
        self.setGraphicsEffect(shadow)

    def _get_status_color(self, status):
        """Obtiene el color correspondiente al estado."""
        colors = {
            'success': '#4CAF50',
            'warning': '#FFC107',
            'error': '#F44336',
            'info': '#2196F3'
        }
        return colors.get(status, '#2196F3')

    def show_notification(self):
        """Muestra la notificación con animación de entrada."""
        # Asegurarse de que el widget esté completamente inicializado
        self.ensurePolished()
        
        # Posicionar la notificación
        self._position_notification()
        
        # Animar siempre que se muestra
        self.fade_in()
        QTimer.singleShot(5000, self.fade_out)


    def _position_notification(self):
        """Posiciona la notificación en la esquina superior derecha de la ventana principal."""
        if not self.parent_window:
            return

        # Obtener la geometría de la ventana principal
        parent_rect = self.parent_window.geometry()
        
        # Calcular la posición en la esquina superior derecha
        x = parent_rect.x() + parent_rect.width() - self.width() - 20
        y = parent_rect.y() + 20
        
        # Asegurarse de que el widget esté completamente inicializado
        self.ensurePolished()
        
        # Mover la notificación a la posición calculada
        self.move(x, y)
        self.raise_()  # Asegurar que esté en la parte superior
        self.activateWindow()  # Activar la ventana
        self.show()  # Mostrar explícitamente# Mostrar explícitamente

    def fade_in(self):
        """Animación de entrada con desvanecimiento y deslizamiento."""
        # Asegurarse de que el widget esté completamente inicializado
        self.ensurePolished()
        
        # Crear animación de posición (deslizamiento desde la derecha)
        self.position_animation = QPropertyAnimation(self, b"pos")
        self.position_animation.setDuration(400)
        self.position_animation.setEasingCurve(QEasingCurve.OutBack)

        # Obtener la geometría de la ventana principal
        parent_rect = self.parent_window.geometry()
        
        # Calcular posiciones
        start_x = parent_rect.right() + 20  # Posición inicial fuera de la pantalla
        start_y = parent_rect.top() + 20
        end_x = parent_rect.right() - self.width() - 20  # Posición final
        end_y = parent_rect.top() + 20

        # Configurar la animación de posición
        self.position_animation.setStartValue(QPoint(start_x, start_y))
        self.position_animation.setEndValue(QPoint(end_x, end_y))
        
        # Configurar animación de opacidad
        self.opacity_animation = QPropertyAnimation(self, b"windowOpacity")
        self.opacity_animation.setDuration(400)
        self.opacity_animation.setStartValue(0)
        self.opacity_animation.setEndValue(1)

        # Mostrar el widget antes de iniciar las animaciones
        self.show()
        
        # Iniciar ambas animaciones
        self.position_animation.start()
        self.opacity_animation.start()

    def fade_out(self):
        """Animación de salida con desvanecimiento y cierre al terminar."""
        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(300)
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        self.animation.finished.connect(self.close_notification)
        self.animation.start()

    def close_notification(self):
        """Cierra la notificación y emite la señal de finalización."""
        self.close()
        self.finished.emit()
        
        # Limpiar la referencia en el padre si existe
        if self.parent_window:
            if hasattr(self.parent_window, '_current_notification'):
                self.parent_window._current_notification = None


# Ejemplo de uso
if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
    
    def show_notification():
        notification = Notification("¡Operación completada con éxito!", "success")
        notification_manager.add_notification(notification)
    
    app = QApplication(sys.argv)
    
    # Crear ventana de prueba
    window = QWidget()
    layout = QVBoxLayout()
    
    btn = QPushButton("Mostrar notificación")
    btn.clicked.connect(show_notification)
    
    layout.addWidget(btn)
    window.setLayout(layout)
    window.show()
    
    # Crear y mostrar el administrador de notificaciones
    notification_manager = NotificationManager()
    
    sys.exit(app.exec())
