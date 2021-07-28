# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'college1.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import sys

import collegeca
import collegeinfocollege
import collegelog
import collegesi

check = True


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.setEnabled(True)
        Form.resize(726, 549)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        Form.setInputMethodHints(QtCore.Qt.ImhNone)
        self.c1widget = QtWidgets.QWidget(Form)
        self.c1widget.setGeometry(QtCore.QRect(50, 50, 581, 381))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.c1widget.setFont(font)
        self.c1widget.setStyleSheet("")
        self.c1widget.setObjectName("c1widget")
        self.c1label = QtWidgets.QLabel(self.c1widget)
        self.c1label.setGeometry(QtCore.QRect(69, 40, 491, 321))
        self.c1label.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border-bottom-right-radius:50px")
        self.c1label.setText("")
        self.c1label.setObjectName("c1label")
        self.c1label_2 = QtWidgets.QLabel(self.c1widget)
        self.c1label_2.setGeometry(QtCore.QRect(49, 25, 211, 71))
        self.c1label_2.setStyleSheet("border-top-left-radius:50px;\n"
"background-color:rgba(0,0,0,80);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));")
        self.c1label_2.setText("")
        self.c1label_2.setObjectName("c1label_2")
        self.c1label_5 = QtWidgets.QLabel(self.c1widget)
        self.c1label_5.setGeometry(QtCore.QRect(80, 40, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.c1label_5.setFont(font)
        self.c1label_5.setStyleSheet("color:rgba(255,255,255,220);")
        self.c1label_5.setObjectName("c1label_5")
        self.c1label_6 = QtWidgets.QLabel(self.c1widget)
        self.c1label_6.setGeometry(QtCore.QRect(270, 50, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.c1label_6.setFont(font)
        self.c1label_6.setStyleSheet("color:rgba(0,0,0,200);")
        self.c1label_6.setObjectName("c1label_6")
        self.cstudentinfo = QtWidgets.QPushButton(self.c1widget)
        self.cstudentinfo.setGeometry(QtCore.QRect(260, 170, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.cstudentinfo.setFont(font)
        self.cstudentinfo.setStyleSheet("QPushButton{\n"
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
        self.cstudentinfo.setObjectName("cstudentinfo")
        self.c1logout = QtWidgets.QPushButton(self.c1widget)
        self.c1logout.setGeometry(QtCore.QRect(470, 50, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.c1logout.setFont(font)
        self.c1logout.setStyleSheet("QPushButton{\n"
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
        self.c1logout.setObjectName("c1logout")
        self.cseatallot = QtWidgets.QPushButton(self.c1widget)
        self.cseatallot.setGeometry(QtCore.QRect(420, 170, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.cseatallot.setFont(font)
        self.cseatallot.setStyleSheet("QPushButton{\n"
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
        self.cseatallot.setObjectName("cseatallot")
        self.cscollegeinfo = QtWidgets.QPushButton(self.c1widget)
        self.cscollegeinfo.setGeometry(QtCore.QRect(110, 170, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.cscollegeinfo.setFont(font)
        self.cscollegeinfo.setStyleSheet("QPushButton{\n"
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
        self.cscollegeinfo.setObjectName("cscollegeinfo")
        self.c1logout.clicked.connect(self.passage13)
        self.cscollegeinfo.clicked.connect(self.passage10)
        self.cstudentinfo.clicked.connect(self.passage3)
        self.cseatallot.clicked.connect(self.passage4)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.c1label_5.setText(_translate("Form", "College"))
        self.c1label_6.setText(_translate("Form", "Home"))
        self.cstudentinfo.setText(_translate("Form", "Student\n"
"Information"))
        self.c1logout.setText(_translate("Form", "Log Out"))
        self.cseatallot.setText(_translate("Form", "Seat\n"
"Allotment"))
        self.cscollegeinfo.setText(_translate("Form", "College\n"
"Information"))
        global check
        check = True
        if(check):
                global x
                x = Form
                check = False

    def collegelog(self,x):
        self.window3 = QtWidgets.QMainWindow()
        self.ui = collegelog.Ui_Form()
        self.ui.setupUi(self.window3)
        self.window3.show()
        x.close()

    def passage13(self):
        self.collegelog(x)

    def collegeinfocollege(self,x):
        self.window4 = QtWidgets.QMainWindow()
        self.ui = collegeinfocollege.Ui_Form()
        self.ui.setupUi(self.window4)
        self.window4.show()
        x.close()

    def passage10(self):
        self.collegeinfocollege(x)

    def collegeca(self,x):
        self.window4 = QtWidgets.QMainWindow()
        self.ui = collegeca.Ui_Form()
        self.ui.setupUi(self.window4)
        self.window4.show()
        x.close()

    def passage4(self):
        self.collegeca(x)

    def collegesi(self,x):
        self.window4 = QtWidgets.QMainWindow()
        self.ui = collegesi.Ui_Form()
        self.ui.setupUi(self.window4)
        self.window4.show()
        x.close()

    def passage3(self):
        self.collegesi(x)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
