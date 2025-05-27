from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                              QPushButton, QFrame, QGridLayout,
                              QLineEdit, QSizePolicy as QSP)
from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QFont, QDoubleValidator
from .sensor_service import SensorService
import logging

class RangeEditor(QWidget):
    ranges_updated = Signal(dict)
    
    def __init__(self, theme_manager, db_path, parent=None):
        super().__init__(parent)
        self.theme_manager = theme_manager
        self.sensor_service = SensorService(db_path)
        self.edit_mode = False
        self.sensor_inputs = {}
        self.original_values = {}
        # Map sensor IDs to their display names
        self.sensor_ids = {
            'ph': 1,
            'ec': 2,
            'temperature': 3,
            'water_level': 4
        }
        self.setup_ui()
        self.load_sensor_ranges()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Main card
        self.main_card = QFrame()
        self.main_card.setObjectName("mainCard")
        self.main_card.setStyleSheet("""
            QFrame#mainCard {
                background: white;
                border-radius: 12px;
                padding: 20px;
                border: 1px solid #e2e8f0;
            }
            QLabel {
                color: #2d3748;
                font-size: 14px;
            }
            QLineEdit {
                padding: 8px 12px;
                border: 1px solid #cbd5e0;
                border-radius: 6px;
                min-width: 80px;
            }
            QLineEdit:disabled {
                background: #f7fafc;
                border-color: #e2e8f0;
            }
            QPushButton {
                padding: 8px 16px;
                border-radius: 6px;
                font-weight: 500;
                min-width: 100px;
            }
            #saveButton {
                background: #48bb78;
                color: white;
                border: none;
            }
            #saveButton:hover {
                background: #38a169;
            }
            #cancelButton {
                background: #f56565;
                color: white;
                border: none;
                margin-left: 10px;
            }
            #cancelButton:hover {
                background: #e53e3e;
            }
            #editButton {
                background: #4299e1;
                color: white;
                border: none;
            }
            #editButton:hover {
                background: #3182ce;
            }
        """)
        
        card_layout = QVBoxLayout(self.main_card)
        
        # Title
        title = QLabel("Rangos de Sensores")
        title.setFont(QFont("Segoe UI", 16, QFont.Bold))
        title.setStyleSheet("margin-bottom: 20px;")
        card_layout.addWidget(title)
        
        # Grid for sensor inputs
        self.grid = QGridLayout()
        self.grid.setSpacing(15)
        self.grid.setColumnStretch(0, 1)
        self.grid.setColumnStretch(1, 1)
        self.grid.setColumnStretch(2, 1)
        
        # Add headers
        headers = ["Sensor", "Mínimo", "Máximo"]
        for col, text in enumerate(headers):
            label = QLabel(f"<b>{text}</b>")
            self.grid.addWidget(label, 0, col)
        
        # Add sensor rows with proper labels and keys
        self.sensors = ["Temperatura", "Conductividad Eléctrica", "pH", "Nivel de Agua"]
        self.sensor_keys = ["temperature", "ec", "ph", "water_level"]
        self.unit_suffixes = {
            "Temperatura": "°C",
            "Conductividad Eléctrica": " mS/cm",
            "pH": "",
            "Nivel de Agua": " cm"
        }
        
        for row, (sensor, key) in enumerate(zip(self.sensors, self.sensor_keys), 1):
            # Sensor name with unit
            name_label = QLabel(f"{sensor}{self.unit_suffixes[sensor]}")
            self.grid.addWidget(name_label, row, 0)
            
            # Min input
            min_input = QLineEdit()
            min_input.setValidator(QDoubleValidator())
            min_input.setEnabled(False)
            self.grid.addWidget(min_input, row, 1)
            
            # Max input
            max_input = QLineEdit()
            max_input.setValidator(QDoubleValidator())
            max_input.setEnabled(False)
            self.grid.addWidget(max_input, row, 2)
            
            self.sensor_inputs[key] = {"min": min_input, "max": max_input}
        
        card_layout.addLayout(self.grid)
        
        # Button container
        self.button_container = QHBoxLayout()
        self.button_container.addStretch()
        
        # Edit button (shown by default)
        self.edit_button = QPushButton("Modificar")
        self.edit_button.setObjectName("editButton")
        self.edit_button.clicked.connect(self.enable_editing)
        self.button_container.addWidget(self.edit_button)
        
        # Save and Cancel buttons (hidden by default)
        self.save_button = QPushButton("Guardar")
        self.save_button.setObjectName("saveButton")
        self.save_button.clicked.connect(self.save_ranges)
        self.save_button.hide()
        
        self.cancel_button = QPushButton("Cancelar")
        self.cancel_button.setObjectName("cancelButton")
        self.cancel_button.clicked.connect(self.cancel_editing)
        self.cancel_button.hide()
        
        self.button_container.addWidget(self.save_button)
        self.button_container.addWidget(self.cancel_button)
        
        card_layout.addLayout(self.button_container)
        layout.addWidget(self.main_card)
    
    def load_sensor_ranges(self):
        """Load sensor optimal ranges from the database."""
        logging.info("Cargando rangos de sensores desde la base de datos...")
        
        try:
            # Get sensor ranges from the service
            sensor_ranges = self.sensor_service.get_sensor_ranges()
            logging.info(f"Rangos obtenidos de la base de datos: {sensor_ranges}")
            
            # Clear any existing values first
            for sensor_key, inputs in self.sensor_inputs.items():
                logging.info(f"Limpiando inputs para {sensor_key}")
                inputs["min"].clear()
                inputs["max"].clear()
            
            # Mapeo de claves de sensor a sus respectivos nombres en la interfaz
            sensor_display_names = {
                'temperature': 'Temperatura',
                'ec': 'Conductividad Eléctrica',
                'ph': 'pH',
                'water_level': 'Nivel de Agua'
            }
            
            # Actualizar la interfaz con los valores cargados
            for sensor_key, inputs in self.sensor_inputs.items():
                if sensor_key in sensor_ranges:
                    try:
                        min_val = float(sensor_ranges[sensor_key]["min"])
                        max_val = float(sensor_ranges[sensor_key]["max"])
                        
                        inputs["min"].setText(f"{min_val:.2f}")
                        inputs["max"].setText(f"{max_val:.2f}")
                        
                        # Guardar valores originales
                        self.original_values[sensor_key] = {
                            "min": min_val,
                            "max": max_val
                        }
                        
                        logging.info(f"Cargado {sensor_key} ({sensor_display_names.get(sensor_key, sensor_key)}): min={min_val}, max={max_val}")
                    except (ValueError, KeyError) as e:
                        logging.error(f"Error al procesar valores para {sensor_key}: {e}")
                        if sensor_key in sensor_ranges:
                            logging.error(f"Valores recibidos: {sensor_ranges[sensor_key]}")
                else:
                    logging.warning(f"No se encontraron valores para el sensor: {sensor_key} ({sensor_display_names.get(sensor_key, sensor_key)})")
            
            # Verificar que todos los sensores tengan valores
            for sensor_key in self.sensor_inputs.keys():
                if sensor_key not in sensor_ranges:
                    logging.warning(f"Sensor {sensor_key} ({sensor_display_names.get(sensor_key, sensor_key)}) no encontrado en la base de datos")
                    
        except Exception as e:
            logging.error(f"Error inesperado al cargar rangos de sensores: {e}", exc_info=True)
        
        return True
        
        return True
    
    def enable_editing(self):
        self.edit_mode = True
        self.edit_button.hide()
        self.save_button.show()
        self.cancel_button.show()
        
        for inputs in self.sensor_inputs.values():
            inputs["min"].setEnabled(True)
            inputs["max"].setEnabled(True)
    
    def cancel_editing(self):
        """Cancel editing and restore original values."""
        self.edit_mode = False
        self.save_button.hide()
        self.cancel_button.hide()
        self.edit_button.show()
        
        # Restore original values
        for key, inputs in self.sensor_inputs.items():
            if key in self.original_values:
                # Format the values to 2 decimal places
                min_val = self.original_values[key]["min"]
                max_val = self.original_values[key]["max"]
                inputs["min"].setText(f"{float(min_val):.2f}")
                inputs["max"].setText(f"{float(max_val):.2f}")
            inputs["min"].setEnabled(False)
            inputs["max"].setEnabled(False)
        
        print("Edición cancelada - Valores restaurados")
    
    def save_ranges(self):
        """Save the current optimal ranges to the database."""
        logging.info("Iniciando guardado de rangos de sensores...")
        
        try:
            # First validate all inputs
            sensor_updates = {}
            
            # Mapeo de claves de sensor a sus respectivos nombres en la interfaz
            sensor_display_names = {
                'temperature': 'Temperatura',
                'ec': 'Conductividad Eléctrica',
                'ph': 'pH',
                'water_level': 'Nivel de Agua'
            }
            
            for sensor_key, inputs in self.sensor_inputs.items():
                display_name = sensor_display_names.get(sensor_key, sensor_key)
                
                try:
                    # Obtener y validar valores mínimos y máximos
                    min_text = inputs["min"].text().replace(',', '.').strip()
                    max_text = inputs["max"].text().replace(',', '.').strip()
                    
                    # Validar que los campos no estén vacíos
                    if not min_text or not max_text:
                        error_msg = f"Error: Los valores no pueden estar vacíos para {display_name}"
                        logging.error(error_msg)
                        self.show_error_message(error_msg)
                        return False
                    
                    # Convertir a valores numéricos
                    try:
                        min_val = float(min_text)
                        max_val = float(max_text)
                    except ValueError:
                        error_msg = f"Error: Valores inválidos para {display_name}. Deben ser números."
                        logging.error(error_msg)
                        self.show_error_message(error_msg)
                        return False
                    
                    # Validar que el mínimo sea menor que el máximo
                    if min_val >= max_val:
                        error_msg = (
                            f"Error en {display_name}: "
                            f"El valor mínimo ({min_val}) debe ser menor que el máximo ({max_val})"
                        )
                        logging.error(error_msg)
                        self.show_error_message(error_msg)
                        return False
                    
                    # Validar rangos razonables según el tipo de sensor
                    if sensor_key == 'temperature' and (min_val < -20 or max_val > 50):
                        error_msg = f"Advertencia: El rango de temperatura ({min_val}-{max_val}°C) parece fuera de lo normal."
                        logging.warning(error_msg)
                        
                    elif sensor_key == 'ph' and (min_val < 0 or max_val > 14):
                        error_msg = f"Advertencia: El rango de pH ({min_val}-{max_val}) está fuera de la escala estándar (0-14)."
                        logging.warning(error_msg)
                    
                    # Obtener el ID del sensor
                    sensor_id = self.sensor_ids.get(sensor_key)
                    if not sensor_id:
                        error_msg = f"Error: ID no encontrado para el sensor {display_name}"
                        logging.error(error_msg)
                        self.show_error_message(error_msg)
                        return False
                    
                    # Guardar los valores validados
                    sensor_updates[sensor_id] = {"min": min_val, "max": max_val}
                    logging.info(f"Validado {display_name} (ID: {sensor_id}): rango {min_val} - {max_val}")
                    
                except Exception as e:
                    error_msg = f"Error inesperado al validar {display_name}: {str(e)}"
                    logging.error(error_msg, exc_info=True)
                    self.show_error_message(f"Error al validar {display_name}")
                    return False
                    
                except ValueError as ve:
                    logging.error(f"Error: Valores inválidos para {display_name}: {ve}")
                    return False
            
            # Save to database using the service
            if self.sensor_service.update_sensor_ranges(sensor_updates):
                # Update original values to match the saved values
                for sensor_key, inputs in self.sensor_inputs.items():
                    min_val = float(inputs["min"].text().replace(',', '.'))
                    max_val = float(inputs["max"].text().replace(',', '.'))
                    self.original_values[sensor_key] = {"min": min_val, "max": max_val}
                
                # Emit signal with updated ranges
                updated_ranges = {
                    sensor: {
                        "min": float(inputs["min"].text().replace(',', '.')), 
                        "max": float(inputs["max"].text().replace(',', '.'))
                    }
                    for sensor, inputs in self.sensor_inputs.items()
                }
                self.ranges_updated.emit(updated_ranges)
                
                # Disable editing mode
                self.cancel_editing()
                logging.info("Rangos guardados exitosamente")
                return True
            else:
                logging.error("Error al guardar los rangos en la base de datos")
                return False
                
        except Exception as e:
            logging.error(f"Error inesperado al guardar rangos: {e}", exc_info=True)
            return False
    
    def show_error_message(self, message):
        """Muestra un mensaje de error al usuario con el diseño de la aplicación.
        
        Args:
            message (str): El mensaje de error a mostrar.
        """
        from PySide6.QtWidgets import (QMessageBox, QVBoxLayout, QLabel, 
                                    QDialog, QDialogButtonBox, QPushButton)
        from PySide6.QtGui import QIcon
        from PySide6.QtCore import Qt
        
        # Obtener colores del tema actual
        colors = self.theme_manager.get_colors()
        bg_color = colors.get("background", "#F0F2F5")
        card_bg = colors.get("card", "#FFFFFF")
        text_color = colors.get("text", "#1E293B")
        error_color = colors.get("error", "#EF4444")
        border_color = colors.get("border", "#E2E8F0")
        
        # Crear diálogo personalizado
        dialog = QDialog(self)
        dialog.setWindowTitle("Error de validación")
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.resize(400, 200)
        
        # Configurar layout
        layout = QVBoxLayout(dialog)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        
        # Ícono de error
        icon_label = QLabel()
        icon_label.setPixmap(QIcon(":/icons/error.svg").pixmap(48, 48))
        icon_label.setAlignment(Qt.AlignCenter)
        
        # Título
        title = QLabel("Error de validación")
        title.setStyleSheet(f"""
            font-size: 18px;
            font-weight: bold;
            color: {error_color};
            margin-bottom: 10px;
        """)
        title.setAlignment(Qt.AlignCenter)
        
        # Mensaje
        msg_label = QLabel(message)
        msg_label.setStyleSheet(f"""
            font-size: 14px;
            color: {text_color};
            padding: 10px;
            background: {bg_color};
            border-radius: 6px;
            border: 1px solid {border_color};
        """)
        msg_label.setWordWrap(True)
        msg_label.setAlignment(Qt.AlignCenter)
        
        # Botón de aceptar
        button_box = QDialogButtonBox(QDialogButtonBox.Ok)
        button_box.accepted.connect(dialog.accept)
        
        # Aplicar estilos al botón
        ok_button = button_box.button(QDialogButtonBox.Ok)
        ok_button.setStyleSheet(f"""
            QPushButton {{
                background-color: {error_color};
                color: white;
                border: none;
                padding: 8px 20px;
                border-radius: 6px;
                min-width: 100px;
            }}
            QPushButton:hover {{
                background-color: #DC2626;
            }}
        """)
        
        # Añadir widgets al layout
        layout.addWidget(icon_label, alignment=Qt.AlignCenter)
        layout.addWidget(title)
        layout.addWidget(msg_label)
        layout.addWidget(button_box, alignment=Qt.AlignCenter)
        
        # Estilo del diálogo
        dialog.setStyleSheet(f"""
            QDialog {{
                background: {card_bg};
                border: 1px solid {border_color};
                border-radius: 12px;
            }}
            QLabel {{
                color: {text_color};
            }}
        """)
        
        # Mostrar diálogo
        dialog.exec_()
    
    def get_ranges(self):
        ranges = {}
        for key, inputs in self.sensor_inputs.items():
            try:
                ranges[key] = {
                    "min": float(inputs["min"].text()),
                    "max": float(inputs["max"].text())
                }
            except ValueError:
                ranges[key] = {"min": 0, "max": 0}
        return ranges
    
    def update_ranges(self, ranges):
        for key, values in ranges.items():
            if key in self.sensor_inputs:
                self.sensor_inputs[key]["min"].setText(str(values.get("min", 0)))
                self.sensor_inputs[key]["max"].setText(str(values.get("max", 0)))
                
                # Update original values
                self.original_values[key] = {
                    "min": values.get("min", 0),
                    "max": values.get("max", 0)
                }
    
    def apply_theme(self):
        """Apply the current theme to the widget."""
        colors = self.theme_manager.get_colors()
        
        # Get colors with fallbacks
        bg_color = colors.get("background", "#F0F2F5")
        card_bg = colors.get("card", "#FFFFFF")
        text_color = colors.get("text", "#1E293B")
        text_secondary = colors.get("text_secondary", "#64748B")
        primary = colors.get("primary", "#0EA5E9")
        border_color = colors.get("border", "#E2E8F0")
        
        # Update card style
        self.main_card.setStyleSheet(f"""
            QFrame#mainCard {{
                background: {card_bg};
                border-radius: 12px;
                padding: 20px;
                border: 1px solid {border_color};
            }}
            QLabel {{
                color: {text_color};
                font-size: 14px;
            }}
            QLineEdit {{
                padding: 8px 12px;
                border: 1px solid {border_color};
                border-radius: 6px;
                min-width: 80px;
                color: {text_color};
                background: {card_bg};
            }}
            QLineEdit:disabled {{
                background: {bg_color};
                border-color: {border_color};
                color: {text_secondary};
            }}
            QPushButton {{
                padding: 8px 16px;
                border-radius: 6px;
                font-weight: 500;
                min-width: 100px;
            }}
            #saveButton {{
                background: #10B981;  /* ph_color from constants */
                color: white;
                border: none;
            }}
            #saveButton:hover {{
                background: #0d9f74;  /* Slightly darker green */
            }}
            #cancelButton {{
                background: #EF4444;  /* Red color for cancel */
                color: white;
                border: none;
                margin-left: 10px;
            }}
            #cancelButton:hover {{
                background: #DC2626;  /* Slightly darker red */
            }}
            #editButton {{
                background: {primary};
                color: white;
                border: none;
            }}
            #editButton:hover {{
                background: #0c8fd1;  /* Slightly darker primary */
            }}
        """)
