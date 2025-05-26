from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit, QPushButton, QFrame
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
import sqlite3

class RangeEditor(QWidget):
    def __init__(self, theme_manager, db_path="hydrobyte.sqlite", parent=None):
        super().__init__(parent)
        self.theme_manager = theme_manager
        self.db_path = db_path
        self.editors = {}
        self.is_editing = False
        self.setup_ui()
        self.load_ranges()
        self.apply_theme()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(20)
        layout.setContentsMargins(0, 0, 0, 0)

        # Tarjeta de fondo
        self.card = QFrame()
        self.card.setObjectName("rangeEditorCard")
        card_layout = QVBoxLayout(self.card)
        card_layout.setSpacing(15)
        card_layout.setContentsMargins(20, 20, 20, 20)

        # Título
        title = QLabel("Rangos Óptimos de Sensores")
        title.setFont(QFont("Segoe UI", 18, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        card_layout.addWidget(title)

        # Contenedor para los editores
        self.editor_container = QVBoxLayout()
        self.editor_container.setSpacing(10)
        card_layout.addLayout(self.editor_container)

        # Botones de acción
        self.update_button = QPushButton("Actualizar")
        self.update_button.setObjectName("updateButton")
        self.update_button.clicked.connect(self.enable_editing)
        card_layout.addWidget(self.update_button, alignment=Qt.AlignRight)

        # Contenedor para los botones de guardar/cancelar
        self.save_cancel_widget = QWidget()
        self.save_cancel_layout = QHBoxLayout(self.save_cancel_widget)
        self.save_cancel_layout.setSpacing(10)
        self.save_cancel_layout.setAlignment(Qt.AlignRight)

        self.save_button = QPushButton("Guardar")
        self.save_button.setObjectName("saveButton")
        self.save_button.clicked.connect(self.save_changes)

        self.cancel_button = QPushButton("Cancelar")
        self.cancel_button.setObjectName("cancelButton")
        self.cancel_button.clicked.connect(self.cancel_changes)

        self.save_cancel_layout.addWidget(self.save_button)
        self.save_cancel_layout.addWidget(self.cancel_button)
        card_layout.addWidget(self.save_cancel_widget)
        self.save_cancel_widget.setVisible(False)

        layout.addWidget(self.card)

    def load_ranges(self):
        """Carga los rangos desde la base de datos y los muestra."""
        self.editor_container.setParent(None)  # Limpia el contenedor
        self.editor_container = QVBoxLayout()
        self.editor_container.setSpacing(10)

        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT name, optimal_min, optimal_max FROM sensors")
            sensors = cursor.fetchall()
            conn.close()

            for sensor in sensors:
                sensor_name, optimal_min, optimal_max = sensor

                sensor_layout = QHBoxLayout()
                sensor_layout.setSpacing(10)

                sensor_label = QLabel(sensor_name)
                sensor_label.setFont(QFont("Segoe UI", 14))
                sensor_label.setFixedWidth(150)

                min_input = QLineEdit(str(optimal_min))
                min_input.setFixedWidth(100)
                min_input.setObjectName("minInput")
                min_input.setReadOnly(True)

                max_input = QLineEdit(str(optimal_max))
                max_input.setFixedWidth(100)
                max_input.setObjectName("maxInput")
                max_input.setReadOnly(True)

                sensor_layout.addWidget(sensor_label)
                sensor_layout.addWidget(min_input)
                sensor_layout.addWidget(max_input)

                self.editor_container.addLayout(sensor_layout)
                self.editors[sensor_name] = (min_input, max_input)

        except sqlite3.Error as e:
            print(f"Error al cargar los rangos desde la base de datos: {e}")

        self.card.layout().insertLayout(1, self.editor_container)

    def enable_editing(self):
        """Habilita la edición de los campos."""
        self.is_editing = True
        for min_input, max_input in self.editors.values():
            min_input.setReadOnly(False)
            max_input.setReadOnly(False)
        self.update_button.setVisible(False)
        self.save_cancel_widget.setVisible(True)

    def cancel_changes(self):
        """Cancela los cambios y deshabilita la edición."""
        self.is_editing = False
        self.load_ranges()
        self.update_button.setVisible(True)
        self.save_cancel_widget.setVisible(False)

    def save_changes(self):
        """Guarda los cambios en la base de datos."""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            for sensor_name, (min_input, max_input) in self.editors.items():
                optimal_min = float(min_input.text())
                optimal_max = float(max_input.text())
                cursor.execute("""
                    UPDATE sensors
                    SET optimal_min = ?, optimal_max = ?
                    WHERE name = ?
                """, (optimal_min, optimal_max, sensor_name))

            conn.commit()
            conn.close()
            print("Rangos actualizados correctamente.")
        except sqlite3.Error as e:
            print(f"Error al guardar los rangos en la base de datos: {e}")

        self.cancel_changes()  # Deshabilita la edición y recarga los valores

    def apply_theme(self):
        """Aplica el tema actual (claro u oscuro) a los elementos del editor."""
        colors = self.theme_manager.get_colors()
        self.card.setStyleSheet(f"""
            QFrame#rangeEditorCard {{
                background-color: {colors['card']};
                border-radius: 12px;
                border: 1px solid {colors['border']};
            }}
        """)
        self.setStyleSheet(f"""
            QLabel {{
                color: {colors['text']};
            }}
            QLineEdit#minInput, QLineEdit#maxInput {{
                background-color: {colors['background']};
                color: {colors['text']};
                border: 1px solid {colors['border']};
                border-radius: 6px;
                padding: 6px;
            }}
            QLineEdit[readOnly="true"] {{
                background-color: {colors['card']};
                color: {colors['text_secondary']};
            }}
            QPushButton#updateButton {{
                background-color: {colors['primary']};
                color: white;
                border: none;
                border-radius: 6px;
                padding: 6px;
            }}
            QPushButton#updateButton:hover {{
                background-color: {colors['primary_light']};
            }}
            QPushButton#saveButton, QPushButton#cancelButton {{
                background-color: {colors['primary']};
                color: white;
                border: none;
                border-radius: 6px;
                padding: 6px;
            }}
            QPushButton#saveButton:hover, QPushButton#cancelButton:hover {{
                background-color: {colors['primary_light']};
            }}
        """)
