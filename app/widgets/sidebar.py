from PySide6.QtWidgets import (QWidget, QVBoxLayout, QPushButton, 
                              QLabel, QScrollArea, QFrame, QHBoxLayout,QToolTip)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont

class SidebarButton(QPushButton):
    def __init__(self, text, icon_name, tooltip, parent=None, is_submenu=False):
        super().__init__(parent)
        self.setText("")
        self.setToolTip(tooltip)
        self.setCursor(Qt.PointingHandCursor)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(20 if not is_submenu else 35, 0, 20, 0)
        layout.setSpacing(15)

        icon_label = QLabel(icon_name[0].upper())
        icon_label.setFixedSize(30, 30)
        icon_label.setAlignment(Qt.AlignCenter)
        icon_label.setObjectName("iconLabel")
        self.icon_label = icon_label

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
            #iconLabel {{
                background-color: {'#E0F2FE' if not is_submenu else 'transparent'};
                color: {colors['text']};
                font-weight: bold;
                font-size: {"15px" if is_submenu else "16px"};
                border-radius: 8px;
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
        
        # Initialize colors first
        self.colors = {
            'primary': "#FFFFFF",
            'text': "#1E293B",
            'hover': "#F0F9FF",
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

        logo_label = QLabel()
        logo_label.setFixedSize(40, 40)
        logo_label.setAlignment(Qt.AlignCenter)
        logo_label.setText("H")
        logo_label.setObjectName("../drop.png")

        title = QLabel("Sistema Hidropónico")
        title.setObjectName("titleLabel")
        title.setFont(QFont("Segoe UI", 16, QFont.Bold))

        title_layout.addWidget(logo_label)
        title_layout.addWidget(title)

        # Botones principales
        self.home_btn = SidebarButton("Estado", "E", "Ver estado general del sistema")
        self.alerts_btn = SidebarButton("Alertas", "A", "Ver alertas del sistema")

        # Gráficas section as a button
        self.graphs_btn = SidebarButton("Gráficas", "G", "Mostrar/ocultar gráficas")
        self.graphs_btn.setCheckable(True)
        self.graphs_btn.setChecked(True)
        
        # Force main menu styling (overriding any submenu styling)
        self.graphs_btn.apply_theme(self.colors, is_submenu=False)

        # Submenu items
        self.ph_btn = SidebarButton("pH", "pH", "Ver gráfico de pH", is_submenu=True)
        self.ec_btn = SidebarButton("Conductividad Eléctrica", "CE", "Ver gráfico de conductividad", is_submenu=True)
        self.temp_btn = SidebarButton("Temperatura", "T", "Ver gráfico de temperatura", is_submenu=True)
        self.water_btn = SidebarButton("Nivel del Agua", "NA", "Ver gráfico de nivel de agua", is_submenu=True)

        self.help_btn = SidebarButton("Ayudas", "?", "Obtener ayuda")
        self.settings_btn = SidebarButton("Configuración", "C", "Configurar el sistema")
        self.theme_btn = SidebarButton("Cambiar Tema", "T", "Alternar entre modo claro y oscuro")

        # Layout del menú
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
        self.menu_buttons = [self.home_btn, self.alerts_btn, self.help_btn, self.settings_btn, self.theme_btn, self.graphs_btn]
        self.submenu_buttons = [self.ph_btn, self.ec_btn, self.temp_btn, self.water_btn]

        self.graphs_btn.clicked.connect(self.toggle_submenu)
        self.theme_btn.clicked.connect(self.toggle_theme)

    def toggle_submenu(self):
        show = self.graphs_btn.isChecked()
        for button in self.submenu_buttons:
            button.setVisible(show)
        
        # Update button style while preserving theme colors
        if show:
            self.graphs_btn.icon_label.setStyleSheet(f"""
                background-color: #E0F2FE;
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

        colors = self.colors

        self.setStyleSheet(f"""
            QWidget {{
                background-color: {colors['primary']};
            }}
            #sidebar {{
                background-color: {colors['primary']};
                border-right: 1px solid {colors['border']};
            }}
            QScrollArea {{
                background-color: {colors['primary']};
                border: none;
            }}
            QScrollArea > QWidget {{
                background-color: {colors['primary']};
            }}
            #titleContainer {{
                background-color: {colors['primary']};
                border-bottom: 1px solid {colors['border']};
            }}
            #logoLabel {{
                background-color: {colors['secondary']};
                color: {colors['text']};
                border-radius: 20px;
                font-size: 20px;
                font-weight: bold;
            }}
            #titleLabel {{
                color: {colors['text']};
            }}
            #sectionLabel {{
                color: {colors['text']};
            }}
        """)

        for btn in self.menu_buttons:
            btn.apply_theme(colors)

        for btn in self.submenu_buttons:
            btn.apply_theme(colors, is_submenu=True)
