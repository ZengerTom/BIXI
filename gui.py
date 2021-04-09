from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *

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


class Ui_BIXIMap(object):
    def setupUi(self, BIXIMap):

        self.indexO = 0
        self.indexD = 0

        BIXIMap.setObjectName(_fromUtf8("BIXIMap"))
        BIXIMap.resize(560, 400)
        BIXIMap.setMinimumSize(QtCore.QSize(560, 400))
        BIXIMap.setMaximumSize(QtCore.QSize(560, 400))
        self.centralwidget = QtGui.QWidget(BIXIMap)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.welcome_label = QtGui.QLabel(self.centralwidget)
        self.welcome_label.setGeometry(QtCore.QRect(20, 20, 350, 20))
        self.welcome_label.setObjectName(_fromUtf8("welcome_label"))
        self.station_label = QtGui.QLabel(self.centralwidget)
        self.station_label.setGeometry(QtCore.QRect(20, 50, 350, 20))
        self.station_label.setObjectName(_fromUtf8("station_label"))
        self.label_orig = QtGui.QLabel(self.centralwidget)
        self.label_orig.setGeometry(QtCore.QRect(20, 165, 100, 20))
        self.label_orig.setObjectName(_fromUtf8("label_orig"))
        self.label_dest = QtGui.QLabel(self.centralwidget)
        self.label_dest.setGeometry(QtCore.QRect(20, 200, 100, 40))
        self.label_dest.setMaximumSize(QtCore.QSize(200, 40))
        self.label_dest.setObjectName(_fromUtf8("label_dest"))
        self.label_k = QtGui.QLabel(self.centralwidget)
        self.label_k.setGeometry(QtCore.QRect(20, 130, 100, 20))
        self.label_k.setObjectName(_fromUtf8("label_k"))
        self.label_info = QtGui.QLabel(self.centralwidget)
        self.label_info.setGeometry(QtCore.QRect(20, 100, 180, 20))
        self.label_info.setObjectName(_fromUtf8("label_info"))
        self.output = QtGui.QTextEdit(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(20, 300, 380, 80))
        self.output.setObjectName(_fromUtf8("output"))
        self.btn_bike = QtGui.QPushButton(self.centralwidget)
        self.btn_bike.setGeometry(QtCore.QRect(20, 260, 120, 24))
        self.btn_bike.setDefault(True)
        self.btn_bike.setObjectName(_fromUtf8("btn_bike"))
        self.btn_station = QtGui.QPushButton(self.centralwidget)
        self.btn_station.setGeometry(QtCore.QRect(150, 260, 120, 24))
        self.btn_station.setDefault(True)
        self.btn_station.setObjectName(_fromUtf8("btn_station"))
        self.btn_route = QtGui.QPushButton(self.centralwidget)
        self.btn_route.setGeometry(QtCore.QRect(280, 260, 120, 24))
        self.btn_route.setDefault(True)
        self.btn_route.setObjectName(_fromUtf8("btn_route"))
        self.label_pic = QtGui.QLabel(self.centralwidget)
        self.label_pic.setGeometry(QtCore.QRect(390, 20, 150, 150))
        self.label_pic.setPixmap(QPixmap("logo.png"))
        self.label_pic.setObjectName(_fromUtf8("label_pic"))
        self.edit_k = QtGui.QLineEdit(self.centralwidget)
        self.edit_k.setGeometry(QtCore.QRect(170, 125, 120, 30))
        self.edit_k.setObjectName(_fromUtf8("edit_k"))
        self.edit_orig = QtGui.QComboBox(self.centralwidget)
        self.edit_orig.setGeometry(QtCore.QRect(170, 160, 120, 30))
        self.edit_orig.setObjectName(_fromUtf8("edit_orig"))
        self.edit_orig.setEditable(True)
        self.edit_dest = QtGui.QComboBox(self.centralwidget)
        self.edit_dest.setGeometry(QtCore.QRect(170, 195, 120, 30))
        self.edit_dest.setObjectName(_fromUtf8("edit_dest"))
        self.edit_dest.setEditable(True)
        BIXIMap.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(BIXIMap)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        BIXIMap.setStatusBar(self.statusbar)

        self.retranslateUi(BIXIMap)
        QtCore.QMetaObject.connectSlotsByName(BIXIMap)
        BIXIMap.setTabOrder(self.btn_bike, self.btn_station)
        BIXIMap.setTabOrder(self.btn_station, self.btn_route)
        BIXIMap.setTabOrder(self.btn_route, self.output)

    def retranslateUi(self, BIXIMap):
        BIXIMap.setWindowTitle(_translate("BIXIMap", "BIXIMap", None))
        self.welcome_label.setText(_translate("BIXIMap",
                                              "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Welcome to Bike Share Toronto</span></p></body></html>",
                                              None))
        self.station_label.setText(_translate("BIXIMap",
                                              "<html><head/><body><p><span style=\" font-size:12pt;\">Actual we list x bike stations you are free to use</span></p></body></html>",
                                              None))
        self.label_orig.setText(_translate("BIXIMap",
                                           "<html><head/><body><p><span style=\" font-size:12pt;\">Origin</span></p></body></html>",
                                           None))
        self.label_dest.setText(_translate("BIXIMap",
                                           "<html><head/><body><p><span style=\" font-size:12pt;\">Destination<br/>(optional)</span></p></body></html>",
                                           None))
        self.label_k.setText(_translate("BIXIMap",
                                        "<html><head/><body><p><span style=\" font-size:12pt;\">Number k</span></p></body></html>",
                                        None))
        self.label_info.setText(_translate("BIXIMap",
                                           "<html><head/><body><p><span style=\" font-size:12pt; text-decoration: underline;\">Information:</span></p></body></html>",
                                           None))
        self.btn_bike.setText(_translate("BIXIMap", "Find Bike", None))
        self.btn_station.setText(_translate("BIXIMap", "Find Return Station", None))
        self.btn_route.setText(_translate("BIXIMap", "Route", None))
        self.output.setReadOnly(True)
        self.output.append(("Hello you!"))
        self.output.append(("Please write the addresses in following term:"))
        self.output.append(("'Number, Street'"))
        self.output.append("There is no need to add the city or country")
        self.output.append(("Otherwise it wouldn't accept the input."))
        self.output.moveCursor(QtGui.QTextCursor.Start)
        self.output.ensureCursorVisible()
