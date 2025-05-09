from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, 
                              QHBoxLayout, QPushButton, QLabel, QStackedWidget,
                              QFrame, QApplication, QLineEdit, QListWidget, QListWidgetItem, QDialog, QTextEdit, QGridLayout, QSizePolicy)
from PySide6.QtCore import Qt, QTimer, Slot, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QFont, QIcon, QColor
from PySide6.QtWidgets import QGraphicsDropShadowEffect
from app.widgets.pump_control import PumpCard
from app.theme_manager import ThemeManager
from app.widgets.sidebar import Sidebar
from app.widgets.sensor_card import SensorCard
from app.widgets.chart_widget import ChartWidget
from app.widgets.chart_historial import ChartWidgetHistory
from app.widgets.alerts_table import AlertsTable
from app.widgets.alert_card import AlertCard
from utils.data_generator import DataGenerator
from utils.constants import LIGHT_COLORS
import json
import random

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
        self.timer.start(1000)  # Actualizar cada 3 segundos
        
    def setup_ui(self):
        self.setWindowTitle("HydroByte")
        self.resize(1200, 800)
        self.setObjectName("mainWindow")
        
        # Inicializar los datos antes de crear las páginas
        self.realtime_data = self.data_generator.get_realtime_data()
        self.historical_data = self.data_generator.get_historical_data()
        
        # Crear la gráfica general ANTES de armar el layout
        self.realtime_chart = ChartWidget("Variables del Sistema en Tiempo Real", self.realtime_data, self.theme_manager, self)
        
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
        self.sidebar.pumps_btn.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(6))
        self.sidebar.help_btn.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(7))
        self.sidebar.settings_btn.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(8))
        
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
        
        self.ph_card = SensorCard("pH", "ph", "", "5.5 - 6.5", LIGHT_COLORS["ph_color"], self.theme_manager, self)
        self.ec_card = SensorCard("Conductividad (EC)", "tds", "mS/cm", "1.5 - 2.2 mS/cm", LIGHT_COLORS["ec_color"], self.theme_manager, self)
        self.temp_card = SensorCard("Temperatura", "temp", "°C", "18 - 24 °C", LIGHT_COLORS["temp_color"], self.theme_manager, self)
        self.water_card = SensorCard("Nivel del Agua", "dist", "%", "70 - 90 %", "#9333EA", self.theme_manager, self)
        
        sensors_layout.addWidget(self.ph_card)
        sensors_layout.addWidget(self.ec_card)
        sensors_layout.addWidget(self.temp_card)
        sensors_layout.addWidget(self.water_card)
        
        home_layout.addWidget(sensors_widget)
        
        # Gráficos en la página de inicio
        self.realtime_chart_container = QWidget()
        realtime_layout = QVBoxLayout(self.realtime_chart_container)
        realtime_layout.setContentsMargins(0, 0, 0, 0)
        realtime_layout.addWidget(self.realtime_chart)  # Mostrar la gráfica con todos los sensores monitoreando
        home_layout.addWidget(self.realtime_chart_container)
        
        # Página de alertas
        alerts_page = QWidget()
        alerts_layout = QVBoxLayout(alerts_page)

        alerts_title = QLabel("Alertas del Sistema")
        alerts_title.setFont(QFont("Segoe UI", 24, QFont.Bold))
        alerts_title.setObjectName("pageTitle")
        alerts_layout.addWidget(alerts_title)

        # Cards de las 3 alertas más recientes (deben ir arriba)
        self.alerts_cards_container = QWidget()
        self.alerts_cards_layout = QHBoxLayout(self.alerts_cards_container)
        self.alerts_cards_layout.setContentsMargins(0, 0, 0, 0)
        self.alerts_cards_layout.setSpacing(18)
        alerts_layout.addWidget(self.alerts_cards_container)

        # Buscador a la derecha, arriba de la tabla
        search_row = QWidget()
        search_row_layout = QHBoxLayout(search_row)
        search_row_layout.setContentsMargins(0, 0, 0, 0)
        search_row_layout.setSpacing(10)
        search_row_layout.addStretch()
        self.alerts_search = QLineEdit()
        self.alerts_search.setPlaceholderText("Buscar alerta...")
        self.alerts_search.setFixedWidth(260)
        self.alerts_search.setStyleSheet("font-size: 15px; border-radius: 8px; border: 1px solid #CBD5E1; padding: 7px 12px;")
        self.alerts_search.setMaximumWidth(260)
        self.alerts_search.setMinimumHeight(36)
        self.alerts_search.setContentsMargins(0, 0, 0, 0)
        search_row_layout.addWidget(self.alerts_search)
        alerts_layout.addWidget(search_row)

        # Tabla de alertas bonita y adaptable al tema
        self.alerts_table = AlertsTable(self.theme_manager)
        alerts_layout.addWidget(self.alerts_table)

        # Paginación abajo a la derecha
        pagination_row = QWidget()
        pagination_layout = QHBoxLayout(pagination_row)
        pagination_layout.setContentsMargins(0, 0, 0, 0)
        pagination_layout.setSpacing(10)
        pagination_layout.addStretch()
        self.alerts_prev_btn = QPushButton("Anterior")
        self.alerts_prev_btn.setFixedWidth(95)
        self.alerts_prev_btn.clicked.connect(self.on_alerts_prev_page)
        self.alerts_page_label = QLabel()
        self.alerts_page_label.setFont(QFont("Segoe UI", 11, QFont.Bold))
        self.alerts_next_btn = QPushButton("Siguiente")
        self.alerts_next_btn.setFixedWidth(95)
        self.alerts_next_btn.clicked.connect(self.on_alerts_next_page)
        pagination_layout.addWidget(self.alerts_prev_btn)
        pagination_layout.addWidget(self.alerts_page_label)
        pagination_layout.addWidget(self.alerts_next_btn)
        alerts_layout.addWidget(pagination_row)

        # Ejemplo de datos de prueba
        example_alerts = [
            [1, "pH", "Valor fuera de rango", "Activo", "2025-04-30 22:45"],
            [2, "EC", "Conductividad baja", "Solucionado", "2025-04-30 21:12"],
            [3, "Temperatura", "Sensor desconectado", "Activo", "2025-04-29 10:03"],
            [4, "Nivel Agua", "Nivel crítico", "Activo", "2025-04-28 08:27"],
            [5, "pH", "pH estable", "Solucionado", "2025-04-27 15:00"],
            [6, "EC", "Conductividad estable", "Solucionado", "2025-04-27 14:45"],
            [7, "Temperatura", "Temperatura alta", "Activo", "2025-04-27 10:33"],
            [8, "Nivel Agua", "Nivel bajo", "Activo", "2025-04-26 09:50"],
            [9, "pH", "Sensor sin calibrar", "Activo", "2025-04-25 08:21"],
            [10, "EC", "Conductividad fuera de rango", "Activo", "2025-04-25 07:10"],
            [11, "Temperatura", "Temperatura normal", "Solucionado", "2025-04-24 19:40"],
            [12, "Nivel Agua", "Nivel óptimo", "Solucionado", "2025-04-24 18:00"]
        ]
        self.set_alerts_data(example_alerts)

        # Páginas para cada tipo de gráfico
        ph_page = self.create_chart_page("Monitoreo de pH", "ph")
        ec_page = self.create_chart_page("Monitoreo de Conductividad Eléctrica", "ec")
        temp_page = self.create_chart_page("Monitoreo de Temperatura", "temp")
        water_page = self.create_chart_page("Monitoreo de Nivel de Agua", "water")
        
        # Página de bombas
        pumps_page = self.create_pumps_page()
        
        # Página de ayuda
        help_page = self.create_help_page()
        
        # Páginas de ayuda y configuración
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
        self.stacked_widget.addWidget(pumps_page)
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

        page_title = QLabel(title)
        page_title.setFont(QFont("Segoe UI", 24, QFont.Bold))
        page_title.setObjectName("pageTitle")

        top_row = QWidget()
        top_row_layout = QHBoxLayout(top_row)
        top_row_layout.setContentsMargins(0, 0, 0, 0)
        top_row_layout.setSpacing(20)

        # Card de sensor y gráficas
        if chart_type == "ph":
            sensor_card = SensorCard("pH", "ph", "", "5.5 - 6.5", LIGHT_COLORS["ph_color"], self.theme_manager, self)
            self.ph_submenu_card = sensor_card
            realtime_index = 0
            chart_title = "Gráfica de pH"
            secondary_title = "Histórico de pH"
        elif chart_type == "ec":
            sensor_card = SensorCard("Conductividad (EC)", "tds", "mS/cm", "1.5 - 2.2 mS/cm", LIGHT_COLORS["ec_color"], self.theme_manager, self)
            self.ec_submenu_card = sensor_card
            realtime_index = 1
            chart_title = "Gráfica de Conductividad"
            secondary_title = "Histórico de Conductividad"
        elif chart_type == "temp":
            sensor_card = SensorCard("Temperatura", "temp", "°C", "18 - 24 °C", LIGHT_COLORS["temp_color"], self.theme_manager, self)
            self.temp_submenu_card = sensor_card
            realtime_index = 2
            chart_title = "Gráfica de Temperatura"
            secondary_title = "Histórico de Temperatura"
        elif chart_type == "water":
            sensor_card = SensorCard("Nivel del Agua", "dist", "%", "70 - 90 %", "#9333EA", self.theme_manager, self)
            self.water_submenu_card = sensor_card
            realtime_index = None
            chart_title = "Gráfica de Nivel de Agua"
            secondary_title = "Histórico de Nivel de Agua"
        else:
            sensor_card = QLabel("No implementado")
            realtime_index = None
            chart_title = "Gráfica"
            secondary_title = "Histórico"

        sensor_card.setMinimumWidth(260)
        sensor_card.setMaximumWidth(320)
        top_row_layout.addWidget(sensor_card)

        # Gráfica de tiempo real (referencia para actualización)
        if chart_type == "water":
            realtime_chart = ChartWidget(chart_title, [{"name": "Distancia (cm)", "data": [], "color": "#9333EA"}], self.theme_manager, self)
            self.water_realtime_chart = realtime_chart
            historical_data = [self.historical_data[3]]
        elif realtime_index is not None:
            realtime_chart = ChartWidget(chart_title, [self.realtime_data[realtime_index]], self.theme_manager, self)
            if chart_type == "ph":
                self.ph_realtime_chart = realtime_chart
                historical_data = [self.historical_data[0]]
            elif chart_type == "ec":
                self.ec_realtime_chart = realtime_chart
                historical_data = [self.historical_data[1]]
            elif chart_type == "temp":
                self.temp_realtime_chart = realtime_chart
                historical_data = [self.historical_data[2]]
        else:
            realtime_chart = ChartWidget(chart_title, [], self.theme_manager, self)
            historical_data = []

        realtime_chart.setMaximumHeight(400)
        top_row_layout.addWidget(realtime_chart, 1)

        # Gráfica de historial (más grande, abajo)
        bottom_chart = ChartWidgetHistory(secondary_title, historical_data, self.theme_manager, self)
        bottom_chart.setMinimumHeight(260)

        layout.addWidget(page_title)
        layout.addWidget(top_row)
        layout.addWidget(bottom_chart)

        return page
    
    def create_pumps_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setAlignment(Qt.AlignTop)
        layout.setContentsMargins(40, 30, 40, 30)
        layout.setSpacing(20)

        # Título
        title = QLabel("Control de Bombas")
        title.setFont(QFont("Segoe UI", 24, QFont.Bold))
        title.setObjectName("pageTitle")
        layout.addWidget(title)

        # Descripción
        description = QLabel("Aquí puedes controlar el estado de las bombas del sistema hidropónico.")
        description.setFont(QFont("Segoe UI", 14))
        description.setWordWrap(True)
        layout.addWidget(description)

        # Contenedor para las tarjetas de bombas
        pumps_container = QWidget()
        pumps_layout = QHBoxLayout(pumps_container)
        pumps_layout.setSpacing(20)
        pumps_layout.setContentsMargins(0, 20, 0, 0)
        
        # Crear tarjetas para cada bomba usando el nuevo widget PumpCard
        pump1 = PumpCard("Bomba de Circulación", self.theme_manager, "pump_circulacion.png")
        pump2 = PumpCard("Bomba de Alcalinización", self.theme_manager, "pump_peristaltica.png")
        pump3 = PumpCard("Bomba de Acidez", self.theme_manager, "pump_peristaltica.png")
        
        pumps_layout.addWidget(pump1)
        pumps_layout.addWidget(pump2)
        pumps_layout.addWidget(pump3)
        
        layout.addWidget(pumps_container)
        layout.addStretch()
        
        return page

    def create_help_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setAlignment(Qt.AlignTop)
        layout.setContentsMargins(40, 30, 40, 30)
        layout.setSpacing(20)

        # Título
        title = QLabel("Preguntas Frecuentes")
        title.setFont(QFont("Segoe UI", 22, QFont.Bold))
        title.setAlignment(Qt.AlignHCenter)
        layout.addWidget(title)

        # Barra de búsqueda
        search_bar = QLineEdit()
        search_bar.setPlaceholderText("Buscar pregunta...")
        search_bar.setFixedWidth(420)
        search_bar.setAlignment(Qt.AlignCenter)
        search_bar.setStyleSheet("font-size: 16px; padding: 8px; border-radius: 8px; border: 1px solid #CBD5E1;")
        search_bar.setMaximumWidth(420)
        search_bar.setMinimumHeight(36)
        search_bar.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(search_bar, alignment=Qt.AlignHCenter)

        # Contenedor para las cards
        cards_container = QWidget()
        cards_layout = QGridLayout(cards_container)
        cards_layout.setSpacing(18)
        cards_layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(cards_container)

        # Botón/Label para ver más
        ver_mas_label = QLabel('<a href="#" style="color:#2563EB;font-weight:bold;text-decoration:none;">Ver más</a>')
        ver_mas_label.setAlignment(Qt.AlignHCenter)
        ver_mas_label.setOpenExternalLinks(False)
        ver_mas_label.setTextInteractionFlags(Qt.TextBrowserInteraction)
        ver_mas_label.setStyleSheet("font-size: 16px; margin-top: 12px;")
        layout.addWidget(ver_mas_label)
        ver_mas_label.hide()    

        # Cargar preguntas desde JSON
        try:
            with open("ayuda.json", "r", encoding="utf-8") as f:
                faqs = json.load(f)
        except Exception as e:
            faqs = []

        self.faq_items = faqs
        self.cards_container = cards_container
        self.cards_layout = cards_layout
        self.faqs_filtered = faqs
        self.faqs_page = 0
        self.faqs_per_page = 9

        def show_faq_cards(page=0, filtered=None):
            # Limpia cards previas
            while cards_layout.count():
                item = cards_layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()
            faqs_to_show = filtered if filtered is not None else faqs
            start = page * self.faqs_per_page
            end = start + self.faqs_per_page
            for idx, faq in enumerate(faqs_to_show[start:end]):
                card = QFrame()
                card.setFrameShape(QFrame.StyledPanel)
                # Cambia el color de fondo y borde usando el tema actual
                theme_colors = self.theme_manager.get_colors() if hasattr(self, 'theme_manager') else {
                    'card': '#FFFFFF', 'border': '#E2E8F0'
                }
                card.setStyleSheet(f"""
                    QFrame {{
                        background: {theme_colors['card']};
                        border-radius: 12px;
                        border: 1px solid {theme_colors['border']};
                        padding: 18px;
                    }}
                """)
                card.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
                card_layout = QVBoxLayout(card)
                card_layout.setSpacing(10)
                pregunta_lbl = QLabel(faq["pregunta"])
                pregunta_lbl.setWordWrap(True)
                pregunta_lbl.setFont(QFont("Segoe UI", 14, QFont.Bold))
                # Cambia el color del texto usando el tema actual
                pregunta_lbl.setStyleSheet(f"color: {theme_colors.get('text', '#1E293B')};")
                pregunta_lbl.setAlignment(Qt.AlignTop)
                card_layout.addWidget(pregunta_lbl)
                card.mousePressEvent = lambda e, pregunta=faq["pregunta"], respuesta=faq["respuesta"]: show_answer_modal(pregunta, respuesta)
                cards_layout.addWidget(card, idx // 3, idx % 3)
            # Mostrar/ocultar "Ver más"
            if end < len(faqs_to_show):
                ver_mas_label.show()
            else:
                ver_mas_label.hide()

        def on_search():
            query = search_bar.text().strip().lower()
            if not query:
                self.faqs_filtered = faqs
            else:
                self.faqs_filtered = [faq for faq in faqs if query in faq["pregunta"].lower() or query in faq["respuesta"].lower()]
            self.faqs_page = 0
            show_faq_cards(self.faqs_page, self.faqs_filtered)

        def ver_mas_clicked(_):
            self.faqs_page += 1
            show_faq_cards(self.faqs_page, self.faqs_filtered)

        def show_answer_modal(pregunta, respuesta):
            # Obtener colores del tema actual
            theme_colors = self.theme_manager.get_colors() if hasattr(self, 'theme_manager') else {
                'card': '#FFFFFF', 'border': '#E2E8F0', 'text': '#1E293B', 'text_secondary': '#64748B', 'background': '#F8FAFC', 'shadow': 'rgba(0,0,0,0.08)'
            }
            dlg = QDialog(page)
            dlg.setWindowTitle("")  # Sin barra de título
            dlg.setWindowFlags(dlg.windowFlags() | Qt.FramelessWindowHint | Qt.Dialog)
            dlg.setAttribute(Qt.WA_TranslucentBackground)
            dlg.setModal(True)
            dlg.setMinimumWidth(420)
            dlg.setMaximumWidth(520)
            dlg.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

            # Animación de aparición (fade in)
            anim = QPropertyAnimation(dlg, b"windowOpacity")
            anim.setDuration(260)
            anim.setStartValue(0.0)
            anim.setEndValue(1.0)
            anim.setEasingCurve(QEasingCurve.OutCubic)
            anim.start()
            dlg._anim = anim  # Para evitar recolección de basura

            # Fondo y sombra
            container = QFrame(dlg)
            container.setObjectName("faqModalContainer")
            container.setStyleSheet(f"""
                QFrame#faqModalContainer {{
                    background: {theme_colors['card']};
                    border-radius: 18px;
                    border: 1.5px solid {theme_colors['border']};
                    padding: 26px 28px 18px 28px;
                }}
            """)
            shadow = QGraphicsDropShadowEffect(container)
            shadow.setBlurRadius(32)
            shadow.setOffset(0, 12)
            shadow.setColor(QColor(0, 0, 0, 80 if theme_colors.get('shadow') == 'dark' else 40))
            container.setGraphicsEffect(shadow)

            layout = QVBoxLayout(dlg)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.addWidget(container)
            container_layout = QVBoxLayout(container)
            container_layout.setSpacing(18)
            container_layout.setContentsMargins(0, 0, 0, 0)

            # Pregunta
            pregunta_lbl = QLabel(pregunta)
            pregunta_lbl.setFont(QFont("Segoe UI", 16, QFont.Bold))
            pregunta_lbl.setStyleSheet(f"color: {theme_colors['text']}; margin-bottom: 6px;")
            pregunta_lbl.setWordWrap(True)
            container_layout.addWidget(pregunta_lbl)

            # Respuesta
            answer_lbl = QTextEdit()
            answer_lbl.setReadOnly(True)
            answer_lbl.setText(respuesta)
            answer_lbl.setStyleSheet(f"font-size: 15px; padding: 8px 0 0 0; border: none; background: transparent; color: {theme_colors['text_secondary']};")
            container_layout.addWidget(answer_lbl)

            # Botón cerrar
            btn_close = QPushButton("Cerrar")
            btn_close.setCursor(Qt.PointingHandCursor)
            btn_close.setFixedWidth(100)
            btn_close.setStyleSheet(f"""
                QPushButton {{
                    background-color: {theme_colors['border']};
                    color: {theme_colors['text']};
                    border: none;
                    border-radius: 8px;
                    font-size: 15px;
                    font-weight: 600;
                    padding: 9px 0;
                    margin-top: 10px;
                }}
                QPushButton:hover {{
                    background-color: {theme_colors['text_secondary']};
                    color: {theme_colors['card']};
                }}
            """)
            btn_close.clicked.connect(dlg.accept)
            container_layout.addWidget(btn_close, alignment=Qt.AlignRight)

            dlg.exec()

        show_faq_cards(0)
        search_bar.textChanged.connect(on_search)
        ver_mas_label.linkActivated.connect(ver_mas_clicked)

        return page
    
    def setup_data(self):
        # Obtener datos iniciales
        # self.realtime_data y self.historical_data ya se inicializan en setup_ui
        # Solo se crean los ChartWidgets que faltan
        self.ph_chart = ChartWidget("Gráfica de pH", [self.realtime_data[0]], self.theme_manager, self)
        self.ec_chart = ChartWidget("Gráfica de Conductividad", [self.realtime_data[1]], self.theme_manager, self)
        self.temp_chart = ChartWidget("Gráfica de Temperatura", [self.realtime_data[2]], self.theme_manager, self)
        self.water_chart = ChartWidget("Gráfica de Nivel de Agua", [self.realtime_data[3]], self.theme_manager, self)

        # Las referencias a los ChartWidget se usan para actualización, pero ya no hay que reemplazar widgets en contenedores

    def update_data(self):
        # Obtener nuevos datos
        new_data = self.data_generator.update_realtime_data()
        
        # Actualizar tarjetas de sensores y gráficas en tiempo real
        for series in new_data:
            if series["name"] == "pH":
                self.ph_card.update_value(series["data"][-1])
                self.ph_card.set_status()
                if hasattr(self, "ph_submenu_card"):
                    self.ph_submenu_card.update_value(series["data"][-1])
                    self.ph_submenu_card.set_status()
                self.ph_chart.update_data([series])
                if hasattr(self, "ph_realtime_chart"):
                    self.ph_realtime_chart.update_data([series])
            elif series["name"] == "EC (mS/cm)":
                self.ec_card.update_value(series["data"][-1])
                self.ec_card.set_status()
                if hasattr(self, "ec_submenu_card"):
                    self.ec_submenu_card.update_value(series["data"][-1])
                    self.ec_submenu_card.set_status()
                self.ec_chart.update_data([series])
                if hasattr(self, "ec_realtime_chart"):
                    self.ec_realtime_chart.update_data([series])
            elif series["name"] == "Temperatura (°C)":
                self.temp_card.update_value(series["data"][-1])
                self.temp_card.set_status()
                if hasattr(self, "temp_submenu_card"):
                    self.temp_submenu_card.update_value(series["data"][-1])
                    self.temp_submenu_card.set_status()
                self.temp_chart.update_data([series])
                if hasattr(self, "temp_realtime_chart"):
                    self.temp_realtime_chart.update_data([series])
            elif series["name"] == "Distancia (cm)":
                self.water_card.update_value(series["data"][-1])
                self.water_card.set_status()
                if hasattr(self, "water_submenu_card"):
                    self.water_submenu_card.update_value(series["data"][-1])
                    self.water_submenu_card.set_status()
                self.water_chart.update_data([series])
                if hasattr(self, "water_realtime_chart"):
                    self.water_realtime_chart.update_data([series])


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
        if hasattr(self, 'alerts_table'):
            self.alerts_table.apply_theme()
        if hasattr(self, 'alerts_cards_layout'):
            for i in range(self.alerts_cards_layout.count()):
                widget = self.alerts_cards_layout.itemAt(i).widget()
                if hasattr(widget, 'apply_theme'):
                    widget.apply_theme()
        if hasattr(self, 'cards_layout'):
            for i in range(self.cards_layout.count()):
                item = self.cards_layout.itemAt(i)
                widget = item.widget()
                if widget:
                    widget.setStyleSheet(f"background: {colors['card']}; border-radius: 12px; border: 1px solid {colors['border']}; padding: 18px;")
                    # Cambia el color del texto de la pregunta
                    if widget.layout() and widget.layout().count() > 0:
                        pregunta_lbl = widget.layout().itemAt(0).widget()
                        if pregunta_lbl:
                            pregunta_lbl.setStyleSheet(f"color: {colors.get('text', '#1E293B')};")
        # --- NUEVO: Aplicar tema a páginas de submenú (gráficas) ---
        for idx in range(self.stacked_widget.count()):
            page = self.stacked_widget.widget(idx)
            # Solo aplica a páginas de submenú (pH, EC, Temp, Agua)
            # Se asume que las páginas de submenú están en los índices 2,3,4,5
            if idx in [2, 3, 4, 5]:
                self.apply_theme_to_subpage(page, idx)

    def apply_theme_to_subpage(self, page, idx):
        colors = self.theme_manager.get_colors()
        # Aplica fondo y color de texto general
        page.setStyleSheet(f"background-color: {colors['background']};")
        layout = page.layout() if hasattr(page, 'layout') else None
        if layout:
            for i in range(layout.count()):
                widget = layout.itemAt(i).widget()
                if isinstance(widget, QLabel):
                    # Aplicar estilo a las etiquetas
                    widget.setStyleSheet(f"color: {colors['text']}; background: transparent;")
                # Si es top_row, contiene sensor_card y realtime_chart
                elif isinstance(widget, QWidget) and widget.layout():
                    for j in range(widget.layout().count()):
                        subwidget = widget.layout().itemAt(j).widget()
                        if hasattr(subwidget, 'apply_theme'):
                            subwidget.apply_theme()
                # Si es bottom_chart
                if hasattr(widget, 'apply_theme'):
                    widget.apply_theme()

    def set_alerts_data(self, alerts):
        # Mostrar las 3 alertas más recientes como cards
        for i in reversed(range(self.alerts_cards_layout.count())):
            widget = self.alerts_cards_layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)
        for alert in alerts[-3:][::-1]:
            card = AlertCard(alert, self.theme_manager)
            self.alerts_cards_layout.addWidget(card)
        self.alerts_table.set_alerts(alerts)
        self.update_alerts_pagination()

    def update_alerts_pagination(self):
        total_pages = self.alerts_table.get_total_pages()
        current_page = self.alerts_table.get_current_page()
        self.alerts_page_label.setText(f"Página {current_page} de {total_pages}")
        self.alerts_prev_btn.setEnabled(current_page > 1)
        self.alerts_next_btn.setEnabled(current_page < total_pages)

    def on_alerts_search(self, text):
        self.alerts_table.search(text)
        self.update_alerts_pagination()

    def on_alerts_prev_page(self):
        self.alerts_table.prev_page()
        self.update_alerts_pagination()

    def on_alerts_next_page(self):
        self.alerts_table.next_page()
        self.update_alerts_pagination()
