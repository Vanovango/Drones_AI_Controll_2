# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\settings_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        SettingsWindow.setObjectName("SettingsWindow")
        SettingsWindow.resize(600, 600)
        SettingsWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        SettingsWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        SettingsWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(SettingsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_start_demonstration = QtWidgets.QPushButton(self.centralwidget)
        self.button_start_demonstration.setEnabled(True)
        self.button_start_demonstration.setGeometry(QtCore.QRect(310, 500, 286, 75))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.button_start_demonstration.setFont(font)
        self.button_start_demonstration.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.button_start_demonstration.setMouseTracking(False)
        self.button_start_demonstration.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.button_start_demonstration.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.button_start_demonstration.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.button_start_demonstration.setAutoFillBackground(True)
        self.button_start_demonstration.setCheckable(False)
        self.button_start_demonstration.setAutoDefault(False)
        self.button_start_demonstration.setDefault(True)
        self.button_start_demonstration.setFlat(False)
        self.button_start_demonstration.setObjectName("button_start_demonstration")
        self.button_back = QtWidgets.QPushButton(self.centralwidget)
        self.button_back.setEnabled(True)
        self.button_back.setGeometry(QtCore.QRect(10, 500, 286, 75))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.button_back.setFont(font)
        self.button_back.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.button_back.setMouseTracking(False)
        self.button_back.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.button_back.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.button_back.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.button_back.setAutoFillBackground(True)
        self.button_back.setCheckable(False)
        self.button_back.setAutoDefault(False)
        self.button_back.setDefault(True)
        self.button_back.setFlat(False)
        self.button_back.setObjectName("button_back")
        self.label_main = QtWidgets.QLabel(self.centralwidget)
        self.label_main.setGeometry(QtCore.QRect(75, 10, 450, 110))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        self.label_main.setFont(font)
        self.label_main.setObjectName("label_main")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 250, 561, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_speed = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(15)
        self.label_speed.setFont(font)
        self.label_speed.setObjectName("label_speed")
        self.horizontalLayout_2.addWidget(self.label_speed)
        self.lineEdit_drone_speed = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_drone_speed.setFont(font)
        self.lineEdit_drone_speed.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_drone_speed.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_drone_speed.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_drone_speed.setDragEnabled(False)
        self.lineEdit_drone_speed.setObjectName("lineEdit_drone_speed")
        self.horizontalLayout_2.addWidget(self.lineEdit_drone_speed)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 330, 561, 71))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_n_drones = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(15)
        self.label_n_drones.setFont(font)
        self.label_n_drones.setObjectName("label_n_drones")
        self.horizontalLayout_3.addWidget(self.label_n_drones)
        self.lineEdit_n_drones = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_n_drones.setFont(font)
        self.lineEdit_n_drones.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_n_drones.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_n_drones.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_n_drones.setObjectName("lineEdit_n_drones")
        self.horizontalLayout_3.addWidget(self.lineEdit_n_drones)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 410, 561, 71))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_radius = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(15)
        self.label_radius.setFont(font)
        self.label_radius.setObjectName("label_radius")
        self.horizontalLayout_4.addWidget(self.label_radius)
        self.lineEdit_retransmission_radius = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_retransmission_radius.setFont(font)
        self.lineEdit_retransmission_radius.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_retransmission_radius.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_retransmission_radius.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_retransmission_radius.setObjectName("lineEdit_retransmission_radius")
        self.horizontalLayout_4.addWidget(self.lineEdit_retransmission_radius)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(20, 170, 561, 71))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_load_map = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(15)
        self.label_load_map.setFont(font)
        self.label_load_map.setObjectName("label_load_map")
        self.horizontalLayout_5.addWidget(self.label_load_map)
        self.button_open_map = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(15)
        self.button_open_map.setFont(font)
        self.button_open_map.setObjectName("button_open_map")
        self.horizontalLayout_5.addWidget(self.button_open_map)
        self.label_author = QtWidgets.QLabel(self.centralwidget)
        self.label_author.setGeometry(QtCore.QRect(0, 580, 141, 16))
        self.label_author.setObjectName("label_author")
        self.label_version = QtWidgets.QLabel(self.centralwidget)
        self.label_version.setGeometry(QtCore.QRect(560, 580, 41, 20))
        self.label_version.setObjectName("label_version")
        self.label_map_path = QtWidgets.QLabel(self.centralwidget)
        self.label_map_path.setGeometry(QtCore.QRect(20, 220, 561, 20))
        self.label_map_path.setText("")
        self.label_map_path.setAlignment(QtCore.Qt.AlignCenter)
        self.label_map_path.setObjectName("label_map_path")
        SettingsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SettingsWindow)
        QtCore.QMetaObject.connectSlotsByName(SettingsWindow)

    def retranslateUi(self, SettingsWindow):
        _translate = QtCore.QCoreApplication.translate
        SettingsWindow.setWindowTitle(_translate("SettingsWindow", "MainWindow"))
        self.button_start_demonstration.setText(_translate("SettingsWindow", "начать\n"
"демонстрацию"))
        self.button_back.setText(_translate("SettingsWindow", "назад"))
        self.label_main.setText(_translate("SettingsWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Корректировка </span></p><p align=\"center\"><span style=\" font-size:20pt;\">основных параметров</span></p></body></html>"))
        self.label_speed.setText(_translate("SettingsWindow", "Скорость дрона                    "))
        self.label_n_drones.setText(_translate("SettingsWindow", "Количество дронов             "))
        self.label_radius.setText(_translate("SettingsWindow", "Радиус ретранслятора        "))
        self.label_load_map.setText(_translate("SettingsWindow", "Загрузить карту                  "))
        self.button_open_map.setText(_translate("SettingsWindow", "Выбрать файл"))
        self.label_author.setText(_translate("SettingsWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#bcbcbc;\">Автор: Войтенко И. А.</span></p></body></html>"))
        self.label_version.setText(_translate("SettingsWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#bcbcbc;\">v.2.5</span></p></body></html>"))
