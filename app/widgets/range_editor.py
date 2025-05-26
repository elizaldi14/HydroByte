from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
import sqlite3

class RangeEditor(QWidget):
    def __init__(self, theme_manager, db_path="hydrobyte.sqlite", parent=None):
        super().__init__(parent)
        self.theme_manager = theme_manager
        self.db_path = db_path

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)

        title_label = QLabel("Editor de Rangos")
        title_label.setFont(QFont("Segoe UI", 14, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        self.ph_min_input = QLineEdit()
        self.ph_min_input.setPlaceholderText("Mínimo pH")
        layout.addWidget(self.ph_min_input)

        self.ph_max_input = QLineEdit()
        self.ph_max_input.setPlaceholderText("Máximo pH")
        layout.addWidget(self.ph_max_input)

        save_button = QPushButton("Guardar")
        save_button.clicked.connect(self.save_ranges)
        layout.addWidget(save_button)

    def save_ranges(self):
        ph_min = self.ph_min_input.text()
        ph_max = self.ph_max_input.text()
        print(f"Guardando rangos: pH mínimo = {ph_min}, pH máximo = {ph_max}")

    def apply_theme(self):
        """Aplica el tema actual (claro u oscuro) al editor de rangos."""
        colors = self.theme_manager.get_colors()
        self.setStyleSheet(f"""
            QWidget {{
                background-color: {colors['card']};
                border: 1px solid {colors['border']};
                border-radius: 8px;
            }}
            QLabel {{
                color: {colors['text']};
                font-size: 14px;
                font-weight: bold;
            }}
            QLineEdit {{
                background-color: {colors['background']};
                color: {colors['text']};
                border: 1px solid {colors['border']};
                border-radius: 6px;
                padding: 4px;
            }}
            QPushButton {{
                background-color: {colors['primary']};
                color: {colors['primary_light']};
                border: none;
                border-radius: 6px;
                padding: 6px 12px;
            }}
            QPushButton:hover {{
                background-color: {colors['primary_light']};
                color: {colors['primary']};
            }}
        """)
