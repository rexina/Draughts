# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindowUI.ui'
#
# Created: Fri Mar 07 23:44:56 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(967, 744)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(760, 450, 120, 146))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.configButton = QtGui.QPushButton(self.layoutWidget)
        self.configButton.setObjectName(_fromUtf8("configButton"))
        self.gridLayout.addWidget(self.configButton, 1, 0, 1, 1)
        self.calibrateCornersButton = QtGui.QPushButton(self.layoutWidget)
        self.calibrateCornersButton.setObjectName(_fromUtf8("calibrateCornersButton"))
        self.gridLayout.addWidget(self.calibrateCornersButton, 2, 0, 1, 1)
        self.nxtControlButton = QtGui.QPushButton(self.layoutWidget)
        self.nxtControlButton.setObjectName(_fromUtf8("nxtControlButton"))
        self.gridLayout.addWidget(self.nxtControlButton, 0, 0, 1, 1)
        self.makeMoveButton = QtGui.QPushButton(self.layoutWidget)
        self.makeMoveButton.setObjectName(_fromUtf8("makeMoveButton"))
        self.gridLayout.addWidget(self.makeMoveButton, 3, 0, 1, 1)
        self.saveSettingsButton = QtGui.QPushButton(self.layoutWidget)
        self.saveSettingsButton.setObjectName(_fromUtf8("saveSettingsButton"))
        self.gridLayout.addWidget(self.saveSettingsButton, 4, 0, 1, 1)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(90, 0, 612, 631))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.Image = QtGui.QWidget()
        self.Image.setObjectName(_fromUtf8("Image"))
        self.imageNormal = QtGui.QGraphicsView(self.Image)
        self.imageNormal.setGeometry(QtCore.QRect(0, 0, 605, 605))
        self.imageNormal.setObjectName(_fromUtf8("imageNormal"))
        self.tabWidget.addTab(self.Image, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.imageEdges = QtGui.QGraphicsView(self.tab_2)
        self.imageEdges.setGeometry(QtCore.QRect(0, 0, 605, 605))
        self.imageEdges.setObjectName(_fromUtf8("imageEdges"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.connectionStatusLabel = QtGui.QLabel(self.centralwidget)
        self.connectionStatusLabel.setGeometry(QtCore.QRect(740, 650, 131, 16))
        self.connectionStatusLabel.setObjectName(_fromUtf8("connectionStatusLabel"))
        self.tabWidget_2 = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget_2.setGeometry(QtCore.QRect(700, 0, 261, 441))
        self.tabWidget_2.setAutoFillBackground(True)
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.movesListTextBrowser = QtGui.QTextBrowser(self.tab)
        self.movesListTextBrowser.setGeometry(QtCore.QRect(0, 0, 256, 421))
        self.movesListTextBrowser.setObjectName(_fromUtf8("movesListTextBrowser"))
        self.tabWidget_2.addTab(self.tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.logsTextBrowser = QtGui.QTextBrowser(self.tab_3)
        self.logsTextBrowser.setGeometry(QtCore.QRect(0, 0, 256, 421))
        self.logsTextBrowser.setObjectName(_fromUtf8("logsTextBrowser"))
        self.tabWidget_2.addTab(self.tab_3, _fromUtf8(""))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(105, 640, 601, 58))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(30)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(30)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.label_4 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(30)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.label_5 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(30)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout.addWidget(self.label_5)
        self.label_8 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(30)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout.addWidget(self.label_8)
        self.label_6 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(30)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout.addWidget(self.label_6)
        self.label_7 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(30)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout.addWidget(self.label_7)
        self.widget1 = QtGui.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(40, 11, 26, 611))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget1)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_11 = QtGui.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(30)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout.addWidget(self.label_11)
        self.label_10 = QtGui.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(30)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout.addWidget(self.label_10)
        self.label_12 = QtGui.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(30)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.verticalLayout.addWidget(self.label_12)
        self.label_13 = QtGui.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(30)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalLayout.addWidget(self.label_13)
        self.label_14 = QtGui.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(30)
        self.label_14.setFont(font)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.verticalLayout.addWidget(self.label_14)
        self.label_15 = QtGui.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(30)
        self.label_15.setFont(font)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.verticalLayout.addWidget(self.label_15)
        self.label_16 = QtGui.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(30)
        self.label_16.setFont(font)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.verticalLayout.addWidget(self.label_16)
        self.label_9 = QtGui.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(30)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout.addWidget(self.label_9)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 967, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuTest = QtGui.QMenu(self.menubar)
        self.menuTest.setObjectName(_fromUtf8("menuTest"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNXT_Control = QtGui.QAction(MainWindow)
        self.actionNXT_Control.setObjectName(_fromUtf8("actionNXT_Control"))
        self.actionConfig = QtGui.QAction(MainWindow)
        self.actionConfig.setObjectName(_fromUtf8("actionConfig"))
        self.menuTest.addAction(self.actionNXT_Control)
        self.menuTest.addAction(self.actionConfig)
        self.menubar.addAction(self.menuTest.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Draughts player", None))
        self.configButton.setText(_translate("MainWindow", "Config", None))
        self.calibrateCornersButton.setText(_translate("MainWindow", "Calibrate corners", None))
        self.nxtControlButton.setText(_translate("MainWindow", "NXT control", None))
        self.makeMoveButton.setText(_translate("MainWindow", "Make move", None))
        self.saveSettingsButton.setText(_translate("MainWindow", "Save settings", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Image), _translate("MainWindow", "Image", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Edges", None))
        self.connectionStatusLabel.setText(_translate("MainWindow", "Connection Status:", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("MainWindow", "Moves list", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Logs", None))
        self.label.setText(_translate("MainWindow", "A", None))
        self.label_2.setText(_translate("MainWindow", "B", None))
        self.label_3.setText(_translate("MainWindow", "C", None))
        self.label_4.setText(_translate("MainWindow", "D", None))
        self.label_5.setText(_translate("MainWindow", "E", None))
        self.label_8.setText(_translate("MainWindow", "F", None))
        self.label_6.setText(_translate("MainWindow", "G", None))
        self.label_7.setText(_translate("MainWindow", "H", None))
        self.label_11.setText(_translate("MainWindow", "8", None))
        self.label_10.setText(_translate("MainWindow", "7", None))
        self.label_12.setText(_translate("MainWindow", "6", None))
        self.label_13.setText(_translate("MainWindow", "5", None))
        self.label_14.setText(_translate("MainWindow", "4", None))
        self.label_15.setText(_translate("MainWindow", "3", None))
        self.label_16.setText(_translate("MainWindow", "2", None))
        self.label_9.setText(_translate("MainWindow", "1", None))
        self.menuTest.setTitle(_translate("MainWindow", "Test", None))
        self.actionNXT_Control.setText(_translate("MainWindow", "NXT Control", None))
        self.actionConfig.setText(_translate("MainWindow", "Config", None))

