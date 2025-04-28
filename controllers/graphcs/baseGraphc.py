import pyqtgraph as pg
from PySide6.QtWidgets import QWidget, QVBoxLayout  # Importa QVBoxLayout
from time import time
from random import randrange
from PySide6.QtCore import QTimer

class GraphCE(QWidget):
    def __init__(self):
        super().__init__()
        
        self.graphWidget = pg.PlotWidget()
        self.layout = QVBoxLayout(self)  # Aquí usas QVBoxLayout
        self.layout.addWidget(self.graphWidget)
        
        # Datos
        self.x = []
        self.y = []
        self.max_points = 5  # Limitar a los últimos 10 puntos
        # Fondo de la grafica
        self.graphWidget.setBackground('w')
        # Curva
        self.data_line = self.graphWidget.plot(self.x, self.y, pen=pg.mkPen('#00AAFF'))
        #Fijar el rango
        self.graphWidget.setYRange(0, 15)

        # Bloquear interacción
        vb = self.graphWidget.getViewBox()
        vb.setMouseEnabled(x=False, y=False)
        vb.setMenuEnabled(False)
        vb.wheelEvent = lambda ev: None
        
        # Timer
        self.timer = QTimer(self)
        self.timer.setInterval(1000)  # Actualización cada 1 segundo
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

    def update_plot(self):
        t = time()
        v = randrange(0, 15)  # Aquí puedes integrar tu método para obtener datos reales
        self.x.append(t)
        self.y.append(v)

        # Solo mantener los últimos N puntos
        if len(self.x) > self.max_points:
            self.x = self.x[-self.max_points:]
            self.y = self.y[-self.max_points:]

        self.data_line.setData(self.x, self.y)
