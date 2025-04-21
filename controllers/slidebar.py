from ui_slidebar import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from controllers.baseGraphc import GraphCE

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
        
        self.change_page(0)
        self.graphc()

    def change_page(self, index):
        self.stackedWidget.setCurrentIndex(index)

    def graphc(self):
        self.graph = GraphCE()

        # Crear layout dentro del widget de historial_1
        layout = QVBoxLayout(self.widget)
        layout.addWidget(self.graph)
        self.widget.setLayout(layout)
