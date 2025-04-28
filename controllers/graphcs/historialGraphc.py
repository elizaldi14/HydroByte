import pyqtgraph as pg
from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCore import QTimer
from time import time, strftime, localtime
from random import randrange

class TimeAxisItem(pg.AxisItem):
    def tickStrings(self, values, scale, spacing):
        return [strftime('%H:%M:%S', localtime(value)) for value in values]

class GraphHistory(QWidget):
    def __init__(self):
        super().__init__()

        # Crear eje X personalizado
        self.graphWidget = pg.PlotWidget(axisItems={'bottom': TimeAxisItem(orientation='bottom')})
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.graphWidget)

        # Datos
        self.x = []
        self.y = []
        self.max_points = 10

        # Fondo transparente
        self.graphWidget.setBackground(None)

        # Grid
        self.graphWidget.showGrid(x=False, y=True, alpha=0.5)

        # Estilo de los ejes
        axis_pen = pg.mkPen(color='#000000', width=1)
        for orientation in ['bottom', 'left']:
            self.graphWidget.getAxis(orientation).setPen(axis_pen)
            self.graphWidget.getAxis(orientation).setTextPen(axis_pen)
            self.graphWidget.getAxis(orientation).setStyle(tickLength=-5)

        # Marcar cada número del 0 al 15 en Y con espaciado
        yticks = [(i, str(i)) for i in range(20, 30)]
        self.graphWidget.getAxis('left').setTicks([yticks])

        # Ajustar la posición de los ticks del eje Y para espaciado
        y_axis = self.graphWidget.getAxis('left')
        y_axis.setTickSpacing(2)  # Aumenta el espaciado entre los números

        # Curva
        self.data_line = self.graphWidget.plot(
            self.x,
            self.y,
            pen=pg.mkPen(color='#00AAFF', width=3),
            symbol='o',
            symbolSize=8,
            symbolBrush='#00AAFF'
        )

        # Fijar rango en Y
        self.graphWidget.setYRange(20, 30)

        # Desactivar interacción
        vb = self.graphWidget.getViewBox()
        vb.setMouseEnabled(x=False, y=False)
        vb.setMenuEnabled(False)
        vb.wheelEvent = lambda ev: None

        # Timer
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

    def update_plot(self):
        t = time()
        v = randrange(20, 30)
        self.x.append(t)
        self.y.append(v)

        if len(self.x) > self.max_points:
            self.x = self.x[-self.max_points:]
            self.y = self.y[-self.max_points:]

        self.data_line.setData(self.x, self.y)
