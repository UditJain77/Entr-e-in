# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminsi.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets

import admin1


class Ui_Form(object):

    def loadData(self):
        connection = sqlite3.connect("Project.db")
        sqlquery = "SELECT * FROM Student_Information"
        result = connection.execute(sqlquery)
        self.asitableWidget.setRowCount(0)
        x = 0
        for row_number, row_data in enumerate(result):
            self.asitableWidget.insertRow(row_number)
            for x, data in enumerate(row_data):
                self.asitableWidget.setItem(row_number, x, QtWidgets.QTableWidgetItem(str(data)))
                x += 1

        connection.close()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(962, 549)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.awidget = QtWidgets.QWidget(Form)
        self.awidget.setGeometry(QtCore.QRect(20, 20, 921, 491))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.awidget.setFont(font)
        self.awidget.setStyleSheet("QPushButton#alogin{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#alogin:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150,123,111,255);\n"
"}\n"
"QPushButton#alogin:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}")
        self.awidget.setObjectName("awidget")
        self.asilabel = QtWidgets.QLabel(self.awidget)
        self.asilabel.setGeometry(QtCore.QRect(170, 40, 741, 401))
        self.asilabel.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border-bottom-right-radius:50px")
        self.asilabel.setText("")
        self.asilabel.setObjectName("asilabel")
        self.asilabel_2 = QtWidgets.QLabel(self.awidget)
        self.asilabel_2.setGeometry(QtCore.QRect(10, 20, 171, 431))
        self.asilabel_2.setStyleSheet("border-top-left-radius:50px;\n"
"background-color:rgba(0,0,0,80);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));")
        self.asilabel_2.setText("")
        self.asilabel_2.setObjectName("asilabel_2")
        self.asilabel_3 = QtWidgets.QLabel(self.awidget)
        self.asilabel_3.setGeometry(QtCore.QRect(350, 50, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.asilabel_3.setFont(font)
        self.asilabel_3.setStyleSheet("color:rgba(0,0,0,200);")
        self.asilabel_3.setObjectName("asilabel_3")
        self.asilabel_5 = QtWidgets.QLabel(self.awidget)
        self.asilabel_5.setGeometry(QtCore.QRect(20, 50, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.asilabel_5.setFont(font)
        self.asilabel_5.setStyleSheet("color:rgba(255,255,255,220);")
        self.asilabel_5.setObjectName("asilabel_5")
        self.asilabel_6 = QtWidgets.QLabel(self.awidget)
        self.asilabel_6.setGeometry(QtCore.QRect(20, 200, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.asilabel_6.setFont(font)
        self.asilabel_6.setStyleSheet("color:rgba(255,255,255,220);")
        self.asilabel_6.setObjectName("asilabel_6")
        self.asiback = QtWidgets.QPushButton(self.awidget)
        self.asiback.setGeometry(QtCore.QRect(810, 50, 81, 23))
        font = QtGui.QFont()
        font.setFamily("Wingdings 3")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.asiback.setFont(font)
        self.asiback.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150,123,111,255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}")
        self.asiback.setObjectName("asiback")
        self.asitableWidget = QtWidgets.QTableWidget(self.awidget)
        self.asitableWidget.setGeometry(QtCore.QRect(190, 90, 691, 331))
        self.asitableWidget.setStyleSheet("border: 1px solid black;\n"
"")
        self.asitableWidget.setObjectName("asitableWidget")
        self.asitableWidget.setColumnCount(8)
        self.asitableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.asitableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.asitableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.asitableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.asitableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.asitableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.asitableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.asitableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.asitableWidget.setHorizontalHeaderItem(7, item)
        self.loadData()
        self.asiback.clicked.connect(self.passage2)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.asilabel_3.setText(_translate("Form", "Student Information"))
        self.asilabel_5.setText(_translate("Form", "Entrée-in"))
        self.asilabel_6.setText(_translate("Form", "Admin"))
        self.asiback.setText(_translate("Form", "8"))
        item = self.asitableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Name"))
        item = self.asitableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Email-ID"))
        item = self.asitableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Mobile No."))
        item = self.asitableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "DOB"))
        item = self.asitableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Physics"))
        item = self.asitableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Chemistry"))
        item = self.asitableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Mathematic"))
        item = self.asitableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Total"))
        global check
        check = True
        if (check):
            global x
            x = Form
            check = False

    def admin1(self, x):
        self.window1 = QtWidgets.QMainWindow()
        self.ui = admin1.Ui_Form()
        self.ui.setupUi(self.window1)
        self.window1.show()
        x.close()

    def passage2(self):
        self.admin1(x)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
