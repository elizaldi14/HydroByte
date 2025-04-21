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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(964, 607)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
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
        icon = QIcon()
        icon.addFile(u":/img/menu_black.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_12.setIcon(icon)
        self.pushButton_12.setIconSize(QSize(25, 25))
        self.pushButton_12.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.pushButton_12)

        self.horizontalSpacer = QSpacerItem(591, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.pushButton_11 = QPushButton(self.header_widget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setStyleSheet(u"border: none;")
        icon1 = QIcon()
        icon1.addFile(u":/img/notifications_black.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_11.setIcon(icon1)
        self.pushButton_11.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.pushButton_11)

        self.salir_1 = QPushButton(self.header_widget)
        self.salir_1.setObjectName(u"salir_1")
        self.salir_1.setStyleSheet(u"border: none;")
        icon2 = QIcon()
        icon2.addFile(u":/img/exit_black.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.salir_1.setIcon(icon2)
        self.salir_1.setIconSize(QSize(25, 25))
        self.salir_1.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.salir_1)


        self.verticalLayout_5.addWidget(self.header_widget)

        self.stackedWidget = QStackedWidget(self.main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: #F3F6FF;")
        self.estado_page = QWidget()
        self.estado_page.setObjectName(u"estado_page")
        self.label_7 = QLabel(self.estado_page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(260, 0, 171, 71))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_7.setFont(font)
        self.layoutWidget = QWidget(self.estado_page)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 80, 631, 391))
        self.gridLayout_2 = QGridLayout(self.layoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(20)
        self.gridLayout_2.setVerticalSpacing(10)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.layoutWidget)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"QFrame {\n"
"	background-color: #FFFFFF ;\n"
"	border-radius: 15px;\n"
" box-shadow: 3px 3px 5px rgba(0, 0, 0, 0.3);\n"
"}\n"
"\n"
"QFrame:hover {\n"
"	border: 1px solid #0055ff;\n"
"}\n"
"\n"
"")
        self.frame_8.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout_9 = QVBoxLayout(self.frame_8)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 20, 0, 20)
        self.label_4 = QLabel(self.frame_8)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"QLabel {\n"
"	color: rgb(152, 152, 152);\n"
"	border: none;\n"
"}")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_4)

        self.label_9 = QLabel(self.frame_8)
        self.label_9.setObjectName(u"label_9")
        font2 = QFont()
        font2.setPointSize(13)
        font2.setBold(True)
        self.label_9.setFont(font2)
        self.label_9.setStyleSheet(u"QLabel {\n"
"	color: rgb(199, 199, 199);\n"
"	border: none;\n"
"}")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_9)

        self.label_10 = QLabel(self.frame_8)
        self.label_10.setObjectName(u"label_10")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.label_10.setFont(font3)
        self.label_10.setStyleSheet(u"QLabel {\n"
"	color: rgb(70, 255, 3);\n"
"	border: none;\n"
"}")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_10)

        self.label_17 = QLabel(self.frame_8)
        self.label_17.setObjectName(u"label_17")
        font4 = QFont()
        font4.setPointSize(10)
        self.label_17.setFont(font4)
        self.label_17.setStyleSheet(u"QLabel {\n"
"	color: rgb(153, 153, 153);\n"
"	border: none;\n"
"}\n"
"")
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_17)


        self.gridLayout_2.addWidget(self.frame_8, 0, 0, 1, 1)

        self.frame_9 = QFrame(self.layoutWidget)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(25, 25, 25);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QFrame:hover {\n"
"	border: 1px solid rgb(255, 85, 0);\n"
"}")
        self.frame_9.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout_10 = QVBoxLayout(self.frame_9)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 20, 0, 20)
        self.label_18 = QLabel(self.frame_9)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font1)
        self.label_18.setStyleSheet(u"QLabel {\n"
"	color: rgb(152, 152, 152);\n"
"	border: none;\n"
"}")
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_18)

        self.label_19 = QLabel(self.frame_9)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font2)
        self.label_19.setStyleSheet(u"QLabel {\n"
"	color: rgb(199, 199, 199);\n"
"	border: none;\n"
"}")
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_19)

        self.label_20 = QLabel(self.frame_9)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font3)
        self.label_20.setStyleSheet(u"QLabel {\n"
"	color: rgb(70, 255, 3);\n"
"	border: none;\n"
"}")
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_20)

        self.label_21 = QLabel(self.frame_9)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font4)
        self.label_21.setStyleSheet(u"QLabel {\n"
"	color: rgb(153, 153, 153);\n"
"	border: none;\n"
"}\n"
"")
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_21)


        self.gridLayout_2.addWidget(self.frame_9, 0, 1, 1, 1)

        self.frame_10 = QFrame(self.layoutWidget)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(25, 25, 25);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QFrame:hover {\n"
"	border: 1px solid rgb(255, 85, 0);\n"
"}")
        self.frame_10.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout_11 = QVBoxLayout(self.frame_10)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 20, 0, 20)
        self.label_22 = QLabel(self.frame_10)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font1)
        self.label_22.setStyleSheet(u"QLabel {\n"
"	color: rgb(152, 152, 152);\n"
"	border: none;\n"
"}")
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_22)

        self.label_23 = QLabel(self.frame_10)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font2)
        self.label_23.setStyleSheet(u"QLabel {\n"
"	color: rgb(199, 199, 199);\n"
"	border: none;\n"
"}")
        self.label_23.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_23)

        self.label_24 = QLabel(self.frame_10)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font3)
        self.label_24.setStyleSheet(u"QLabel {\n"
"	color: rgb(70, 255, 3);\n"
"	border: none;\n"
"}")
        self.label_24.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_24)

        self.label_25 = QLabel(self.frame_10)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font4)
        self.label_25.setStyleSheet(u"QLabel {\n"
"	color: rgb(153, 153, 153);\n"
"	border: none;\n"
"}\n"
"")
        self.label_25.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_25)


        self.gridLayout_2.addWidget(self.frame_10, 0, 2, 1, 1)

        self.frame_13 = QFrame(self.layoutWidget)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(25, 25, 25);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QFrame:hover {\n"
"	border: 1px solid rgb(255, 85, 0);\n"
"}")
        self.frame_13.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout_14 = QVBoxLayout(self.frame_13)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 20, 0, 20)
        self.label_34 = QLabel(self.frame_13)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font1)
        self.label_34.setStyleSheet(u"QLabel {\n"
"	color: rgb(152, 152, 152);\n"
"	border: none;\n"
"}")
        self.label_34.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_34)

        self.label_35 = QLabel(self.frame_13)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font2)
        self.label_35.setStyleSheet(u"QLabel {\n"
"	color: rgb(199, 199, 199);\n"
"	border: none;\n"
"}")
        self.label_35.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_35)

        self.label_36 = QLabel(self.frame_13)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font3)
        self.label_36.setStyleSheet(u"QLabel {\n"
"	color: rgb(70, 255, 3);\n"
"	border: none;\n"
"}")
        self.label_36.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_36)

        self.label_37 = QLabel(self.frame_13)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font4)
        self.label_37.setStyleSheet(u"QLabel {\n"
"	color: rgb(153, 153, 153);\n"
"	border: none;\n"
"}\n"
"")
        self.label_37.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_37)


        self.gridLayout_2.addWidget(self.frame_13, 1, 0, 1, 1)

        self.frame_11 = QFrame(self.layoutWidget)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(25, 25, 25);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QFrame:hover {\n"
"	border: 1px solid rgb(255, 85, 0);\n"
"}")
        self.frame_11.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout_12 = QVBoxLayout(self.frame_11)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 20, 0, 20)
        self.label_26 = QLabel(self.frame_11)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font1)
        self.label_26.setStyleSheet(u"QLabel {\n"
"	color: rgb(152, 152, 152);\n"
"	border: none;\n"
"}")
        self.label_26.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_26)

        self.label_27 = QLabel(self.frame_11)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font2)
        self.label_27.setStyleSheet(u"QLabel {\n"
"	color: rgb(199, 199, 199);\n"
"	border: none;\n"
"}")
        self.label_27.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_27)

        self.label_28 = QLabel(self.frame_11)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font3)
        self.label_28.setStyleSheet(u"QLabel {\n"
"	color: rgb(70, 255, 3);\n"
"	border: none;\n"
"}")
        self.label_28.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_28)

        self.label_29 = QLabel(self.frame_11)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font4)
        self.label_29.setStyleSheet(u"QLabel {\n"
"	color: rgb(153, 153, 153);\n"
"	border: none;\n"
"}\n"
"")
        self.label_29.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_29)


        self.gridLayout_2.addWidget(self.frame_11, 1, 1, 1, 1)

        self.frame_12 = QFrame(self.layoutWidget)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(25, 25, 25);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QFrame:hover {\n"
"	border: 1px solid rgb(255, 85, 0);\n"
"}")
        self.frame_12.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout_13 = QVBoxLayout(self.frame_12)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 20, 0, 20)
        self.label_30 = QLabel(self.frame_12)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font1)
        self.label_30.setStyleSheet(u"QLabel {\n"
"	color: rgb(152, 152, 152);\n"
"	border: none;\n"
"}")
        self.label_30.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_30)

        self.label_31 = QLabel(self.frame_12)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font2)
        self.label_31.setStyleSheet(u"QLabel {\n"
"	color: rgb(199, 199, 199);\n"
"	border: none;\n"
"}")
        self.label_31.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_31)

        self.label_32 = QLabel(self.frame_12)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font3)
        self.label_32.setStyleSheet(u"QLabel {\n"
"	color: rgb(70, 255, 3);\n"
"	border: none;\n"
"}")
        self.label_32.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_32)

        self.label_33 = QLabel(self.frame_12)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font4)
        self.label_33.setStyleSheet(u"QLabel {\n"
"	color: rgb(153, 153, 153);\n"
"	border: none;\n"
"}\n"
"")
        self.label_33.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_33)


        self.gridLayout_2.addWidget(self.frame_12, 1, 2, 1, 1)

        self.stackedWidget.addWidget(self.estado_page)
        self.historial_page = QWidget()
        self.historial_page.setObjectName(u"historial_page")
        self.label_8 = QLabel(self.historial_page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 0, 211, 71))
        self.label_8.setFont(font)
        self.widget = QWidget(self.historial_page)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 80, 271, 181))
        self.stackedWidget.addWidget(self.historial_page)
        self.ayuda_page = QWidget()
        self.ayuda_page.setObjectName(u"ayuda_page")
        self.label_5 = QLabel(self.ayuda_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(220, 160, 171, 71))
        self.label_5.setFont(font)
        self.stackedWidget.addWidget(self.ayuda_page)
        self.configuracion_page = QWidget()
        self.configuracion_page.setObjectName(u"configuracion_page")
        self.label_6 = QLabel(self.configuracion_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(160, 170, 271, 71))
        self.label_6.setFont(font)
        self.stackedWidget.addWidget(self.configuracion_page)
        self.alerta_page = QWidget()
        self.alerta_page.setObjectName(u"alerta_page")
        self.horizontalLayout_4 = QHBoxLayout(self.alerta_page)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tableWidget = QTableWidget(self.alerta_page)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 2):
            self.tableWidget.setRowCount(2)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(1, 2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setItem(1, 3, __qtablewidgetitem13)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"    QTableWidget {\n"
"        background-color: #f0f0f0;\n"
"        border: 1px solid #d3d3d3;\n"
"        gridline-color: #ccc;\n"
"        font-size: 14px;\n"
"    }\n"
"\n"
"    QHeaderView::section {\n"
"        background-color: #3d8cd6;\n"
"        color: white;\n"
"        padding: 4px;\n"
"        font-weight: bold;\n"
"        border: 1px solid #ccc;\n"
"    }\n"
"\n"
"    QTableWidget::item {\n"
"        padding: 5px;\n"
"    }\n"
"\n"
"    QTableWidget::item:selected {\n"
"        background-color: #a0c4ff;\n"
"        color: black;\n"
"    }")

        self.horizontalLayout_4.addWidget(self.tableWidget)

        self.stackedWidget.addWidget(self.alerta_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main_menu, 0, 2, 1, 1)

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
        icon3 = QIcon()
        icon3.addFile(u":/img/home_white.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/img/home_black.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.estado_1.setIcon(icon3)
        self.estado_1.setIconSize(QSize(25, 25))
        self.estado_1.setCheckable(True)
        self.estado_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.estado_1)

        self.alerta_1 = QPushButton(self.icon_widget)
        self.alerta_1.setObjectName(u"alerta_1")
        icon4 = QIcon()
        icon4.addFile(u":/img/warning_white.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/img/warning_black.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.alerta_1.setIcon(icon4)
        self.alerta_1.setIconSize(QSize(25, 25))
        self.alerta_1.setCheckable(True)
        self.alerta_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.alerta_1)

        self.historial_1 = QPushButton(self.icon_widget)
        self.historial_1.setObjectName(u"historial_1")
        icon5 = QIcon()
        icon5.addFile(u":/img/timeline__white.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/img/timeline_black.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.historial_1.setIcon(icon5)
        self.historial_1.setIconSize(QSize(25, 25))
        self.historial_1.setCheckable(True)
        self.historial_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.historial_1)

        self.ayuda_1 = QPushButton(self.icon_widget)
        self.ayuda_1.setObjectName(u"ayuda_1")
        icon6 = QIcon()
        icon6.addFile(u":/img/help__white.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon6.addFile(u":/img/help_black.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.ayuda_1.setIcon(icon6)
        self.ayuda_1.setIconSize(QSize(25, 25))
        self.ayuda_1.setCheckable(True)
        self.ayuda_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.ayuda_1)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 315, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.configuracion_1 = QPushButton(self.icon_widget)
        self.configuracion_1.setObjectName(u"configuracion_1")
        icon7 = QIcon()
        icon7.addFile(u":/img/settings_white.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon7.addFile(u":/img/settings_black.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.configuracion_1.setIcon(icon7)
        self.configuracion_1.setIconSize(QSize(25, 25))
        self.configuracion_1.setCheckable(True)
        self.configuracion_1.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.configuracion_1)


        self.gridLayout.addWidget(self.icon_widget, 0, 0, 1, 1)

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
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(True)
        self.label_3.setFont(font5)
        self.label_3.setTextFormat(Qt.TextFormat.PlainText)

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 15, -1, -1)
        self.estado_2 = QPushButton(self.icon_name_widget)
        self.estado_2.setObjectName(u"estado_2")
        self.estado_2.setIcon(icon3)
        self.estado_2.setIconSize(QSize(25, 25))
        self.estado_2.setCheckable(True)
        self.estado_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.estado_2)

        self.alerta_2 = QPushButton(self.icon_name_widget)
        self.alerta_2.setObjectName(u"alerta_2")
        self.alerta_2.setIcon(icon4)
        self.alerta_2.setIconSize(QSize(25, 25))
        self.alerta_2.setCheckable(True)
        self.alerta_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.alerta_2)

        self.historial_2 = QPushButton(self.icon_name_widget)
        self.historial_2.setObjectName(u"historial_2")
        self.historial_2.setIcon(icon5)
        self.historial_2.setIconSize(QSize(25, 25))
        self.historial_2.setCheckable(True)
        self.historial_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.historial_2)

        self.ayuda_2 = QPushButton(self.icon_name_widget)
        self.ayuda_2.setObjectName(u"ayuda_2")
        self.ayuda_2.setIcon(icon6)
        self.ayuda_2.setIconSize(QSize(25, 25))
        self.ayuda_2.setCheckable(True)
        self.ayuda_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.ayuda_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 315, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.configuracion_2 = QPushButton(self.icon_name_widget)
        self.configuracion_2.setObjectName(u"configuracion_2")
        self.configuracion_2.setIcon(icon7)
        self.configuracion_2.setIconSize(QSize(25, 25))
        self.configuracion_2.setCheckable(True)
        self.configuracion_2.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.configuracion_2)


        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)

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

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_12.setText("")
        self.pushButton_11.setText("")
        self.salir_1.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Estado Page", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Ph", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"5, 625", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Activo", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"9th Aug 2021", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Ph", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"5, 625", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Activo", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"9th Aug 2021", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Ph", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"5, 625", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Activo", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"9th Aug 2021", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Ph", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"5, 625", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Activo", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"9th Aug 2021", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Ph", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"5, 625", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Activo", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"9th Aug 2021", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Ph", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"5, 625", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Activo", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"9th Aug 2021", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Historial Page", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Ayuda Page", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Configuracion Page", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Alerta", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Nivel", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Estado", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem6 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"dd", None));
        ___qtablewidgetitem7 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"d", None));
        ___qtablewidgetitem8 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"d", None));
        ___qtablewidgetitem9 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"d", None));
        ___qtablewidgetitem10 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"aa", None));
        ___qtablewidgetitem11 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"a", None));
        ___qtablewidgetitem12 = self.tableWidget.item(1, 2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"a", None));
        ___qtablewidgetitem13 = self.tableWidget.item(1, 3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"a", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

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
    # retranslateUi

