from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QLabel, QScrollArea,
    QFrame, QHBoxLayout, QToolTip
)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont, QPixmap
import os

class SidebarButton(QPushButton):
    def __init__(self, text, icon_name, tooltip, parent=None, is_submenu=False):
        super().__init__(parent)
        self.setText("")
        self.setToolTip(tooltip)
        self.setCursor(Qt.PointingHandCursor)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(20 if not is_submenu else 35, 0, 20, 0)
        layout.setSpacing(15)

        icon_label = QLabel()
        icon_label.setFixedSize(30, 30)
        icon_label.setScaledContents(True)
        icon_label.setAlignment(Qt.AlignCenter)
        icon_label.setObjectName("iconLabel")
        self.icon_label = icon_label

        icon_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', '..', 'utils', 'img', icon_name)
        )
        if os.path.exists(icon_path):
            pixmap = QPixmap(icon_path)
            if not pixmap.isNull():
                pixmap = pixmap.scaled(30, 30, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                icon_label.setPixmap(pixmap)
            else:
                icon_label.setText(icon_name[0].upper())
        else:
            icon_label.setText(icon_name[0].upper())

        text_label = QLabel(text)
        text_label.setObjectName("textLabel")
        self.text_label = text_label

        layout.addWidget(icon_label)
        layout.addWidget(text_label, 1)

        self.setFixedHeight(56 if not is_submenu else 44)
        QToolTip.setFont(QFont("Segoe UI", 10))

    def apply_theme(self, colors, is_submenu=False):
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {colors['primary']};
                border: none;
                text-align: left;
                padding: 0px;
                border-radius: 8px;
                margin: 4px 8px;
            }}
            QPushButton:hover {{
                background-color: {colors['hover']};
            }}
            QPushButton:hover #iconLabel {{
                background-color: {colors['hover']};
                border-radius: {"8px" if not is_submenu else "15px"};
            }}
            QPushButton:hover #textLabel {{
                color: {colors['hover_text']};
            }}
            #iconLabel {{
                background-color: {'#E0F2FE' if not is_submenu else 'transparent'};
                color: {colors['text']};
                font-weight: bold;
                font-size: {"15px" if is_submenu else "16px"};
                border-radius: {"8px" if not is_submenu else "15px"};
                padding: 4px;
            }}
            #textLabel {{
                color: {colors['text']};
                font-size: {"14px" if is_submenu else "15px"};
                font-weight: {"500" if is_submenu else "600"};
                font-family: 'Segoe UI', sans-serif;
            }}
        """)

class Sidebar(QWidget):
    toggle_submenu_signal = Signal(bool)

    def __init__(self, theme_manager=None, parent=None):
        super().__init__(parent)
        self.theme_manager = theme_manager
        self.dark_mode = False

        self.colors = {
            'primary': "#FFFFFF",
            'text': "#1E293B",
            'hover': "#E0FFE",
            'hover_text': "#0F172A",
            'border': "#E2E8F0",
            'secondary': "#F0F2F5"
        }

        self.setup_ui()
        self.apply_theme()

    def setup_ui(self):
        self.setFixedWidth(300)
        self.setObjectName("sidebar")

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(12, 12, 12, 12)
        main_layout.setSpacing(8)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFrameShape(QFrame.NoFrame)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setObjectName("scrollArea")

        menu_widget = QWidget()
        menu_layout = QVBoxLayout(menu_widget)
        menu_layout.setContentsMargins(0, 0, 0, 0)
        menu_layout.setSpacing(0)

        title_container = QWidget()
        title_container.setFixedHeight(70)
        title_container.setObjectName("titleContainer")

        title_layout = QHBoxLayout(title_container)
        title_layout.setContentsMargins(15, 0, 15, 0)

        logo_label = QLabel("H")
        logo_label.setFixedSize(40, 40)
        logo_label.setAlignment(Qt.AlignCenter)
        logo_label.setObjectName("logoLabel")

        title = QLabel("Sistema Hidropónico")
        title.setObjectName("titleLabel")
        title.setFont(QFont("Segoe UI", 16, QFont.Bold))

        title_layout.addWidget(logo_label)
        title_layout.addWidget(title)

        self.home_btn = SidebarButton("Estado", "menu_black.svg", "Ver estado general del sistema")
        self.alerts_btn = SidebarButton("Alertas", "notifications_black.svg", "Ver alertas del sistema")

        self.graphs_btn = SidebarButton("Gráficas", "timeline_black.svg", "Mostrar/ocultar gráficas")
        self.graphs_btn.setCheckable(True)
        self.graphs_btn.setChecked(False)
        self.graphs_btn.apply_theme(self.colors, is_submenu=False)

        self.ph_btn = SidebarButton("pH", "ph_black.png", "Ver gráfico de pH", is_submenu=True)
        self.ec_btn = SidebarButton("Conductividad Eléctrica", "settings_black.svg", "Ver gráfico de conductividad", is_submenu=True)
        self.temp_btn = SidebarButton("Temperatura", "temperatura_black.png", "Ver gráfico de temperatura", is_submenu=True)
        self.water_btn = SidebarButton("Nivel del Agua", "nivelAgua_black.png", "Ver gráfico de nivel de agua", is_submenu=True)

        for btn in [self.ph_btn, self.ec_btn, self.temp_btn, self.water_btn]:
            btn.setVisible(False)

        self.help_btn = SidebarButton("Ayudas", "help_black.svg", "Obtener ayuda")
        self.settings_btn = SidebarButton("Configuración", "settings_black.svg", "Configurar el sistema")
        self.theme_btn = SidebarButton("Cambiar Tema", "tema_black.png", "Alternar entre modo claro y oscuro")

        menu_layout.addWidget(title_container)
        menu_layout.addWidget(self.home_btn)
        menu_layout.addWidget(self.alerts_btn)
        menu_layout.addWidget(self.graphs_btn)
        menu_layout.addWidget(self.ph_btn)
        menu_layout.addWidget(self.ec_btn)
        menu_layout.addWidget(self.temp_btn)
        menu_layout.addWidget(self.water_btn)
        menu_layout.addWidget(self.help_btn)
        menu_layout.addWidget(self.settings_btn)
        menu_layout.addStretch()
        menu_layout.addWidget(self.theme_btn)

        scroll_area.setWidget(menu_widget)
        main_layout.addWidget(scroll_area)

        self.title = title
        self.logo_label = logo_label
        self.menu_buttons = [
            self.home_btn, self.alerts_btn, self.graphs_btn,
            self.help_btn, self.settings_btn, self.theme_btn
        ]
        self.submenu_buttons = [
            self.ph_btn, self.ec_btn, self.temp_btn, self.water_btn
        ]

        self.graphs_btn.clicked.connect(self.toggle_submenu)
        self.theme_btn.clicked.connect(self.toggle_theme)

    def toggle_submenu(self):
        show = self.graphs_btn.isChecked()
        for button in self.submenu_buttons:
            button.setVisible(show)
        if show:
            self.graphs_btn.icon_label.setStyleSheet(f"""
                background-color: #E0FFE;
                color: {self.colors['text']};
                font-weight: bold;
                font-size: 16px;
                border-radius: 8px;
                padding: 4px;
            """)
        else:
            self.graphs_btn.apply_theme(self.colors, is_submenu=False)

    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        self.apply_theme()

    def apply_theme(self):
        if self.dark_mode:
            self.colors = {
                'primary': "#1E293B",
                'text': "#F8FAFC",
                'hover': "#334155",
                'hover_text': "#BFDBFE",
                'border': "#334155",
                'secondary': "#0F172A"
            }
        else:
            self.colors = {
                'primary': "#FFFFFF",
                'text': "#1E293B",
                'hover': "#F0F9FF",
                'hover_text': "#0F172A",
                'border': "#E2E8F0",
                'secondary': "#F0F2F5"
            }

        self.setStyleSheet(f"""
            QWidget {{
                background-color: {self.colors['primary']};
            }}
            #sidebar {{
                background-color: {self.colors['primary']};
                border-right: 1px solid {self.colors['border']};
            }}
            QScrollArea {{
                background-color: {self.colors['primary']};
                border: none;
            }}
            QScrollArea > QWidget {{
                background-color: {self.colors['primary']};
            }}
            #titleContainer {{
                background-color: {self.colors['primary']};
                border-bottom: 1px solid {self.colors['border']};
            }}
            #logoLabel {{
                background-color: {self.colors['secondary']};
                color: {self.colors['text']};
                border-radius: 8px;
                font-size: 20px;
                font-weight: bold;
            }}
            #titleLabel {{
                color: {self.colors['text']};
            }}
        """)

        for btn in self.menu_buttons:
            btn.apply_theme(self.colors)

        for btn in self.submenu_buttons:
            btn.apply_theme(self.colors, is_submenu=True)
