from ui_slidebar import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from controllers.slidebar import MySideBar

app = QApplication(sys.argv)

window = MySideBar()    

window.show()
app.exec()