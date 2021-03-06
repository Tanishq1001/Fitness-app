# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fitness.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(725, 622)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_pushups = QtWidgets.QPushButton(self.centralwidget)
        self.button_pushups.setGeometry(QtCore.QRect(220, 360, 261, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.button_pushups.setFont(font)
        self.button_pushups.setObjectName("button_pushups")
        self.button_sitsups = QtWidgets.QPushButton(self.centralwidget)
        self.button_sitsups.setGeometry(QtCore.QRect(220, 530, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.button_sitsups.setFont(font)
        self.button_sitsups.setObjectName("button_sitsups")
        self.button_burpees = QtWidgets.QPushButton(self.centralwidget)
        self.button_burpees.setGeometry(QtCore.QRect(220, 450, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.button_burpees.setFont(font)
        self.button_burpees.setObjectName("button_burpees")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 30, 331, 281))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("media resources/pushup.gif"))
        self.label.setObjectName("label")
        self.button_sitsups.raise_()
        self.button_burpees.raise_()
        self.button_pushups.raise_()
        self.label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 725, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.button_pushups.clicked.connect(self.show_pushup)
        self.button_sitsups.clicked.connect(self.show_situp)
        self.button_burpees.clicked.connect(self.show_burpees)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_pushups.setText(_translate("MainWindow", "Push-ups"))
        self.button_sitsups.setText(_translate("MainWindow", "Sit-ups"))
        self.button_burpees.setText(_translate("MainWindow", "Burpees"))

    def show_pushup(self):
        self.label.setPixmap(QtGui.QPixmap("media resources/pushup.gif"))

    def show_situp(self):
        self.label.setPixmap(QtGui.QPixmap("media resources/Sit-up.gif"))

    def show_burpees(self):
        self.label.setPixmap(QtGui.QPixmap("media resources/burpees.gif"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
