import random
import pyqtgraph as pg
from PySide6.QtCore import Qt, QSizeF
from PySide6.QtWidgets import QSizePolicy
from typing import List, Tuple, Optional

class BaseGraph(pg.PlotWidget):
    def __init__(
        self,
        title: str = "Gráfica",
        x_label: str = "Eje X",
        y_label: str = "Eje Y",
        line_color: str = "#3498db",
        background_color: str = "#ffffff",
        axis_color: str = "#333333",
        grid_alpha: float = 0.1,
        data_range: Tuple[float, float] = (0, 10),
        initial_data_length: int = 100,
    ):
        super().__init__()

        # Configuración básica
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.setBackground(background_color)

        # Configuración de ejes
        self.getPlotItem().setTitle(title, color=axis_color)
        self.getPlotItem().setLabel("left", y_label, color=axis_color)
        self.getPlotItem().setLabel("bottom", x_label, color=axis_color)
        self.getPlotItem().getAxis("bottom").setPen(axis_color)
        self.getPlotItem().getAxis("left").setPen(axis_color)

        # Cuadrícula
        self.getPlotItem().showGrid(x=True, y=True, alpha=grid_alpha)

        # Datos iniciales
        self.data_x = list(range(initial_data_length))
        self.data_y = [random.uniform(*data_range) for _ in range(initial_data_length)]
        self.curve = self.plot(self.data_x, self.data_y, pen=line_color)

        # Configuración personalizable adicional
        self.custom_config()

    def custom_config(self):
        """Método para configuraciones adicionales en clases hijas"""
        pass

    def sizeHint(self):
        if self.parent() is not None:
            parent_size = self.parent().size()
            return QSizeF(parent_size.width() * 0.8, parent_size.height() * 0.8).toSize()
        return super().sizeHint()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        if self.parent() is not None:
            new_width = int(self.parent().width() * 0.8)
            new_height = int(self.parent().height() * 0.8)
            self.setFixedSize(new_width, new_height)

    def update_data(self, new_value: float):
        self.data_x = self.data_x[1:] + [self.data_x[-1] + 1]
        self.data_y = self.data_y[1:] + [new_value]
        self.curve.setData(self.data_x, self.data_y)

    def set_data_range(self, min_val: float, max_val: float):
        self.getPlotItem().setYRange(min_val, max_val)

    def set_line_style(self, color: str, width: float = 1.0):
        self.curve.setPen(pg.mkPen(color=color, width=width))


class GraphCE(BaseGraph):
    def __init__(self):
        super().__init__(
            title="Gráfica de Conductividad Eléctrica",
            x_label="Tiempo",
            y_label="CE",
            line_color="#3498db",
            data_range=(6.0, 8.0),
        )
        self.set_data_range(0, 14)
