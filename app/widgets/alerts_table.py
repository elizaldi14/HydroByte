from PySide6.QtWidgets import (QTableWidget, QTableWidgetItem, QHeaderView, QLineEdit, QHBoxLayout, QPushButton, QLabel, QWidget)
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QColor, QFont
import sqlite3

class AlertsTable(QTableWidget):
    def __init__(self, theme_manager, parent=None):
        super().__init__(0, 4, parent)
        self.theme_manager = theme_manager
        self.setHorizontalHeaderLabels(["ID", "Sensor", "Mensaje", "Fecha"])
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.verticalHeader().setVisible(False)
        self.setAlternatingRowColors(True)
        self.setShowGrid(False)
        self.setSelectionBehavior(QTableWidget.SelectRows)
        self.setEditTriggers(QTableWidget.NoEditTriggers)
        self.setObjectName("alertsTable")
        self.setMinimumHeight(300)
        self.setFont(QFont("Segoe UI", 12))
        self.page = 0
        self.rows_per_page = 21
        self.full_alerts = []
        self.filtered_alerts = []
        self.search_text = ''
        self.apply_theme()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.load_alerts_from_db)
        self.timer.start(1000)  # Cada 5 segundos


    def apply_theme(self):
        colors = self.theme_manager.get_colors()
        hover = colors.get('hover', '#F1F5F9')
        hover_text = colors.get('hover_text', '#0F172A')
        background = colors.get('background', '#FFFFFF')
        card = colors.get('card', '#FFFFFF')
        border = colors.get('border', '#E5E7EB')
        text = colors.get('text', '#1E293B')
        primary = colors.get('primary', '#F8FAFC')

        self.setStyleSheet(f"""
            QTableWidget#alertsTable {{
                background-color: {card};
                border: 1px solid {border};
                border-radius: 10px;
                color: {text};
                font-size: 13px;
                font-family: "Segoe UI", sans-serif;
            }}
            QHeaderView::section {{
                background-color: {primary};
                color: {text};
                font-weight: 500;
                font-size: 13px;
                border: none;
                border-bottom: 1px solid {border};
                padding: 6px 4px;
            }}
            QTableWidget::item {{
                background-color: transparent;
                padding: 4px;
                border: none;
                border-bottom: 1px solid {border};
            }}
            QTableWidget::item:selected {{
                background-color: {hover};
                color: {hover_text};
            }}
            QTableWidget {{
                selection-background-color: {hover};
                selection-color: {hover_text};
                alternate-background-color: {background};
            }}
        """)


    def set_alerts(self, alerts):
        self.full_alerts = alerts
        self.page = 0
        self.search(self.search_text)  # Esto también llama a update_table()
        
        # 🔄 Actualizar botones y etiqueta de paginación desde la ventana principal
        main_window = self.window()
        if hasattr(main_window, 'update_alerts_pagination'):
            main_window.update_alerts_pagination()


    
    def load_alerts_from_db(self, db_path='hydrobyte.sqlite'):
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()

            # Obtener las últimas alertas
            cursor.execute("""
            SELECT 
                alerts.id, 
                sensors.name AS sensor_name, 
                alerts.message, 
                alerts.timestamp
            FROM alerts
            JOIN sensors ON alerts.sensor_id = sensors.id
            ORDER BY alerts.timestamp DESC
            LIMIT 100
            """)

            alerts = cursor.fetchall()
            conn.close()

            if alerts == self.full_alerts:
                return

            # Hay nuevas alertas
            if alerts and (not self.full_alerts or alerts[0][0] != self.full_alerts[0][0]):
                sensor_name = alerts[0][1]
                message = alerts[0][2]

                main_window = self.window()
                if hasattr(main_window, 'mostrar_alerta'):
                    main_window.mostrar_alerta(sensor_name, message, "warning")

            self.set_alerts(alerts)

        except sqlite3.Error as e:
            print(f"Error al consultar la base de datos: {e}")


    def update_table(self):
        start = self.page * self.rows_per_page
        end = start + self.rows_per_page
        alerts_to_show = self.filtered_alerts[start:end]
        self.setRowCount(len(alerts_to_show))
        for row, alert in enumerate(alerts_to_show):
            for col, value in enumerate(alert):
                item = QTableWidgetItem(str(value))
                self.setItem(row, col, item)
        self.resizeRowsToContents()

    def search(self, text):
        self.search_text = text.lower()
        if not self.search_text:
            self.filtered_alerts = self.full_alerts
        else:
            self.filtered_alerts = [a for a in self.full_alerts if any(self.search_text in str(x).lower() for x in a)]
        self.page = 0
        self.update_table()

    def next_page(self):
        if (self.page + 1) * self.rows_per_page < len(self.filtered_alerts):
            self.page += 1
            self.update_table()

    def prev_page(self):
        if self.page > 0:
            self.page -= 1
            self.update_table()

    def get_total_pages(self):
        return max(1, (len(self.filtered_alerts) + self.rows_per_page - 1) // self.rows_per_page)

    def get_current_page(self):
        return self.page + 1

    def keyPressEvent(self, event):
        # Navegación con flechas y enter
        if event.key() == Qt.Key_Right:
            self.parent().parent().parent().on_alerts_next_page()
        elif event.key() == Qt.Key_Left:
            self.parent().parent().parent().on_alerts_prev_page()
        elif event.key() == Qt.Key_Down:
            next_row = min(self.currentRow() + 1, self.rowCount() - 1)
            self.setCurrentCell(next_row, self.currentColumn())
        elif event.key() == Qt.Key_Up:
            prev_row = max(self.currentRow() - 1, 0)
            self.setCurrentCell(prev_row, self.currentColumn())
        else:
            super().keyPressEvent(event)


