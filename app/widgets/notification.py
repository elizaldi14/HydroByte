from PySide6.QtWidgets import QLabel, QWidget, QVBoxLayout, QApplication, QGraphicsDropShadowEffect
from PySide6.QtCore import QTimer, Qt, QPoint, QPropertyAnimation, QEasingCurve, QEvent
from PySide6.QtGui import QColor


class Notification(QWidget):
    def __init__(self, parent, title, message, status, theme_manager, *args, **kwargs):
        """
        Crea una notificación con título, mensaje y estado.

        Args:
            parent (QWidget): Widget padre (ventana principal)
            title (str): Título de la notificación
            message (str): El mensaje a mostrar en la notificación
            status (str): Estado de la notificación ('success', 'warning', 'error', 'info')
            theme_manager (ThemeManager): Administrador de temas para aplicar colores
        """
        super().__init__(parent, *args, **kwargs)
        self.parent_window = parent
        self.theme_manager = theme_manager
        self.status = status
        self.is_application_active = True

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

        parent.installEventFilter(self)
        QApplication.instance().applicationStateChanged.connect(self.on_application_state_changed)

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

        self.adjustSize()
        self.setFixedWidth(320)
        self.setMinimumHeight(80)

        self.apply_color()
        self._position_notification()
        self.fade_in()
        QTimer.singleShot(5000, self.fade_out)

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

    def _position_notification(self):
        """Posiciona la notificación en la esquina superior derecha de la ventana principal."""
        if not self.parent_window:
            return

        parent_rect = self.parent_window.frameGeometry()
        x = parent_rect.right() - self.width() - 20
        y = parent_rect.top() + 20
        global_pos = self.parent_window.mapToGlobal(QPoint(x, y))
        self.move(global_pos)

        if not self.isVisible():
            self.show()

        self.raise_()
        self.activateWindow()

    def eventFilter(self, obj, event):
        """Maneja eventos de movimiento, redimensionamiento y estado de la ventana principal."""
        if obj == self.parent_window:
            if event.type() in [QEvent.Move, QEvent.Resize, QEvent.WindowStateChange]:
                self._position_notification()

                if event.type() == QEvent.WindowStateChange:
                    if self.parent_window.isMinimized():
                        self.hide()
                    elif self.is_application_active:
                        self.show()
        return super().eventFilter(obj, event)

    def on_application_state_changed(self, state):
        """Maneja cambios de estado de la aplicación (activa/inactiva)."""
        is_active = state == Qt.ApplicationActive
        if is_active != self.is_application_active:
            self.is_application_active = is_active
            if is_active and not self.parent_window.isMinimized():
                self.show()
                self._position_notification()
            else:
                self.hide()

    def fade_in(self):
        """Animación de entrada con desvanecimiento y desplazamiento."""
        if not self.is_application_active or (self.parent_window and self.parent_window.isMinimized()):
            return

        self._position_notification()
        self.show()
        self.raise_()

        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(300)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)

        self.pos_animation = QPropertyAnimation(self, b"pos")
        self.pos_animation.setDuration(400)
        self.pos_animation.setEasingCurve(QEasingCurve.OutBack)
        self.pos_animation.setStartValue(QPoint(self.x() + 50, self.y()))
        self.pos_animation.setEndValue(QPoint(self.x(), self.y()))

        self.animation.start()
        self.pos_animation.start()

    def fade_out(self):
        """Animación de salida con desvanecimiento y cierre al terminar."""
        self.fade_out_animation = QPropertyAnimation(self, b"windowOpacity")
        self.fade_out_animation.setDuration(300)
        self.fade_out_animation.setStartValue(1)
        self.fade_out_animation.setEndValue(0)
        self.fade_out_animation.finished.connect(self.close)
        self.fade_out_animation.start()


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
