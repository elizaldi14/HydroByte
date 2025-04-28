from ui_slidebar import Ui_MainWindow
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from controllers.graphcs.realTimeGraphc import GraphRealTime
from controllers.graphcs.historialGraphc import GraphHistory
from models.tablaAlerts import TablaAlertas

class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("HydroByte")

        self.icon_name_widget.setHidden(True)

        self.estado_1.clicked.connect(lambda: self.change_page(0))
        self.estado_2.clicked.connect(lambda: self.change_page(0))

        self.alerta_1.clicked.connect(lambda: self.change_page(4))
        self.alerta_2.clicked.connect(lambda: self.change_page(4))
        
        self.historial_1.clicked.connect(lambda: self.change_page(1))
        self.historial_2.clicked.connect(lambda: self.change_page(1))
        
        self.ayuda_1.clicked.connect(lambda: self.change_page(2))
        self.ayuda_2.clicked.connect(lambda: self.change_page(2))
        
        self.configuracion_1.clicked.connect(lambda: self.change_page(3))
        self.configuracion_2.clicked.connect(lambda: self.change_page(3))
        
        self.listWidget.itemClicked.connect(lambda _: self.change_page_ayuda())

        # No necesitas setear manualmente keyPressEvent aquí

        self.change_page(5)
        self.graphcRealTime()
        self.graphcHistory()
        TablaAlertas(self)

    def change_page(self, index):
        self.stackedWidget.setCurrentIndex(index)

    def graphcRealTime(self):
        self.graphcRealTime = GraphRealTime()

        # Crear layout dentro del widget realTime
        layout = QVBoxLayout(self.realTime)
        layout.addWidget(self.graphcRealTime)
        self.realTime.setLayout(layout)

    def graphcHistory(self):
        self.graphcHistory = GraphHistory()

        # Crear layout dentro del widget history
        layout = QVBoxLayout(self.history)
        layout.addWidget(self.graphcHistory)
        self.history.setLayout(layout)

    def change_page_ayuda(self, index=None):
        if isinstance(index, int):
            self.stackAyuda.setCurrentIndex(index)
        else:
            index = self.listWidget.currentRow()
            self.stackAyuda.setCurrentIndex(index)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            if self.stackedWidget.currentIndex() == 2 and not self.stackAyuda.currentIndex() == 4:  # Si estamos en la página de Ayuda
                self.listWidget.clearSelection()
                self.change_page_ayuda(4)
            elif self.stackAyuda.currentIndex() == 4 and self.stackedWidget.currentIndex() == 2:
                self.change_page(5)
            else:
                self.change_page(5)

        else:
            super().keyPressEvent(event)
