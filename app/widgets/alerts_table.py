from PySide6.QtWidgets import (QTableWidget, QTableWidgetItem, QHeaderView, QLineEdit, QHBoxLayout, QPushButton, QLabel, QWidget)
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QFont

class AlertsTable(QTableWidget):
    def __init__(self, theme_manager, parent=None):
        super().__init__(0, 5, parent)
        self.theme_manager = theme_manager
        self.setHorizontalHeaderLabels(["ID", "Sensor", "Mensaje", "Estado", "Fecha"])
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
        self.rows_per_page = 10
        self.full_alerts = []
        self.filtered_alerts = []
        self.search_text = ''
        self.apply_theme()

    def apply_theme(self):
        colors = self.theme_manager.get_colors()
        hover = colors.get('hover', '#F0F9FF')
        hover_text = colors.get('hover_text', '#0F172A')
        background = colors.get('background', '#F8FAFC')
        card = colors.get('card', '#FFFFFF')
        border = colors.get('border', '#E2E8F0')
        text = colors.get('text', '#1E293B')
        primary = colors.get('primary', '#FFFFFF')
        self.setStyleSheet(f"""
            QTableWidget#alertsTable {{
                background: {card};
                border-radius: 14px;
                border: 1.5px solid {border};
                color: {text};
                gridline-color: {border};
            }}
            QHeaderView::section {{
                background: {primary};
                color: {text};
                font-weight: bold;
                font-size: 15px;
                border: none;
                border-bottom: 2px solid {border};
                padding: 7px 0;
            }}
            QTableWidget::item {{
                background: transparent;
                color: {text};
                border-bottom: 1px solid {border};
            }}
            QTableWidget::item:selected {{
                background: {hover};
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
        self.filtered_alerts = alerts
        self.page = 0
        self.update_table()

    def update_table(self):
        start = self.page * self.rows_per_page
        end = start + self.rows_per_page
        alerts_to_show = self.filtered_alerts[start:end]
        self.setRowCount(len(alerts_to_show))
        for row, alert in enumerate(alerts_to_show):
            for col, value in enumerate(alert):
                item = QTableWidgetItem(str(value))
                if col == 3:
                    if value.lower() == 'activo':
                        item.setForeground(QColor('#ef4444'))
                        item.setFont(QFont("Segoe UI", 12, QFont.Bold))
                    elif value.lower() == 'solucionado':
                        item.setForeground(QColor('#22c55e'))
                        item.setFont(QFont("Segoe UI", 12, QFont.Bold))
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
