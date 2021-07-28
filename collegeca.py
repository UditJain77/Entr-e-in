# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'collegeca.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets

import college1


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(764, 445)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.csawidget = QtWidgets.QWidget(Form)
        self.csawidget.setGeometry(QtCore.QRect(20, 20, 731, 411))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.csawidget.setFont(font)
        self.csawidget.setStyleSheet("QPushButton#alogin{\n"
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
        self.csawidget.setObjectName("csawidget")
        self.csalabel = QtWidgets.QLabel(self.csawidget)
        self.csalabel.setGeometry(QtCore.QRect(150, 30, 561, 351))
        self.csalabel.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border-bottom-right-radius:50px")
        self.csalabel.setText("")
        self.csalabel.setObjectName("csalabel")
        self.csalabel_2 = QtWidgets.QLabel(self.csawidget)
        self.csalabel_2.setGeometry(QtCore.QRect(10, 20, 151, 371))
        self.csalabel_2.setStyleSheet("border-top-left-radius:50px;\n"
"background-color:rgba(0,0,0,80);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));")
        self.csalabel_2.setText("")
        self.csalabel_2.setObjectName("csalabel_2")
        self.csalabel_3 = QtWidgets.QLabel(self.csawidget)
        self.csalabel_3.setGeometry(QtCore.QRect(290, 40, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.csalabel_3.setFont(font)
        self.csalabel_3.setStyleSheet("color:rgba(0,0,0,200);")
        self.csalabel_3.setObjectName("csalabel_3")
        self.csalabel_5 = QtWidgets.QLabel(self.csawidget)
        self.csalabel_5.setGeometry(QtCore.QRect(20, 50, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.csalabel_5.setFont(font)
        self.csalabel_5.setStyleSheet("color:rgba(255,255,255,220);")
        self.csalabel_5.setObjectName("csalabel_5")
        self.csalabel_6 = QtWidgets.QLabel(self.csawidget)
        self.csalabel_6.setGeometry(QtCore.QRect(20, 170, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.csalabel_6.setFont(font)
        self.csalabel_6.setStyleSheet("color:rgba(255,255,255,220);")
        self.csalabel_6.setObjectName("csalabel_6")
        self.csaback = QtWidgets.QPushButton(self.csawidget)
        self.csaback.setGeometry(QtCore.QRect(620, 50, 81, 23))
        font = QtGui.QFont()
        font.setFamily("Wingdings 3")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.csaback.setFont(font)
        self.csaback.setStyleSheet("QPushButton{\n"
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
        self.csaback.setObjectName("csaback")
        self.Mech = QtWidgets.QLabel(self.csawidget)
        self.Mech.setGeometry(QtCore.QRect(320, 140, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Mech.setFont(font)
        self.Mech.setStyleSheet("color:rgba(255,255,255,220);\n"
"background-color:rgba(0,0,0,80);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));")
        self.Mech.setObjectName("Mech")
        self.Chem = QtWidgets.QLabel(self.csawidget)
        self.Chem.setGeometry(QtCore.QRect(470, 140, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Chem.setFont(font)
        self.Chem.setStyleSheet("color:rgba(255,255,255,220);\n"
"border-top-right-radius:5px;\n"
"background-color:rgba(0,0,0,80);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));")
        self.Chem.setObjectName("Chem")
        self.Comps = QtWidgets.QLabel(self.csawidget)
        self.Comps.setGeometry(QtCore.QRect(170, 140, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Comps.setFont(font)
        self.Comps.setStyleSheet("border-top-left-radius:5px;\n"
"color:rgba(255,255,255,220);\n"
"background-color:rgba(0,0,0,80);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));")
        self.Comps.setObjectName("Comps")
        self.CSS1 = QtWidgets.QLabel(self.csawidget)
        self.CSS1.setGeometry(QtCore.QRect(170, 170, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.CSS1.setFont(font)
        self.CSS1.setStyleSheet("color:rgba(255,255,255,220);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));")
        self.CSS1.setText("")
        self.CSS1.setObjectName("CSS1")
        self.MS1 = QtWidgets.QLabel(self.csawidget)
        self.MS1.setGeometry(QtCore.QRect(320, 170, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.MS1.setFont(font)
        self.MS1.setStyleSheet("color:rgba(255,255,255,220);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));")
        self.MS1.setText("")
        self.MS1.setObjectName("MS1")
        self.CS1 = QtWidgets.QLabel(self.csawidget)
        self.CS1.setGeometry(QtCore.QRect(470, 170, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.CS1.setFont(font)
        self.CS1.setStyleSheet("color:rgba(255,255,255,220);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));")
        self.CS1.setText("")
        self.CS1.setObjectName("CS1")
        self.CS3 = QtWidgets.QLabel(self.csawidget)
        self.CS3.setGeometry(QtCore.QRect(470, 230, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.CS3.setFont(font)
        self.CS3.setStyleSheet("color:rgba(255,255,255,220);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));")
        self.CS3.setText("")
        self.CS3.setObjectName("CS3")
        self.MS2 = QtWidgets.QLabel(self.csawidget)
        self.MS2.setGeometry(QtCore.QRect(320, 200, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.MS2.setFont(font)
        self.MS2.setStyleSheet("color:rgba(255,255,255,220);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));")
        self.MS2.setText("")
        self.MS2.setObjectName("MS2")
        self.CS2 = QtWidgets.QLabel(self.csawidget)
        self.CS2.setGeometry(QtCore.QRect(470, 200, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.CS2.setFont(font)
        self.CS2.setStyleSheet("color:rgba(255,255,255,220);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));")
        self.CS2.setText("")
        self.CS2.setObjectName("CS2")
        self.MS3 = QtWidgets.QLabel(self.csawidget)
        self.MS3.setGeometry(QtCore.QRect(320, 230, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.MS3.setFont(font)
        self.MS3.setStyleSheet("color:rgba(255,255,255,220);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));")
        self.MS3.setText("")
        self.MS3.setObjectName("MS3")
        self.CSS3 = QtWidgets.QLabel(self.csawidget)
        self.CSS3.setGeometry(QtCore.QRect(170, 230, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.CSS3.setFont(font)
        self.CSS3.setStyleSheet("color:rgba(255,255,255,220);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));")
        self.CSS3.setText("")
        self.CSS3.setObjectName("CSS3")
        self.CSS2 = QtWidgets.QLabel(self.csawidget)
        self.CSS2.setGeometry(QtCore.QRect(170, 200, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.CSS2.setFont(font)
        self.CSS2.setStyleSheet("color:rgba(255,255,255,220);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));")
        self.CSS2.setText("")
        self.CSS2.setObjectName("CSS2")
        self.CS4 = QtWidgets.QLabel(self.csawidget)
        self.CS4.setGeometry(QtCore.QRect(470, 260, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.CS4.setFont(font)
        self.CS4.setStyleSheet("color:rgba(255,255,255,220);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));")
        self.CS4.setText("")
        self.CS4.setObjectName("CS4")
        self.CS5 = QtWidgets.QLabel(self.csawidget)
        self.CS5.setGeometry(QtCore.QRect(470, 290, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.CS5.setFont(font)
        self.CS5.setStyleSheet("border-bottom-right-radius:5px;\n"
"color:rgba(255,255,255,220);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));")
        self.CS5.setText("")
        self.CS5.setObjectName("CS5")
        self.MS5 = QtWidgets.QLabel(self.csawidget)
        self.MS5.setGeometry(QtCore.QRect(320, 290, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.MS5.setFont(font)
        self.MS5.setStyleSheet("color:rgba(255,255,255,220);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));")
        self.MS5.setText("")
        self.MS5.setObjectName("MS5")
        self.CSS5 = QtWidgets.QLabel(self.csawidget)
        self.CSS5.setGeometry(QtCore.QRect(170, 290, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.CSS5.setFont(font)
        self.CSS5.setStyleSheet("border-bottom-left-radius:5px;\n"
"color:rgba(255,255,255,220);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));")
        self.CSS5.setText("")
        self.CSS5.setObjectName("CSS5")
        self.CSS4 = QtWidgets.QLabel(self.csawidget)
        self.CSS4.setGeometry(QtCore.QRect(170, 260, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.CSS4.setFont(font)
        self.CSS4.setStyleSheet("color:rgba(255,255,255,220);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));")
        self.CSS4.setText("")
        self.CSS4.setObjectName("CSS4")
        self.MS4 = QtWidgets.QLabel(self.csawidget)
        self.MS4.setGeometry(QtCore.QRect(320, 260, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.MS4.setFont(font)
        self.MS4.setStyleSheet("color:rgba(255,255,255,220);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));")
        self.MS4.setText("")
        self.MS4.setObjectName("MS4")
        self.csaback.clicked.connect(self.passage)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        connection = sqlite3.connect("Project.db")
        cursor = connection.cursor()
        S_user = cursor.execute(f"SELECT * FROM Current_login WHERE No = {2}")
        record = S_user.fetchone()
        user =record[0]
        print(user)
        try:
                check1 = cursor.execute(f"SELECT * FROM Final_Generate where College ='{user}'")
                print(check1)
                result1 = check1.fetchall()
                print(result1)
                for i in range(0,len(result1)):
                        if result1[i][2]=="Computer Science":
                                if self.CSS1.text()=="":
                                        self.CSS1.setText(result1[i][0])
                                elif self.CSS2.text()=="":
                                        self.CSS2.setText(result1[i][0])
                                elif self.CSS3.text()=="":
                                        self.CSS3.setText(result1[i][0])
                                elif self.CSS4.text()=="":
                                        self.CSS4.setText(result1[i][0])
                                elif self.CSS5.text()=="":
                                        self.CSS5.setText(result1[i][0])
                        elif result1[i][2]=="Mechanics":
                                if self.MS1.text()=="":
                                        self.MS1.setText(result1[i][0])
                                elif self.MS2.text()=="":
                                        self.MS2.setText(result1[i][0])
                                elif self.MS3.text()=="":
                                        self.MS3.setText(result1[i][0])
                                elif self.MS4.text()=="":
                                        self.MS4.setText(result1[i][0])
                                elif self.MS5.text()=="":
                                        self.MS5.setText(result1[i][0])
                        elif result1[i][2]=="Chemical":
                                if self.CS1.text()=="":
                                        self.CS1.setText(result1[i][0])
                                elif self.CS2.text()=="":
                                        self.CS2.setText(result1[i][0])
                                elif self.CS3.text()=="":
                                        self.CS3.setText(result1[i][0])
                                elif self.CS4.text()=="":
                                        self.CS4.setText(result1[i][0])
                                elif self.CS5.text()=="":
                                        self.CS5.setText(result1[i][0])

                connection.commit()
                connection.close()
        except Exception as e:
                print(e)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.csalabel_3.setText(_translate("Form", "Student Allocation"))
        self.csalabel_5.setText(_translate("Form", "Entrée-in"))
        self.csalabel_6.setText(_translate("Form", "College"))
        self.csaback.setText(_translate("Form", "8"))
        self.Mech.setText(_translate("Form", "Mechanics"))
        self.Chem.setText(_translate("Form", "Chemical"))
        self.Comps.setText(_translate("Form", "Computer Science"))
        global check
        check = True
        if (check):
                global x
                x = Form
                check = False

    def college1(self, x):
            self.window3 = QtWidgets.QMainWindow()
            self.ui = college1.Ui_Form()
            self.ui.setupUi(self.window3)
            self.window3.show()
            x.close()

    def passage(self):
            self.college1(x)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
