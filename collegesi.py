# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'collegesi.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
import college1
class Ui_Form(object):

    def loadData(self):
        connection = sqlite3.connect("Project.db")
        sqlquery = "SELECT * FROM Student_Information"
        result = connection.execute(sqlquery)
        self.csitableWidget.setRowCount(0)
        x = 0
        for row_number, row_data in enumerate(result):
            self.csitableWidget.insertRow(row_number)
            for x, data in enumerate(row_data):
                self.csitableWidget.setItem(row_number, x, QtWidgets.QTableWidgetItem(str(data)))
                x += 1
        connection.close()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(962, 549)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.csiwidget = QtWidgets.QWidget(Form)
        self.csiwidget.setGeometry(QtCore.QRect(20, 20, 921, 491))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.csiwidget.setFont(font)
        self.csiwidget.setStyleSheet("QPushButton#alogin{\n"
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
        self.csiwidget.setObjectName("csiwidget")
        self.csilabel = QtWidgets.QLabel(self.csiwidget)
        self.csilabel.setGeometry(QtCore.QRect(170, 40, 741, 401))
        self.csilabel.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border-bottom-right-radius:50px")
        self.csilabel.setText("")
        self.csilabel.setObjectName("csilabel")
        self.csilabel_2 = QtWidgets.QLabel(self.csiwidget)
        self.csilabel_2.setGeometry(QtCore.QRect(10, 20, 171, 431))
        self.csilabel_2.setStyleSheet("border-top-left-radius:50px;\n"
"background-color:rgba(0,0,0,80);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));")
        self.csilabel_2.setText("")
        self.csilabel_2.setObjectName("csilabel_2")
        self.csilabel_3 = QtWidgets.QLabel(self.csiwidget)
        self.csilabel_3.setGeometry(QtCore.QRect(350, 50, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.csilabel_3.setFont(font)
        self.csilabel_3.setStyleSheet("color:rgba(0,0,0,200);")
        self.csilabel_3.setObjectName("csilabel_3")
        self.csilabel_5 = QtWidgets.QLabel(self.csiwidget)
        self.csilabel_5.setGeometry(QtCore.QRect(20, 50, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.csilabel_5.setFont(font)
        self.csilabel_5.setStyleSheet("color:rgba(255,255,255,220);")
        self.csilabel_5.setObjectName("csilabel_5")
        self.csilabel_6 = QtWidgets.QLabel(self.csiwidget)
        self.csilabel_6.setGeometry(QtCore.QRect(20, 200, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.csilabel_6.setFont(font)
        self.csilabel_6.setStyleSheet("color:rgba(255,255,255,220);")
        self.csilabel_6.setObjectName("csilabel_6")
        self.csiback = QtWidgets.QPushButton(self.csiwidget)
        self.csiback.setGeometry(QtCore.QRect(810, 50, 81, 23))
        font = QtGui.QFont()
        font.setFamily("Wingdings 3")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.csiback.setFont(font)
        self.csiback.setStyleSheet("QPushButton{\n"
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
        self.csiback.setObjectName("csiback")
        self.csitableWidget = QtWidgets.QTableWidget(self.csiwidget)
        self.csitableWidget.setGeometry(QtCore.QRect(190, 90, 691, 331))
        self.csitableWidget.setStyleSheet("border: 1px solid black;\n"
"")
        self.csitableWidget.setObjectName("csitableWidget")
        self.csitableWidget.setColumnCount(8)
        self.csitableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.csitableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.csitableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.csitableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.csitableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.csitableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.csitableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.csitableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.csitableWidget.setHorizontalHeaderItem(7, item)
        self.loadData()
        self.csiback.clicked.connect(self.passage1)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.csilabel_3.setText(_translate("Form", "Student Information"))
        self.csilabel_5.setText(_translate("Form", "Entrée-in"))
        self.csilabel_6.setText(_translate("Form", "College"))
        self.csiback.setText(_translate("Form", "8"))
        item = self.csitableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Name"))
        item = self.csitableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Email-ID"))
        item = self.csitableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Mobile No."))
        item = self.csitableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "DOB"))
        item = self.csitableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Physics"))
        item = self.csitableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Chemistry"))
        item = self.csitableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Mathematic"))
        item = self.csitableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Total"))
        global check
        check = True
        if (check):
            global x
            x = Form
            check = False

    def passage1(self):
        self.collegehome(x)

    def collegehome(self, x):
        self.window3 = QtWidgets.QMainWindow()
        self.ui = college1.Ui_Form()
        self.ui.setupUi(self.window3)
        self.window3.show()
        x.close()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
