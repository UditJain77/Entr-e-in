# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin1.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import adminca
import adminci
import adminlog
import adminsi
import studentpl


class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.setEnabled(True)
        Form.resize(726, 549)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        Form.setInputMethodHints(QtCore.Qt.ImhNone)
        self.a1widget = QtWidgets.QWidget(Form)
        self.a1widget.setGeometry(QtCore.QRect(50, 50, 581, 381))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.a1widget.setFont(font)
        self.a1widget.setStyleSheet("")
        self.a1widget.setObjectName("a1widget")
        self.a1label = QtWidgets.QLabel(self.a1widget)
        self.a1label.setGeometry(QtCore.QRect(69, 40, 491, 321))
        self.a1label.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border-bottom-right-radius:50px")
        self.a1label.setText("")
        self.a1label.setObjectName("a1label")
        self.a1label_2 = QtWidgets.QLabel(self.a1widget)
        self.a1label_2.setGeometry(QtCore.QRect(49, 25, 211, 71))
        self.a1label_2.setStyleSheet("border-top-left-radius:50px;\n"
"background-color:rgba(0,0,0,80);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));")
        self.a1label_2.setText("")
        self.a1label_2.setObjectName("a1label_2")
        self.acollegeinfo = QtWidgets.QPushButton(self.a1widget)
        self.acollegeinfo.setGeometry(QtCore.QRect(130, 180, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.acollegeinfo.setFont(font)
        self.acollegeinfo.setStyleSheet("QPushButton{\n"
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
        self.acollegeinfo.setObjectName("acollegeinfo")
        self.a1label_5 = QtWidgets.QLabel(self.a1widget)
        self.a1label_5.setGeometry(QtCore.QRect(80, 40, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.a1label_5.setFont(font)
        self.a1label_5.setStyleSheet("color:rgba(255,255,255,220);")
        self.a1label_5.setObjectName("a1label_5")
        self.a1label_6 = QtWidgets.QLabel(self.a1widget)
        self.a1label_6.setGeometry(QtCore.QRect(270, 50, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.a1label_6.setFont(font)
        self.a1label_6.setStyleSheet("color:rgba(0,0,0,200);")
        self.a1label_6.setObjectName("a1label_6")
        self.astudentinfo = QtWidgets.QPushButton(self.a1widget)
        self.astudentinfo.setGeometry(QtCore.QRect(270, 180, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.astudentinfo.setFont(font)
        self.astudentinfo.setStyleSheet("QPushButton{\n"
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
        self.astudentinfo.setObjectName("astudentinfo")
        self.acollegeallot = QtWidgets.QPushButton(self.a1widget)
        self.acollegeallot.setGeometry(QtCore.QRect(410, 180, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.acollegeallot.setFont(font)
        self.acollegeallot.setStyleSheet("QPushButton{\n"
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
        self.acollegeallot.setObjectName("acollegeallot")
        self.a1logout = QtWidgets.QPushButton(self.a1widget)
        self.a1logout.setGeometry(QtCore.QRect(470, 50, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.a1logout.setFont(font)
        self.a1logout.setStyleSheet("QPushButton{\n"
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
        self.a1logout.setObjectName("a1logout")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.a1logout.clicked.connect(self.passage8)
        self.acollegeinfo.clicked.connect(self.passage)
        self.astudentinfo.clicked.connect(self.passage2)
        self.acollegeallot.clicked.connect(self.passage3)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.acollegeinfo.setText(_translate("Form", "College\n"
"Information"))
        self.a1label_5.setText(_translate("Form", "Admin"))
        self.a1label_6.setText(_translate("Form", "Home"))
        self.astudentinfo.setText(_translate("Form", "Student\n"
"Information"))
        self.acollegeallot.setText(_translate("Form", "College\n"
"Allotment"))
        self.a1logout.setText(_translate("Form", "Log Out"))
        global check
        check = True
        if(check):
                global x
                x = Form
                check = False

    def adminlog(self, x):
        self.window10 = QtWidgets.QMainWindow()
        self.ui = adminlog.Ui_Form()
        self.ui.setupUi(self.window10)
        self.window10.show()
        x.close()

    def passage8(self):
        self.adminlog(x)

    def adminci(self, x):
        self.window1 = QtWidgets.QMainWindow()
        self.ui = adminci.Ui_Form()
        self.ui.setupUi(self.window1)
        self.window1.show()
        x.close()

    def passage(self):
        self.adminci(x)

    def adminsi(self, x):
        self.window1 = QtWidgets.QMainWindow()
        self.ui = adminsi.Ui_Form()
        self.ui.setupUi(self.window1)
        self.window1.show()
        x.close()

    def passage2(self):
        self.adminsi(x)

    def adminca(self, x):
        self.window1 = QtWidgets.QMainWindow()
        self.ui =adminca.Ui_Form()
        self.ui.setupUi(self.window1)
        self.window1.show()
        x.close()

    def passage3(self):
        self.adminca(x)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
