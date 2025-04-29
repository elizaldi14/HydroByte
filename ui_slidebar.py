# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newDessigner.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.icon_widget = QWidget(self.centralwidget)
        self.icon_widget.setObjectName(u"icon_widget")
        self.icon_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"	color:white;\n"
"	height: 30px;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: #F5FAFE;\n"
"	color: #1F95EF;\n"
"	font-weight: bold;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.icon_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.icon_widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(40, 40))
        self.label.setMaximumSize(QSize(40, 40))
        self.label.setPixmap(QPixmap(u":/img/logo.jpg"))
        self.label.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 15, -1, -1)
        self.estado_1 = QPushButton(self.icon_widget)
        self.estado_1.setObjectName(u"estado_1")
        icon = QIcon()
        icon.addFile(u":/img/home_white.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/img/home_black.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.estado_1.setIcon(icon)
        self.estado_1.setIconSize(QSize(25, 25))
        self.estado_1.setCheckable(True)
        self.estado_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.estado_1)

        self.alerta_1 = QPushButton(self.icon_widget)
        self.alerta_1.setObjectName(u"alerta_1")
        icon1 = QIcon()
        icon1.addFile(u":/img/warning_white.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/img/warning_black.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.alerta_1.setIcon(icon1)
        self.alerta_1.setIconSize(QSize(25, 25))
        self.alerta_1.setCheckable(True)
        self.alerta_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.alerta_1)

        self.historial_1 = QPushButton(self.icon_widget)
        self.historial_1.setObjectName(u"historial_1")
        icon2 = QIcon()
        icon2.addFile(u":/img/timeline__white.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/img/timeline_black.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.historial_1.setIcon(icon2)
        self.historial_1.setIconSize(QSize(25, 25))
        self.historial_1.setCheckable(True)
        self.historial_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.historial_1)

        self.ayuda_1 = QPushButton(self.icon_widget)
        self.ayuda_1.setObjectName(u"ayuda_1")
        icon3 = QIcon()
        icon3.addFile(u":/img/help__white.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/img/help_black.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.ayuda_1.setIcon(icon3)
        self.ayuda_1.setIconSize(QSize(25, 25))
        self.ayuda_1.setCheckable(True)
        self.ayuda_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.ayuda_1)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 315, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.configuracion_1 = QPushButton(self.icon_widget)
        self.configuracion_1.setObjectName(u"configuracion_1")
        icon4 = QIcon()
        icon4.addFile(u":/img/settings_white.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/img/settings_black.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.configuracion_1.setIcon(icon4)
        self.configuracion_1.setIconSize(QSize(25, 25))
        self.configuracion_1.setCheckable(True)
        self.configuracion_1.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.configuracion_1)


        self.gridLayout_4.addWidget(self.icon_widget, 0, 0, 1, 1)

        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(0, 170, 255);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton{\n"
"	color:white;\n"
"	text-align: left;\n"
"	height: 30px;\n"
"	border: none;\n"
"	padding-left: 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: #F5FAFE;\n"
"	color: #1F95EF;\n"
"	font-weight: bold;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 20, -1)
        self.label_2 = QLabel(self.icon_name_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(40, 40))
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setPixmap(QPixmap(u":/img/logo.jpg"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.icon_name_widget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(Qt.TextFormat.PlainText)

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 15, -1, -1)
        self.estado_2 = QPushButton(self.icon_name_widget)
        self.estado_2.setObjectName(u"estado_2")
        self.estado_2.setIcon(icon)
        self.estado_2.setIconSize(QSize(25, 25))
        self.estado_2.setCheckable(True)
        self.estado_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.estado_2)

        self.alerta_2 = QPushButton(self.icon_name_widget)
        self.alerta_2.setObjectName(u"alerta_2")
        self.alerta_2.setIcon(icon1)
        self.alerta_2.setIconSize(QSize(25, 25))
        self.alerta_2.setCheckable(True)
        self.alerta_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.alerta_2)

        self.historial_2 = QPushButton(self.icon_name_widget)
        self.historial_2.setObjectName(u"historial_2")
        self.historial_2.setIcon(icon2)
        self.historial_2.setIconSize(QSize(25, 25))
        self.historial_2.setCheckable(True)
        self.historial_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.historial_2)

        self.ayuda_2 = QPushButton(self.icon_name_widget)
        self.ayuda_2.setObjectName(u"ayuda_2")
        self.ayuda_2.setIcon(icon3)
        self.ayuda_2.setIconSize(QSize(25, 25))
        self.ayuda_2.setCheckable(True)
        self.ayuda_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.ayuda_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 315, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.configuracion_2 = QPushButton(self.icon_name_widget)
        self.configuracion_2.setObjectName(u"configuracion_2")
        self.configuracion_2.setIcon(icon4)
        self.configuracion_2.setIconSize(QSize(25, 25))
        self.configuracion_2.setCheckable(True)
        self.configuracion_2.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.configuracion_2)


        self.gridLayout_4.addWidget(self.icon_name_widget, 0, 1, 1, 1)

        self.main_menu = QWidget(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        self.main_menu.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_5 = QVBoxLayout(self.main_menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.header_widget = QWidget(self.main_menu)
        self.header_widget.setObjectName(u"header_widget")
        self.horizontalLayout_3 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_12 = QPushButton(self.header_widget)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setStyleSheet(u"border: none;")
        icon5 = QIcon()
        icon5.addFile(u":/img/menu_black.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_12.setIcon(icon5)
        self.pushButton_12.setIconSize(QSize(25, 25))
        self.pushButton_12.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.pushButton_12)

        self.label_8 = QLabel(self.header_widget)
        self.label_8.setObjectName(u"label_8")
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.label_8.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_8)

        self.horizontalSpacer = QSpacerItem(591, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.pushButton_11 = QPushButton(self.header_widget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setStyleSheet(u"border: none;")
        icon6 = QIcon()
        icon6.addFile(u":/img/notifications_black.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_11.setIcon(icon6)
        self.pushButton_11.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.pushButton_11)

        self.salir_1 = QPushButton(self.header_widget)
        self.salir_1.setObjectName(u"salir_1")
        self.salir_1.setStyleSheet(u"border: none;")
        icon7 = QIcon()
        icon7.addFile(u":/img/exit_black.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.salir_1.setIcon(icon7)
        self.salir_1.setIconSize(QSize(25, 25))
        self.salir_1.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.salir_1)


        self.verticalLayout_5.addWidget(self.header_widget)

        self.stackedWidget = QStackedWidget(self.main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: #F3F6FF;")
        self.estado_page = QWidget()
        self.estado_page.setObjectName(u"estado_page")
        self.gridLayout_5 = QGridLayout(self.estado_page)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(50)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_10 = QFrame(self.estado_page)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"QFrame {\n"
"    background-color: #fefefe; /* Blanco suave */\n"
"    border-radius: 15px;\n"
"    border: 3px solid #d0e3ff; /* Azul muy claro */\n"
"    transition: all 0.3s ease; /* Transiciones suaves */\n"
"}\n"
"\n"
"QFrame:hover {\n"
"    border: 3px solid #3399ff; /* Azul fuerte en hover */\n"
"    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15); /* Sombra para profundidad */\n"
"    transform: translateY(-5px); /* Efecto de levantar el frame */\n"
"}\n"
"")
        self.frame_10.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout_11 = QVBoxLayout(self.frame_10)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 20, 0, 20)
        self.label_15 = QLabel(self.frame_10)
        self.label_15.setObjectName(u"label_15")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.label_15.setFont(font2)
        self.label_15.setStyleSheet(u"QLabel {\n"
"	color: #666666;\n"
"	border: none;\n"
"}")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_15)

        self.label_16 = QLabel(self.frame_10)
        self.label_16.setObjectName(u"label_16")
        font3 = QFont()
        font3.setPointSize(13)
        font3.setBold(True)
        self.label_16.setFont(font3)
        self.label_16.setStyleSheet(u"QLabel {\n"
"	color: #000000;\n"
"	border: none;\n"
"}")
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_16)

        self.label_19 = QLabel(self.frame_10)
        self.label_19.setObjectName(u"label_19")
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        self.label_19.setFont(font4)
        self.label_19.setStyleSheet(u"QLabel {\n"
"	color: rgb(70, 255, 3);\n"
"	border: none;\n"
"}")
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_19)

        self.label_20 = QLabel(self.frame_10)
        self.label_20.setObjectName(u"label_20")
        font5 = QFont()
        font5.setPointSize(10)
        self.label_20.setFont(font5)
        self.label_20.setStyleSheet(u"QLabel {\n"
"	color: #000000;\n"
"	border: none;\n"
"}\n"
"")
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_20)


        self.gridLayout_2.addWidget(self.frame_10, 0, 0, 1, 1)

        self.frame_11 = QFrame(self.estado_page)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"QFrame {\n"
"    background-color: #fefefe; /* Blanco suave */\n"
"    border-radius: 15px;\n"
"    border: 3px solid #d0e3ff; /* Azul muy claro */\n"
"    transition: all 0.3s ease; /* Transiciones suaves */\n"
"}\n"
"\n"
"QFrame:hover {\n"
"    border: 3px solid #3399ff; /* Azul fuerte en hover */\n"
"    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15); /* Sombra para profundidad */\n"
"    transform: translateY(-5px); /* Efecto de levantar el frame */\n"
"}\n"
"")
        self.frame_11.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout_12 = QVBoxLayout(self.frame_11)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 20, 0, 20)
        self.label_17 = QLabel(self.frame_11)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font2)
        self.label_17.setStyleSheet(u"QLabel {\n"
"	color: #666666;\n"
"	border: none;\n"
"}")
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_17)

        self.label_18 = QLabel(self.frame_11)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font3)
        self.label_18.setStyleSheet(u"QLabel {\n"
"	color: #000000;\n"
"	border: none;\n"
"}")
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_18)

        self.label_21 = QLabel(self.frame_11)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font4)
        self.label_21.setStyleSheet(u"QLabel {\n"
"	color: rgb(70, 255, 3);\n"
"	border: none;\n"
"}")
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_21)

        self.label_22 = QLabel(self.frame_11)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font5)
        self.label_22.setStyleSheet(u"QLabel {\n"
"	color: #000000;\n"
"	border: none;\n"
"}\n"
"")
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_22)


        self.gridLayout_2.addWidget(self.frame_11, 0, 1, 1, 1)

        self.frame_12 = QFrame(self.estado_page)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"QFrame {\n"
"    background-color: #fefefe; /* Blanco suave */\n"
"    border-radius: 15px;\n"
"    border: 3px solid #d0e3ff; /* Azul muy claro */\n"
"    transition: all 0.3s ease; /* Transiciones suaves */\n"
"}\n"
"\n"
"QFrame:hover {\n"
"    border: 3px solid #3399ff; /* Azul fuerte en hover */\n"
"    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15); /* Sombra para profundidad */\n"
"    transform: translateY(-5px); /* Efecto de levantar el frame */\n"
"}\n"
"")
        self.frame_12.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout_13 = QVBoxLayout(self.frame_12)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 20, 0, 20)
        self.label_23 = QLabel(self.frame_12)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font2)
        self.label_23.setStyleSheet(u"QLabel {\n"
"	color: #666666;\n"
"	border: none;\n"
"}")
        self.label_23.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_23)

        self.label_24 = QLabel(self.frame_12)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font3)
        self.label_24.setStyleSheet(u"QLabel {\n"
"	color: #000000;\n"
"	border: none;\n"
"}")
        self.label_24.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_24)

        self.label_25 = QLabel(self.frame_12)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font4)
        self.label_25.setStyleSheet(u"QLabel {\n"
"	color: rgb(70, 255, 3);\n"
"	border: none;\n"
"}")
        self.label_25.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_25)

        self.label_26 = QLabel(self.frame_12)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font5)
        self.label_26.setStyleSheet(u"QLabel {\n"
"	color: #000000;\n"
"	border: none;\n"
"}\n"
"")
        self.label_26.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_26)


        self.gridLayout_2.addWidget(self.frame_12, 0, 2, 1, 1)

        self.frame_13 = QFrame(self.estado_page)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"QFrame {\n"
"    background-color: #fefefe; /* Blanco suave */\n"
"    border-radius: 15px;\n"
"    border: 3px solid #d0e3ff; /* Azul muy claro */\n"
"    transition: all 0.3s ease; /* Transiciones suaves */\n"
"}\n"
"\n"
"QFrame:hover {\n"
"    border: 3px solid #3399ff; /* Azul fuerte en hover */\n"
"    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15); /* Sombra para profundidad */\n"
"    transform: translateY(-5px); /* Efecto de levantar el frame */\n"
"}\n"
"")
        self.frame_13.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout_14 = QVBoxLayout(self.frame_13)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 20, 0, 20)
        self.label_27 = QLabel(self.frame_13)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font2)
        self.label_27.setStyleSheet(u"QLabel {\n"
"	color: #666666;\n"
"	border: none;\n"
"}")
        self.label_27.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_27)

        self.label_28 = QLabel(self.frame_13)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font3)
        self.label_28.setStyleSheet(u"QLabel {\n"
"	color: #000000;\n"
"	border: none;\n"
"}")
        self.label_28.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_28)

        self.label_29 = QLabel(self.frame_13)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font4)
        self.label_29.setStyleSheet(u"QLabel {\n"
"	color: rgb(70, 255, 3);\n"
"	border: none;\n"
"}")
        self.label_29.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_29)

        self.label_30 = QLabel(self.frame_13)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font5)
        self.label_30.setStyleSheet(u"QLabel {\n"
"	color: #000000;\n"
"	border: none;\n"
"}\n"
"")
        self.label_30.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_30)


        self.gridLayout_2.addWidget(self.frame_13, 1, 0, 1, 1)

        self.frame_14 = QFrame(self.estado_page)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"QFrame {\n"
"    background-color: #fefefe; /* Blanco suave */\n"
"    border-radius: 15px;\n"
"    border: 3px solid #d0e3ff; /* Azul muy claro */\n"
"    transition: all 0.3s ease; /* Transiciones suaves */\n"
"}\n"
"\n"
"QFrame:hover {\n"
"    border: 3px solid #3399ff; /* Azul fuerte en hover */\n"
"    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15); /* Sombra para profundidad */\n"
"    transform: translateY(-5px); /* Efecto de levantar el frame */\n"
"}\n"
"")
        self.frame_14.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout_15 = QVBoxLayout(self.frame_14)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 20, 0, 20)
        self.label_31 = QLabel(self.frame_14)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font2)
        self.label_31.setStyleSheet(u"QLabel {\n"
"	color: #666666;\n"
"	border: none;\n"
"}")
        self.label_31.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_31)

        self.label_32 = QLabel(self.frame_14)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font3)
        self.label_32.setStyleSheet(u"QLabel {\n"
"	color: #000000;\n"
"	border: none;\n"
"}")
        self.label_32.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_32)

        self.label_33 = QLabel(self.frame_14)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font4)
        self.label_33.setStyleSheet(u"QLabel {\n"
"	color: rgb(70, 255, 3);\n"
"	border: none;\n"
"}")
        self.label_33.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_33)

        self.label_34 = QLabel(self.frame_14)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font5)
        self.label_34.setStyleSheet(u"QLabel {\n"
"	color: #000000;\n"
"	border: none;\n"
"}\n"
"")
        self.label_34.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_34)


        self.gridLayout_2.addWidget(self.frame_14, 1, 1, 1, 1)

        self.frame_15 = QFrame(self.estado_page)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"QFrame {\n"
"    background-color: #fefefe; /* Blanco suave */\n"
"    border-radius: 15px;\n"
"    border: 3px solid #d0e3ff; /* Azul muy claro */\n"
"    transition: all 0.3s ease; /* Transiciones suaves */\n"
"}\n"
"\n"
"QFrame:hover {\n"
"    border: 3px solid #3399ff; /* Azul fuerte en hover */\n"
"    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15); /* Sombra para profundidad */\n"
"    transform: translateY(-5px); /* Efecto de levantar el frame */\n"
"}\n"
"")
        self.frame_15.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout_16 = QVBoxLayout(self.frame_15)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 20, 0, 20)
        self.label_35 = QLabel(self.frame_15)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font2)
        self.label_35.setStyleSheet(u"QLabel {\n"
"	color: #666666;\n"
"	border: none;\n"
"}")
        self.label_35.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_35)

        self.label_36 = QLabel(self.frame_15)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font3)
        self.label_36.setStyleSheet(u"QLabel {\n"
"	color: #000000;\n"
"	border: none;\n"
"}")
        self.label_36.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_36)

        self.label_37 = QLabel(self.frame_15)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font4)
        self.label_37.setStyleSheet(u"QLabel {\n"
"	color: rgb(70, 255, 3);\n"
"	border: none;\n"
"}")
        self.label_37.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_37)

        self.label_38 = QLabel(self.frame_15)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font5)
        self.label_38.setStyleSheet(u"QLabel {\n"
"	color: #000000;\n"
"	border: none;\n"
"}\n"
"")
        self.label_38.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_38)


        self.gridLayout_2.addWidget(self.frame_15, 1, 2, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.estado_page)
        self.historial_page = QWidget()
        self.historial_page.setObjectName(u"historial_page")
        self.comboBox = QComboBox(self.historial_page)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(523, 10, 216, 35))
        self.comboBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.comboBox.setStyleSheet(u"QComboBox {\n"
"    background-color: #F5FAFE;  /* Fondo blanco suave */\n"
"    color: #1F95EF;  /* Texto en azul */\n"
"    font-weight: bold;  /* Negrita en el texto */\n"
"    border: 2px solid #1F95EF;  /* Borde azul suave en todos los lados */\n"
"    border-radius: 12px;  /* Bordes redondeados */\n"
"    padding: 5px 15px;  /* Espaciado interno (top-bottom, left-right) */\n"
"    font-size: 14px;  /* Tama\u00f1o de fuente */\n"
"    transition: all 0.3s ease;  /* Transici\u00f3n suave para los efectos */\n"
"    min-width: 150px;  /* Ancho m\u00ednimo del combobox */\n"
"\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 2px solid #007acc;  /* Borde m\u00e1s oscuro cuando se pasa el mouse */\n"
"    background-color: #e6f0ff;  /* Fondo azul claro al pasar el mouse */\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;  /* Eliminar el borde del dropdown */\n"
"    background-color: transparent;  /* Fondo transparente */\n"
"    width: 30px;  /* Ajusta el tama\u00f1o del \u00e1rea de la flecha */\n"
""
                        "    height: 100%;  /* Ajusta para que ocupe el espacio correcto */\n"
"    border-radius: 0px;  /* Aseg\u00farate de que no tenga bordes redondeados */\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border-radius: 12px;  /* Bordes redondeados para la lista de opciones */\n"
"    background-color: #F5FAFE;  /* Fondo de las opciones */\n"
"    border: 2px solid #1F95EF;  /* Borde azul suave alrededor de las opciones */\n"
"    selection-background-color: #1F95EF;  /* Color de fondo de la opci\u00f3n seleccionada */\n"
"    selection-color: white;  /* Color del texto de la opci\u00f3n seleccionada */\n"
"    padding: 5px 0;  /* Espaciado entre las opciones */\n"
"}\n"
"\n"
"QComboBox::item {\n"
"    padding: 8px 12px;  /* Espaciado entre las opciones */\n"
"    font-size: 14px;  /* Tama\u00f1o de fuente para las opciones */\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background-color: #e6f0ff; "
                        " /* Fondo m\u00e1s claro cuando el combobox es editable */\n"
"}\n"
"")
        self.frame_2 = QFrame(self.historial_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(60, 60, 345, 315))
        self.frame_2.setStyleSheet(u"background-color: #0b468e;\n"
"border-radius: 20px;")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.card_ph_widget = QWidget(self.frame_2)
        self.card_ph_widget.setObjectName(u"card_ph_widget")
        self.card_ph_widget.setGeometry(QRect(0, 0, 341, 310))
        self.card_ph_widget.setStyleSheet(u"QWidget {\n"
"	\n"
"	background-color: #00aaff;\n"
"	border-radius: 20px;\n"
"}")
        self.label_7 = QLabel(self.card_ph_widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 0, 81, 91))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setPointSize(30)
        font6.setBold(True)
        font6.setItalic(True)
        font6.setUnderline(False)
        font6.setStrikeOut(False)
        self.label_7.setFont(font6)
        self.label_7.setStyleSheet(u"QLabel {\n"
"	background: transparent;\n"
"	color: white;\n"
"\n"
"}")
        self.label_9 = QLabel(self.card_ph_widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(95, 90, 161, 91))
        font7 = QFont()
        font7.setFamilies([u"Segoe UI"])
        font7.setPointSize(60)
        font7.setBold(True)
        self.label_9.setFont(font7)
        self.label_9.setStyleSheet(u"background: transparent;\n"
"	color: white;")
        self.label_13 = QLabel(self.card_ph_widget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(248, 20, 61, 51))
        font8 = QFont()
        font8.setPointSize(15)
        font8.setBold(True)
        self.label_13.setFont(font8)
        self.label_13.setStyleSheet(u"background: transparent;\n"
"color: rgb(85, 255, 127);")
        self.label_10 = QLabel(self.card_ph_widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(100, 230, 141, 51))
        font9 = QFont()
        font9.setPointSize(30)
        font9.setBold(True)
        font9.setItalic(True)
        self.label_10.setFont(font9)
        self.label_10.setStyleSheet(u"background: transparent;\n"
"	color: white;")
        self.label_14 = QLabel(self.card_ph_widget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(100, 90, 131, 91))
        self.label_14.setFont(font7)
        self.label_14.setStyleSheet(u"background: transparent;\n"
"	color: black;")
        self.label_39 = QLabel(self.card_ph_widget)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(250, 20, 61, 51))
        self.label_39.setFont(font8)
        self.label_39.setStyleSheet(u"background: transparent;\n"
"color: black;")
        self.pushButton = QPushButton(self.card_ph_widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(250, 210, 80, 80))
        icon8 = QIcon()
        icon8.addFile(u":/img/gota-de-agua.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon8)
        self.pushButton.setIconSize(QSize(80, 80))
        self.label_7.raise_()
        self.label_10.raise_()
        self.label_14.raise_()
        self.label_9.raise_()
        self.label_39.raise_()
        self.label_13.raise_()
        self.pushButton.raise_()
        self.shadow_historial = QFrame(self.historial_page)
        self.shadow_historial.setObjectName(u"shadow_historial")
        self.shadow_historial.setGeometry(QRect(60, 390, 1275, 315))
        self.shadow_historial.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"	border-radius: 20px;")
        self.shadow_historial.setFrameShape(QFrame.Shape.StyledPanel)
        self.shadow_historial.setFrameShadow(QFrame.Shadow.Raised)
        self.top_widget_2 = QWidget(self.shadow_historial)
        self.top_widget_2.setObjectName(u"top_widget_2")
        self.top_widget_2.setGeometry(QRect(0, 0, 1271, 310))
        self.top_widget_2.setStyleSheet(u"QWidget {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.010989 rgba(0, 170, 255, 255), stop:1 rgba(21, 232, 255, 255));\n"
"	border-radius: 20px;\n"
"}")
        self.widget = QWidget(self.top_widget_2)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(21, 20, 1231, 271))
        self.verticalLayout_7 = QVBoxLayout(self.widget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_7 = QSpacerItem(248, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)

        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(0, 50))
        self.label_11.setMaximumSize(QSize(16777215, 50))
        self.label_11.setFont(font9)
        self.label_11.setStyleSheet(u"	background: transparent;\n"
"	color: white;")

        self.horizontalLayout_6.addWidget(self.label_11)

        self.horizontalSpacer_8 = QSpacerItem(248, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_8)


        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        self.history = QWidget(self.widget)
        self.history.setObjectName(u"history")
        self.history.setMinimumSize(QSize(727, 200))

        self.verticalLayout_7.addWidget(self.history)

        self.frame_3 = QFrame(self.historial_page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(440, 60, 900, 312))
        self.frame_3.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"	border-radius: 20px;")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.top_widget = QWidget(self.frame_3)
        self.top_widget.setObjectName(u"top_widget")
        self.top_widget.setGeometry(QRect(0, 0, 896, 310))
        self.top_widget.setStyleSheet(u"QWidget {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.010989 rgba(0, 170, 255, 255), stop:1 rgba(21, 232, 255, 255));\n"
"	border-radius: 20px;\n"
"}")
        self.widget1 = QWidget(self.top_widget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(11, 30, 861, 260))
        self.verticalLayout_6 = QVBoxLayout(self.widget1)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_2 = QSpacerItem(208, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.label_12 = QLabel(self.widget1)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(0, 50))
        self.label_12.setMaximumSize(QSize(16777215, 50))
        self.label_12.setFont(font9)
        self.label_12.setStyleSheet(u"	background: transparent;\n"
"	color: white;")

        self.horizontalLayout_5.addWidget(self.label_12)

        self.horizontalSpacer_6 = QSpacerItem(208, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.realTime = QWidget(self.widget1)
        self.realTime.setObjectName(u"realTime")
        self.realTime.setMinimumSize(QSize(727, 200))

        self.verticalLayout_6.addWidget(self.realTime)

        self.stackedWidget.addWidget(self.historial_page)
        self.ayuda_page = QWidget()
        self.ayuda_page.setObjectName(u"ayuda_page")
        self.stackAyuda = QStackedWidget(self.ayuda_page)
        self.stackAyuda.setObjectName(u"stackAyuda")
        self.stackAyuda.setGeometry(QRect(250, 10, 1421, 981))
        self.stackAyuda.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.ph = QWidget()
        self.ph.setObjectName(u"ph")
        self.gridLayout_8 = QGridLayout(self.ph)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.plainTextEdit = QPlainTextEdit(self.ph)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.gridLayout_8.addWidget(self.plainTextEdit, 0, 0, 1, 1)

        self.stackAyuda.addWidget(self.ph)
        self.ce = QWidget()
        self.ce.setObjectName(u"ce")
        self.gridLayout_7 = QGridLayout(self.ce)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.plainTextEdit_2 = QPlainTextEdit(self.ce)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")

        self.gridLayout_7.addWidget(self.plainTextEdit_2, 0, 0, 1, 1)

        self.stackAyuda.addWidget(self.ce)
        self.tmp = QWidget()
        self.tmp.setObjectName(u"tmp")
        self.gridLayout_9 = QGridLayout(self.tmp)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.plainTextEdit_3 = QPlainTextEdit(self.tmp)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")

        self.gridLayout_9.addWidget(self.plainTextEdit_3, 0, 0, 1, 1)

        self.stackAyuda.addWidget(self.tmp)
        self.bomb = QWidget()
        self.bomb.setObjectName(u"bomb")
        self.plainTextEdit_4 = QPlainTextEdit(self.bomb)
        self.plainTextEdit_4.setObjectName(u"plainTextEdit_4")
        self.plainTextEdit_4.setGeometry(QRect(10, 0, 1391, 971))
        self.stackAyuda.addWidget(self.bomb)
        self.bv = QWidget()
        self.bv.setObjectName(u"bv")
        self.label_4 = QLabel(self.bv)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(180, 190, 801, 161))
        font10 = QFont()
        font10.setPointSize(40)
        self.label_4.setFont(font10)
        self.stackAyuda.addWidget(self.bv)
        self.listWidget = QListWidget(self.ayuda_page)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(0, 0, 250, 1001))
        self.listWidget.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.listWidget.setStyleSheet(u"QWidget {\n"
"    background-color: #f9f9f9;  /* Fondo blanco suave */\n"
"    color: #333333;  /* Texto oscuro para buen contraste */\n"
"}\n"
"\n"
"QListWidget {\n"
"    background-color: #ffffff;  /* Fondo blanco para la lista */\n"
"    border: 1px solid #e0e0e0;  /* Borde gris claro */\n"
"    border-radius: 10px;  /* Bordes redondeados */\n"
"    padding: 5px;  /* Espacio interno */\n"
"    margin: 10px;  /* Espacio externo */\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    padding: 10px;  /* Espacio entre los \u00edtems */\n"
"    border-radius: 8px;  /* Bordes redondeados para los \u00edtems */\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background-color: #e8f4fd;  /* Color suave de fondo al pasar el mouse */\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: #1F95EF;  /* Color azul suave cuando el \u00edtem est\u00e1 seleccionado */\n"
"    color: white;  /* Texto blanco al seleccionar */\n"
"    font-weight: bold;  /* Poner en negrita el texto seleccionado */\n"
"}\n"
"\n"
"QPushBu"
                        "tton {\n"
"    color: white;\n"
"    text-align: left;\n"
"    height: 40px;\n"
"    border: none;\n"
"    padding-left: 15px;\n"
"    border-radius: 10px;\n"
"    background-color: #007AFF;  /* Azul suave */\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #F5FAFE;  /* Fondo muy suave para los botones seleccionados */\n"
"    color: #1F95EF;\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.stackedWidget.addWidget(self.ayuda_page)
        self.configuracion_page = QWidget()
        self.configuracion_page.setObjectName(u"configuracion_page")
        self.label_6 = QLabel(self.configuracion_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(160, 170, 271, 71))
        self.label_6.setFont(font1)
        self.stackedWidget.addWidget(self.configuracion_page)
        self.alerta_page = QWidget()
        self.alerta_page.setObjectName(u"alerta_page")
        self.gridLayout_6 = QGridLayout(self.alerta_page)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_5 = QSpacerItem(29, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.horizontalSpacer_4 = QSpacerItem(30, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.horizontalSpacer_3 = QSpacerItem(339, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.editSearch = QLineEdit(self.alerta_page)
        self.editSearch.setObjectName(u"editSearch")
        self.editSearch.setMinimumSize(QSize(260, 30))
        self.editSearch.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 2px solid #cccccc;\n"
"    border-radius: 15px;\n"
"    padding: 5px 10px;\n"
"    color: #333333;\n"
"    font-size: 14px;\n"
"    font-family: 'Segoe UI', sans-serif;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #aaaaaa;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #0078d7;\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.editSearch)

        self.pbSearch = QPushButton(self.alerta_page)
        self.pbSearch.setObjectName(u"pbSearch")
        self.pbSearch.setMinimumSize(QSize(40, 40))
        self.pbSearch.setStyleSheet(u"QPushButton {\n"
"background-color: #FFFFFF;\n"
"border-radius: 20;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: #aaffff;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/img/search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pbSearch.setIcon(icon9)

        self.horizontalLayout_4.addWidget(self.pbSearch)


        self.gridLayout_6.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.tabla_alertas = QTableWidget(self.alerta_page)
        if (self.tabla_alertas.columnCount() < 5):
            self.tabla_alertas.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabla_alertas.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla_alertas.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabla_alertas.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabla_alertas.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabla_alertas.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tabla_alertas.setObjectName(u"tabla_alertas")
        self.tabla_alertas.setMinimumSize(QSize(740, 450))
        self.tabla_alertas.setStyleSheet(u"QTableWidget {\n"
"    background-color: #ffffff;\n"
"    border: none;\n"
"    gridline-color: #f0f0f0;\n"
"    font-size: 14px;\n"
"    color: #333333;\n"
"    selection-background-color: #1F95EF;\n"
"    selection-color: #ffffff;\n"
"    alternate-background-color: #f9f9f9;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #ffffff;\n"
"    color: #1F95EF;\n"
"    padding: 4px 12px; /* Espaciado m\u00e1s controlado */\n"
"    font-weight: 600;\n"
"    font-size: 13px;\n"
"    border: none;\n"
"    border-bottom: 1px solid #e0e0e0;\n"
"    text-align: center; /* CENTRAR texto */\n"
"}\n"
"\n"
"QHeaderView::section:hover {\n"
"    background-color: #e6f4ff;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    padding: 6px 10px;\n"
"    border: none;\n"
"    text-align: center; /* CENTRAR contenido de celdas */\n"
"    transition: background-color 0.3s ease, color 0.3s ease;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #1F95EF;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QTableCornerBu"
                        "tton::section {\n"
"    background-color: #ffffff;\n"
"    border: none;\n"
"}\n"
"")
        self.tabla_alertas.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla_alertas.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tabla_alertas.verticalHeader().setCascadingSectionResizes(False)

        self.gridLayout_6.addWidget(self.tabla_alertas, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.alerta_page)
        self.bienvenida_page = QWidget()
        self.bienvenida_page.setObjectName(u"bienvenida_page")
        self.label_5 = QLabel(self.bienvenida_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(250, 190, 771, 211))
        font11 = QFont()
        font11.setPointSize(50)
        self.label_5.setFont(font11)
        self.prueba_frame = QFrame(self.bienvenida_page)
        self.prueba_frame.setObjectName(u"prueba_frame")
        self.prueba_frame.setGeometry(QRect(240, 110, 511, 91))
        self.prueba_frame.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"border-radius: 15px;")
        self.prueba_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.prueba_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.stackedWidget.addWidget(self.bienvenida_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout_4.addWidget(self.main_menu, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_12.toggled.connect(self.icon_widget.setHidden)
        self.pushButton_12.toggled.connect(self.icon_name_widget.setVisible)
        self.ayuda_1.toggled.connect(self.ayuda_2.setChecked)
        self.historial_1.toggled.connect(self.historial_2.setChecked)
        self.alerta_1.toggled.connect(self.alerta_2.setChecked)
        self.estado_1.toggled.connect(self.estado_2.setChecked)
        self.configuracion_1.toggled.connect(self.configuracion_2.setChecked)
        self.estado_2.toggled.connect(self.estado_1.setChecked)
        self.alerta_2.toggled.connect(self.alerta_1.setChecked)
        self.historial_2.toggled.connect(self.historial_1.setChecked)
        self.ayuda_2.toggled.connect(self.ayuda_1.setChecked)
        self.configuracion_2.toggled.connect(self.configuracion_1.setChecked)
        self.salir_1.toggled.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(5)
        self.stackAyuda.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.estado_1.setText("")
        self.alerta_1.setText("")
        self.historial_1.setText("")
        self.ayuda_1.setText("")
        self.configuracion_1.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Hydrobyte", None))
        self.estado_2.setText(QCoreApplication.translate("MainWindow", u"Estado ", None))
        self.alerta_2.setText(QCoreApplication.translate("MainWindow", u"Alertas", None))
        self.historial_2.setText(QCoreApplication.translate("MainWindow", u"Historial", None))
        self.ayuda_2.setText(QCoreApplication.translate("MainWindow", u"Ayuda", None))
        self.configuracion_2.setText(QCoreApplication.translate("MainWindow", u"Configuraciones", None))
        self.pushButton_12.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Historial Page", None))
        self.pushButton_11.setText("")
        self.salir_1.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Ph", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"5, 625", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Activo", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"9th Aug 2021", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Ph", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"5, 625", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Activo", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"9th Aug 2021", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Ph", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"5, 625", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Activo", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"9th Aug 2021", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Ph", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"5, 625", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Activo", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"9th Aug 2021", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Ph", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"5, 625", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Activo", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"9th Aug 2021", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Ph", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"5, 625", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Activo", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"9th Aug 2021", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"PH", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"CE", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Temperatura", None))

        self.label_7.setText(QCoreApplication.translate("MainWindow", u"PH", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"793", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Activo", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Estable", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"793", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Activo", None))
        self.pushButton.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Historial", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Tiempo Real", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"\u00bfSab\u00edas que todo a tu alrededor tiene un pH?\n"
"\n"
"El pH (potencial de hidr\u00f3geno) es una forma de medir qu\u00e9 tan \u00e1cido o alcalino (b\u00e1sico) es algo. Vamos a descubrirlo paso a paso.\n"
"\n"
"\u00bfQu\u00e9 es el pH?\n"
"Imagina que el pH es una escala que va del 0 al 14. En esta escala:\n"
"\n"
"0 a 6: \u00a1\u00c1cido!\n"
"\n"
"\u00a1El vinagre y el jugo de lim\u00f3n son \u00e1cidos! Son como los superh\u00e9roes del mundo \u00e1cido.\n"
"\n"
"7: \u00a1Neutral!\n"
"\n"
"El agua pura tiene un pH de 7. Ni \u00e1cido, ni alcalino. \u00a1Es como un \u00e1rbitro imparcial!\n"
"\n"
"8 a 14: \u00a1Alcalino o b\u00e1sico!\n"
"\n"
"Las soluciones como el bicarbonato de sodio son b\u00e1sicas. Son como los \"calmantes\" del mundo qu\u00edmico.\n"
"\n"
"\u00bfPor qu\u00e9 es importante el pH?\n"
"El pH afecta muchas cosas que usamos todos los d\u00edas, como:\n"
"\n"
"Tu cuerpo\n"
"\n"
"Tu est\u00f3mago necesita un pH \u00e1cido para digerir la comida.\n"
"\n"
"Pero tu sangre debe tener u"
                        "n pH casi neutro, \u00a1para que todo funcione correctamente!\n"
"\n"
"La naturaleza\n"
"\n"
"El pH del suelo es clave para que las plantas crezcan bien. Si el suelo es demasiado \u00e1cido o b\u00e1sico, las plantas pueden no crecer.\n"
"\n"
"La comida\n"
"\n"
"El pH en la comida tambi\u00e9n es importante. Un pH demasiado bajo (como en los jugos \u00e1cidos) puede hacer que algunos alimentos se descompongan r\u00e1pidamente.\n"
"\n"
"\u00bfC\u00f3mo medimos el pH?\n"
"Hay diferentes formas de medir el pH, como:\n"
"\n"
"Papeles indicadores: Se vuelven de diferentes colores seg\u00fan si la soluci\u00f3n es \u00e1cida o b\u00e1sica.\n"
"\n"
"Medidores electr\u00f3nicos: Los m\u00e1s avanzados y precisos, perfectos para los laboratorios.\n"
"\n"
"Un dato curioso...\n"
"El pH perfecto para el cuerpo humano es ligeramente b\u00e1sico, alrededor de 7.4. \u00a1Es como un equilibrio perfecto entre \u00e1cido y alcalino!", None))
        self.plainTextEdit_2.setPlainText(QCoreApplication.translate("MainWindow", u"\u00bfSab\u00edas que algunos materiales permiten el paso de la electricidad mejor que otros?\n"
"\n"
"Eso se debe a su conductividad el\u00e9ctrica, que es la capacidad que tiene un material para conducir una corriente el\u00e9ctrica. Vamos a entenderlo paso a paso.\n"
"\n"
"\u00bfQu\u00e9 es la conductividad el\u00e9ctrica?\n"
"La conductividad el\u00e9ctrica mide qu\u00e9 tan f\u00e1cil puede moverse una corriente el\u00e9ctrica a trav\u00e9s de un material. Depende de cu\u00e1nto dejan pasar los electrones.\n"
"\n"
"Materiales con alta conductividad permiten que la electricidad fluya f\u00e1cilmente.\n"
"\n"
"Materiales con baja conductividad resisten el paso de la electricidad.\n"
"\n"
"Ejemplos de buenos conductores:\n"
"\n"
"Metales como el cobre, la plata y el oro.\n"
"\n"
"El agua con sales disueltas.\n"
"\n"
"Ejemplos de malos conductores o aislantes:\n"
"\n"
"Pl\u00e1sticos\n"
"\n"
"Madera seca\n"
"\n"
"Goma\n"
"\n"
"\u00bfPor qu\u00e9 es importante la conductividad el\u00e9ctrica?\n"
"La conductivi"
                        "dad es fundamental en muchos aspectos de la vida diaria:\n"
"\n"
"Electricidad en casa: Los cables que llevan electricidad est\u00e1n hechos de cobre, un excelente conductor.\n"
"\n"
"Dispositivos electr\u00f3nicos: El dise\u00f1o de computadoras y tel\u00e9fonos depende de materiales que conducen electricidad de forma controlada.\n"
"\n"
"Seguridad: Los aislantes protegen a las personas de sufrir descargas el\u00e9ctricas.\n"
"\n"
"\u00bfC\u00f3mo se mide la conductividad el\u00e9ctrica?\n"
"Se utiliza un aparato llamado conduct\u00edmetro, que mide cu\u00e1nta corriente pasa a trav\u00e9s de un material en condiciones espec\u00edficas.\n"
"\n"
"Dato curioso:\n"
"La plata es el mejor conductor el\u00e9ctrico que existe, pero debido a su alto costo, normalmente se usa cobre en la mayor\u00eda de los cables.", None))
        self.plainTextEdit_3.setPlainText(QCoreApplication.translate("MainWindow", u"\u00bfSab\u00edas que la temperatura del agua es crucial para el crecimiento de las hortalizas?\n"
"\n"
"La temperatura del agua que se usa en el riego puede afectar directamente la salud, el crecimiento y la productividad de las plantas.\n"
"\n"
"\u00bfPor qu\u00e9 importa la temperatura del agua?\n"
"Cuando riegas las hortalizas:\n"
"\n"
"Agua demasiado fr\u00eda: Puede \"estresar\" a las plantas, ralentizar su crecimiento y afectar la absorci\u00f3n de nutrientes.\n"
"\n"
"Agua demasiado caliente: Puede da\u00f1ar las ra\u00edces sensibles y reducir la disponibilidad de ox\u00edgeno en el suelo.\n"
"\n"
"\u00bfCu\u00e1l es la temperatura ideal del agua para las hortalizas?\n"
"Lo m\u00e1s recomendable es que el agua est\u00e9 entre 18 y 24 grados Celsius. A esta temperatura:\n"
"\n"
"Las ra\u00edces absorben mejor el agua y los nutrientes.\n"
"\n"
"Se minimiza el riesgo de enfermedades por hongos o bacterias.\n"
"\n"
"Se favorece un desarrollo vigoroso y saludable.\n"
"\n"
"Consejos para un riego efectivo:\n"
""
                        "\n"
"Riega en las primeras horas de la ma\u00f1ana o al final de la tarde para evitar cambios bruscos de temperatura.\n"
"\n"
"Evita usar agua de pozos muy fr\u00edos directamente, especialmente en climas c\u00e1lidos.\n"
"\n"
"Si es posible, deja reposar el agua al sol un tiempo antes de regar para equilibrar su temperatura.\n"
"\n"
"Dato interesante:\n"
"Algunas hortalizas, como el tomate y el pepino, son especialmente sensibles a la temperatura del agua, y un riego adecuado puede marcar la diferencia entre una planta fuerte o una planta d\u00e9bil.\n"
"\n"
"", None))
        self.plainTextEdit_4.setPlainText(QCoreApplication.translate("MainWindow", u"\u00bfSab\u00edas que las bombas de agua son esenciales para mover l\u00edquidos en muchos sistemas agr\u00edcolas e industriales?\n"
"\n"
"Entre las m\u00e1s utilizadas est\u00e1n las bombas de circulaci\u00f3n y las bombas perist\u00e1lticas.\n"
"\n"
"\u00bfQu\u00e9 es una bomba de circulaci\u00f3n?\n"
"Las bombas de circulaci\u00f3n son dispositivos que mantienen el flujo constante de agua u otros l\u00edquidos en un sistema cerrado.\n"
"Son ideales para:\n"
"\n"
"Sistemas de riego.\n"
"\n"
"Sistemas de calefacci\u00f3n o enfriamiento.\n"
"\n"
"Mantenimiento de nutrientes en sistemas hidrop\u00f3nicos.\n"
"\n"
"Funcionan empujando el agua de manera continua, asegurando que siempre haya movimiento y evitando el estancamiento.\n"
"\n"
"\u00bfQu\u00e9 es una bomba perist\u00e1ltica?\n"
"Una bomba perist\u00e1ltica transporta l\u00edquidos a trav\u00e9s de un tubo flexible que es comprimido de manera controlada.\n"
"Son especialmente \u00fatiles cuando:\n"
"\n"
"Se necesita mover l\u00edquidos de manera muy pre"
                        "cisa.\n"
"\n"
"El l\u00edquido debe evitar el contacto directo con partes mec\u00e1nicas.\n"
"\n"
"Se transportan l\u00edquidos viscosos, sensibles o con part\u00edculas s\u00f3lidas.\n"
"\n"
"Ventajas de cada tipo:\n"
"\n"
"Bombas de circulaci\u00f3n: Alta eficiencia en mover grandes vol\u00famenes de l\u00edquido de manera constante.\n"
"\n"
"Bombas perist\u00e1lticas: Precisi\u00f3n en el volumen transportado, ideal para dosificar fertilizantes o nutrientes en peque\u00f1as cantidades.\n"
"\n"
"Dato interesante:\n"
"En la agricultura moderna, muchas veces se combinan ambos tipos de bombas para asegurar que el agua y los nutrientes lleguen de forma continua y precisa a las plantas.", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Bienvenido a la pagina de ayuda", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Ph", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Conductividad Electrica", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Temperatura", None));
        ___qlistwidgetitem3 = self.listWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Bombas", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Configuracion Page", None))
        self.pbSearch.setText("")
        ___qtablewidgetitem = self.tabla_alertas.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tabla_alertas.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Sensor", None));
        ___qtablewidgetitem2 = self.tabla_alertas.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Mensaje", None));
        ___qtablewidgetitem3 = self.tabla_alertas.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Estado", None));
        ___qtablewidgetitem4 = self.tabla_alertas.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Fecha", None));
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Bienvenidos a HydroByte", None))
    # retranslateUi

