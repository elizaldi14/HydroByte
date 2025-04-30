from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, 
                              QHBoxLayout, QPushButton, QLabel, QStackedWidget,
                              QFrame, QApplication)
from PySide6.QtCore import Qt, QTimer, Slot
from PySide6.QtGui import QFont, QIcon

from app.theme_manager import ThemeManager
from app.widgets.sidebar import Sidebar
from app.widgets.sensor_card import SensorCard
from app.widgets.chart_widget import ChartWidget
from utils.data_generator import DataGenerator
from utils.constants import LIGHT_COLORS

class HydroponicMonitor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.theme_manager = ThemeManager()
        self.data_generator = DataGenerator()
        
        self.setup_ui()
        self.setup_data()
        self.apply_theme()
        
        # Configurar temporizador para actualizar datos
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_data)
        self.timer.start(3000)  # Actualizar cada 3 segundos
        
    def setup_ui(self):
        self.setWindowTitle("Sistema Hidropónico - Dashboard")
        self.resize(1200, 800)
        self.setObjectName("mainWindow")
        
        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout principal
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Sidebar
        self.sidebar = Sidebar(self.theme_manager, self)
        self.sidebar.theme_btn.clicked.connect(self.toggle_theme)
        
        # Conectar señales de navegación
        self.sidebar.home_btn.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        self.sidebar.alerts_btn.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        self.sidebar.ph_btn.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))
        self.sidebar.ec_btn.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(3))
        self.sidebar.temp_btn.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(4))
        self.sidebar.water_btn.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(5))
        self.sidebar.help_btn.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(6))
        self.sidebar.settings_btn.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(7))
        
        # Contenido principal
        content = QWidget()
        content.setObjectName("contentArea")
        content_layout = QVBoxLayout(content)
        content_layout.setContentsMargins(20, 20, 20, 20)
        content_layout.setSpacing(20)
        
        # Stacked Widget para las diferentes páginas
        self.stacked_widget = QStackedWidget()
        
        # Página de inicio (Estado)
        home_page = QWidget()
        home_layout = QVBoxLayout(home_page)
        home_layout.setContentsMargins(0, 0, 0, 0)
        home_layout.setSpacing(20)
        
        # Título de la página
        page_title = QLabel("Panel de Control")
        page_title.setFont(QFont("Segoe UI", 24, QFont.Bold))
        page_title.setObjectName("pageTitle")
        home_layout.addWidget(page_title)
        
        # Tarjetas de sensores
        sensors_widget = QWidget()
        sensors_layout = QHBoxLayout(sensors_widget)
        sensors_layout.setContentsMargins(0, 0, 0, 0)
        sensors_layout.setSpacing(20)
        
        self.ph_card = SensorCard("pH", 6.3, "", "5.5 - 6.5", LIGHT_COLORS["ph_color"], self.theme_manager, self)
        self.ec_card = SensorCard("Conductividad (EC)", 1.7, "mS/cm", "1.5 - 2.2 mS/cm", LIGHT_COLORS["ec_color"], self.theme_manager, self)
        self.temp_card = SensorCard("Temperatura", 22, "°C", "18 - 24 °C", LIGHT_COLORS["temp_color"], self.theme_manager, self)
        self.water_card = SensorCard("Nivel del Agua", 85, "%", "70 - 90 %", "#9333EA", self.theme_manager, self)
        
        sensors_layout.addWidget(self.ph_card)
        sensors_layout.addWidget(self.ec_card)
        sensors_layout.addWidget(self.temp_card)
        sensors_layout.addWidget(self.water_card)
        
        home_layout.addWidget(sensors_widget)
        
        # Gráficos en la página de inicio
        self.realtime_chart_container = QWidget()
        realtime_layout = QVBoxLayout(self.realtime_chart_container)
        realtime_layout.setContentsMargins(0, 0, 0, 0)
        realtime_layout.addWidget(QLabel("Cargando gráfico..."))  # Placeholder
        
        home_layout.addWidget(self.realtime_chart_container)
        
        # Página de alertas
        alerts_page = QWidget()
        alerts_layout = QVBoxLayout(alerts_page)
        
        alerts_title = QLabel("Alertas del Sistema")
        alerts_title.setFont(QFont("Segoe UI", 24, QFont.Bold))
        alerts_title.setObjectName("pageTitle")
        
        no_alerts = QLabel("No hay alertas activas")
        no_alerts.setFont(QFont("Segoe UI", 16))
        no_alerts.setAlignment(Qt.AlignCenter)
        
        alerts_layout.addWidget(alerts_title)
        alerts_layout.addWidget(no_alerts)
        alerts_layout.addStretch()
        
        # Páginas para cada tipo de gráfico
        ph_page = self.create_chart_page("Monitoreo de pH", "ph")
        ec_page = self.create_chart_page("Monitoreo de Conductividad Eléctrica", "ec")
        temp_page = self.create_chart_page("Monitoreo de Temperatura", "temp")
        water_page = self.create_chart_page("Monitoreo de Nivel de Agua", "water")
        
        # Páginas de ayuda y configuración
        help_page = QWidget()
        help_layout = QVBoxLayout(help_page)
        
        help_title = QLabel("Ayuda del Sistema")
        help_title.setFont(QFont("Segoe UI", 24, QFont.Bold))
        help_title.setObjectName("pageTitle")
        
        help_content = QLabel("Esta sección contiene información de ayuda sobre el sistema hidropónico.")
        help_content.setFont(QFont("Segoe UI", 14))
        help_content.setWordWrap(True)
        
        help_layout.addWidget(help_title)
        help_layout.addWidget(help_content)
        help_layout.addStretch()
        
        settings_page = QWidget()
        settings_layout = QVBoxLayout(settings_page)
        
        settings_title = QLabel("Configuración del Sistema")
        settings_title.setFont(QFont("Segoe UI", 24, QFont.Bold))
        settings_title.setObjectName("pageTitle")
        
        settings_content = QLabel("Esta sección permite configurar los parámetros del sistema hidropónico.")
        settings_content.setFont(QFont("Segoe UI", 14))
        settings_content.setWordWrap(True)
        
        settings_layout.addWidget(settings_title)
        settings_layout.addWidget(settings_content)
        settings_layout.addStretch()
        
        # Añadir páginas al stacked widget
        self.stacked_widget.addWidget(home_page)
        self.stacked_widget.addWidget(alerts_page)
        self.stacked_widget.addWidget(ph_page)
        self.stacked_widget.addWidget(ec_page)
        self.stacked_widget.addWidget(temp_page)
        self.stacked_widget.addWidget(water_page)
        self.stacked_widget.addWidget(help_page)
        self.stacked_widget.addWidget(settings_page)
        
        content_layout.addWidget(self.stacked_widget)
        
        # Añadir widgets al layout principal
        main_layout.addWidget(self.sidebar)
        main_layout.addWidget(content)
        
        # Guardar referencias para actualizar temas
        self.content = content
    
    def create_chart_page(self, title, chart_type):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(20)
        
        # Título de la página
        page_title = QLabel(title)
        page_title.setFont(QFont("Segoe UI", 24, QFont.Bold))
        page_title.setObjectName("pageTitle")
        
        # Contenedor para el gráfico
        chart_container = QWidget()
        chart_layout = QVBoxLayout(chart_container)
        chart_layout.setContentsMargins(0, 0, 0, 0)
        
        # Placeholder hasta que se cargue el gráfico real
        chart_layout.addWidget(QLabel(f"Cargando gráfico de {chart_type}..."))
        
        # Guardar referencia al contenedor
        setattr(self, f"{chart_type}_chart_container", chart_container)
        
        layout.addWidget(page_title)
        layout.addWidget(chart_container)
        
        return page
    
    def setup_data(self):
        # Obtener datos iniciales
        self.realtime_data = self.data_generator.get_realtime_data()
        self.historical_data = self.data_generator.get_historical_data()
        
        # Crear gráficos
        self.realtime_chart = ChartWidget("Variables del Sistema en Tiempo Real", self.realtime_data, self.theme_manager, self)
        self.ph_chart = ChartWidget("pH", [self.realtime_data[0]], self.theme_manager, self)
        self.ec_chart = ChartWidget("Conductividad Eléctrica", [self.realtime_data[1]], self.theme_manager, self)
        self.temp_chart = ChartWidget("Temperatura", [self.realtime_data[2]], self.theme_manager, self)
        
        # Datos para el nivel de agua
        water_data = {
            "name": "Nivel de Agua (%)",
            "data": [80, 82, 85, 83, 81, 84, 85],
            "color": "#9333EA"  # Púrpura
        }
        self.water_chart = ChartWidget("Nivel de Agua", [water_data], self.theme_manager, self)
        
        # Reemplazar placeholders con gráficos reales
        realtime_layout = self.realtime_chart_container.layout()
        realtime_layout.replaceWidget(realtime_layout.itemAt(0).widget(), self.realtime_chart)
        
        ph_chart_layout = self.ph_chart_container.layout()
        ph_chart_layout.replaceWidget(ph_chart_layout.itemAt(0).widget(), self.ph_chart)
        
        ec_chart_layout = self.ec_chart_container.layout()
        ec_chart_layout.replaceWidget(ec_chart_layout.itemAt(0).widget(), self.ec_chart)
        
        temp_chart_layout = self.temp_chart_container.layout()
        temp_chart_layout.replaceWidget(temp_chart_layout.itemAt(0).widget(), self.temp_chart)
        
        water_chart_layout = self.water_chart_container.layout()
        water_chart_layout.replaceWidget(water_chart_layout.itemAt(0).widget(), self.water_chart)
    
    def update_data(self):
        # Obtener nuevos datos
        new_data = self.data_generator.update_realtime_data()
        
        # Actualizar tarjetas de sensores
        for series in new_data:
            if series["name"] == "pH":
                self.ph_card.update_value(series["data"][-1])
                self.ph_chart.update_data([series])
            elif series["name"] == "EC (mS/cm)":
                self.ec_card.update_value(series["data"][-1])
                self.ec_chart.update_data([series])
            elif series["name"] == "Temperatura (°C)":
                self.temp_card.update_value(series["data"][-1])
                self.temp_chart.update_data([series])
        
        # Actualizar nivel de agua (simulado)
        water_level = round(self.water_card.value + random.uniform(-2, 2))
        if water_level < 70:
            water_level = 70
        elif water_level > 95:
            water_level = 95
        self.water_card.update_value(water_level)
        
        # Actualizar gráficos
        self.realtime_chart.update_data(new_data)
        self.realtime_data = new_data
    
    def toggle_theme(self):
        self.theme_manager.toggle_theme()
        self.apply_theme()
    
    def apply_theme(self):
        colors = self.theme_manager.get_colors()
        
        # Aplicar tema a la ventana principal
        self.setStyleSheet(f"""
            #mainWindow {{
                background-color: {colors['background']};
            }}
            #contentArea {{
                background-color: {colors['background']};
            }}
            QLabel {{
                color: {colors['text']};
            }}
            #pageTitle {{
                color: {colors['text']};
                margin-bottom: 10px;
            }}
            QPushButton {{
                background-color: {colors['primary']};
                color: {colors['primary_light']};
                border: none;
                border-radius: 6px;
                padding: 8px 16px;
            }}
            QPushButton:hover {{
                background-color: {colors['primary_light']};
                color: {colors['primary']};
            }}
        """)
        
        # Aplicar tema a los componentes
        self.sidebar.apply_theme()
        
        # Aplicar tema a las tarjetas
        self.ph_card.apply_theme()
        self.ec_card.apply_theme()
        self.temp_card.apply_theme()
        self.water_card.apply_theme()
        
        # Aplicar tema a los gráficos
        if hasattr(self, 'realtime_chart'):
            self.realtime_chart.apply_theme()
            self.ph_chart.apply_theme()
            self.ec_chart.apply_theme()
            self.temp_chart.apply_theme()
            self.water_chart.apply_theme()

# Importar random para la simulación del nivel de agua
import random
