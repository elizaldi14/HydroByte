from PySide6.QtWidgets import QTableWidgetItem, QHeaderView, QAbstractItemView
from PySide6.QtCore import Qt, QTimer
from models.conexion import ConexionDB

class TablaAlertas:
    def __init__(self, ui):
        self.ui = ui
        self.conexion = ConexionDB()
        self.conn = self.conexion.conectar()
        self.configurar_tabla()  # Configuración inicial
        self.cargar_datos()

        # Aquí creamos el temporizador para refrescar los datos cada 5 segundos
        self.timer = QTimer()
        self.timer.timeout.connect(self.cargar_datos)
        self.timer.start(5000)

    def configurar_tabla(self):
        """Configura propiedades visuales y de comportamiento de la tabla"""
        tabla = self.ui.tabla_alertas
        
        # 1. Ocultar números de fila (vertical header)
        tabla.verticalHeader().setVisible(False)
        
        # 2. Configurar modo de selección (solo una fila a la vez)
        tabla.setSelectionMode(QAbstractItemView.SingleSelection)
        tabla.setSelectionBehavior(QAbstractItemView.SelectRows)  # Selecciona filas completas
        
        # 3. Deshabilitar edición
        tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def cargar_datos(self):
        cursor = self.conn.cursor()
        query = "SELECT * FROM alerts"
        cursor.execute(query)
        resultados = cursor.fetchall()

        tabla = self.ui.tabla_alertas
        tabla.setRowCount(len(resultados))
        tabla.setColumnCount(len(resultados[0]) if resultados else 0)

        for row_idx, row_data in enumerate(resultados):
            for col_idx, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                item.setTextAlignment(Qt.AlignCenter)
                tabla.setItem(row_idx, col_idx, item)

        tabla.resizeColumnsToContents()
        tabla.horizontalHeader().setStretchLastSection(True)

        cursor.close()