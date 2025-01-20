# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class UiMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        MainWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        MainWindow.setIconSize(QtCore.QSize(50, 50))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 280, 581, 111))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_start_demonstration = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.button_start_demonstration.setEnabled(True)
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
        self.horizontalLayout.addWidget(self.button_start_demonstration)
        self.button_model_settings = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.button_model_settings.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.button_model_settings.setFont(font)
        self.button_model_settings.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.button_model_settings.setMouseTracking(False)
        self.button_model_settings.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.button_model_settings.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.button_model_settings.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.button_model_settings.setAutoFillBackground(True)
        self.button_model_settings.setCheckable(False)
        self.button_model_settings.setAutoDefault(False)
        self.button_model_settings.setDefault(True)
        self.button_model_settings.setFlat(False)
        self.button_model_settings.setObjectName("button_model_settings")
        self.horizontalLayout.addWidget(self.button_model_settings)
        self.label_main = QtWidgets.QLabel(self.centralwidget)
        self.label_main.setGeometry(QtCore.QRect(0, 20, 601, 171))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(20)
        self.label_main.setFont(font)
        self.label_main.setToolTipDuration(-1)
        self.label_main.setObjectName("label_main")
        self.label_author = QtWidgets.QLabel(self.centralwidget)
        self.label_author.setGeometry(QtCore.QRect(0, 380, 141, 16))
        self.label_author.setObjectName("label_author")
        self.label_version = QtWidgets.QLabel(self.centralwidget)
        self.label_version.setGeometry(QtCore.QRect(560, 380, 41, 20))
        self.label_version.setObjectName("label_version")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_start_demonstration.setText(_translate("MainWindow", "начать\n"
                                                                         "демонстрацию"))
        self.button_model_settings.setText(_translate("MainWindow", "перейти к\n"
                                                                    "настройкам"))
        self.label_main.setText(_translate("MainWindow",
                                           "<html><head/><body><p align=\"center\">Система</p><p align=\"center\">интеллектуального управления</p><p align=\"center\">роем БпЛА</p></body></html>"))
        self.label_author.setText(_translate("MainWindow",
                                             "<html><head/><body><p align=\"center\"><span style=\" color:#bcbcbc;\">Автор: Войтенко И. А.</span></p></body></html>"))
        self.label_version.setText(_translate("MainWindow",
                                              "<html><head/><body><p align=\"center\"><span style=\" color:#bcbcbc;\">v.2.7</span></p></body></html>"))

