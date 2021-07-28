# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminci.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets

import admin1
import student1


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(764, 549)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.aciwidget = QtWidgets.QWidget(Form)
        self.aciwidget.setGeometry(QtCore.QRect(20, 20, 731, 491))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.aciwidget.setFont(font)
        self.aciwidget.setStyleSheet("QPushButton#alogin{\n"
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
        self.aciwidget.setObjectName("aciwidget")
        self.acilabel = QtWidgets.QLabel(self.aciwidget)
        self.acilabel.setGeometry(QtCore.QRect(150, 30, 561, 441))
        self.acilabel.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border-bottom-right-radius:50px")
        self.acilabel.setText("")
        self.acilabel.setObjectName("acilabel")
        self.acilabel_2 = QtWidgets.QLabel(self.aciwidget)
        self.acilabel_2.setGeometry(QtCore.QRect(10, 20, 151, 461))
        self.acilabel_2.setStyleSheet("border-top-left-radius:50px;\n"
"background-color:rgba(0,0,0,80);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));")
        self.acilabel_2.setText("")
        self.acilabel_2.setObjectName("acilabel_2")
        self.acilabel_3 = QtWidgets.QLabel(self.aciwidget)
        self.acilabel_3.setGeometry(QtCore.QRect(290, 40, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.acilabel_3.setFont(font)
        self.acilabel_3.setStyleSheet("color:rgba(0,0,0,200);")
        self.acilabel_3.setObjectName("acilabel_3")
        self.acilabel_5 = QtWidgets.QLabel(self.aciwidget)
        self.acilabel_5.setGeometry(QtCore.QRect(20, 50, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.acilabel_5.setFont(font)
        self.acilabel_5.setStyleSheet("color:rgba(255,255,255,220);")
        self.acilabel_5.setObjectName("acilabel_5")
        self.acilabel_6 = QtWidgets.QLabel(self.aciwidget)
        self.acilabel_6.setGeometry(QtCore.QRect(20, 200, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.acilabel_6.setFont(font)
        self.acilabel_6.setStyleSheet("color:rgba(255,255,255,220);")
        self.acilabel_6.setObjectName("acilabel_6")
        self.aciback = QtWidgets.QPushButton(self.aciwidget)
        self.aciback.setGeometry(QtCore.QRect(620, 50, 81, 23))
        font = QtGui.QFont()
        font.setFamily("Wingdings 3")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.aciback.setFont(font)
        self.aciback.setStyleSheet("QPushButton{\n"
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
        self.aciback.setObjectName("aciback")
        self.College_name = QtWidgets.QComboBox(self.aciwidget)
        self.College_name.setGeometry(QtCore.QRect(180, 80, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.College_name.setFont(font)
        self.College_name.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"color:rgba(255,255,255,220);")
        self.College_name.setObjectName("College_name")
        self.College_name.addItem("")
        conn = sqlite3.connect('Project.db')
        c = conn.cursor()
        c.execute("SELECT College_Name FROM College_Registration")
        pmList = c.fetchall()
        List = []
        for i in pmList:
                for j in i:
                        if j != None:
                                List.append(j)
        Listlen = len(List)
        conn.commit()
        conn.close()
        for i in range(0, Listlen):
                self.College_name.addItem("")

        self.Address = QtWidgets.QLabel(self.aciwidget)
        self.Address.setGeometry(QtCore.QRect(180, 120, 511, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Address.setFont(font)
        self.Address.setStyleSheet("color:rgba(0,0,0,200);")
        self.Address.setObjectName("Address")
        self.Website = QtWidgets.QLabel(self.aciwidget)
        self.Website.setGeometry(QtCore.QRect(180, 160, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Website.setFont(font)
        self.Website.setStyleSheet("color:rgba(0,0,0,200);")
        self.Website.setObjectName("Website")
        self.Email_ID = QtWidgets.QLabel(self.aciwidget)
        self.Email_ID.setGeometry(QtCore.QRect(530, 160, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Email_ID.setFont(font)
        self.Email_ID.setStyleSheet("color:rgba(0,0,0,200);")
        self.Email_ID.setObjectName("Email_ID")
        self.Description = QtWidgets.QLabel(self.aciwidget)
        self.Description.setGeometry(QtCore.QRect(170, 200, 531, 141))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Description.setFont(font)
        self.Description.setStyleSheet("")
        self.Description.setObjectName("Description")
        self.Contact_no = QtWidgets.QLabel(self.aciwidget)
        self.Contact_no.setGeometry(QtCore.QRect(350, 160, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Contact_no.setFont(font)
        self.Contact_no.setStyleSheet("color:rgba(0,0,0,200);")
        self.Contact_no.setObjectName("Contact_no")
        self.acilabel_7 = QtWidgets.QLabel(self.aciwidget)
        self.acilabel_7.setGeometry(QtCore.QRect(170, 340, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.acilabel_7.setFont(font)
        self.acilabel_7.setStyleSheet("color:rgba(0,0,0,200);")
        self.acilabel_7.setObjectName("acilabel_7")
        self.acilabel_12 = QtWidgets.QLabel(self.aciwidget)
        self.acilabel_12.setGeometry(QtCore.QRect(170, 370, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.acilabel_12.setFont(font)
        self.acilabel_12.setStyleSheet("color:rgba(0,0,0,200);")
        self.acilabel_12.setObjectName("acilabel_12")
        self.acilabel_13 = QtWidgets.QLabel(self.aciwidget)
        self.acilabel_13.setGeometry(QtCore.QRect(170, 400, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.acilabel_13.setFont(font)
        self.acilabel_13.setStyleSheet("color:rgba(0,0,0,200);")
        self.acilabel_13.setObjectName("acilabel_13")
        self.acilabel_11 = QtWidgets.QLabel(self.aciwidget)
        self.acilabel_11.setGeometry(QtCore.QRect(170, 430, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.acilabel_11.setFont(font)
        self.acilabel_11.setStyleSheet("color:rgba(0,0,0,200);")
        self.acilabel_11.setObjectName("acilabel_11")
        self.acilabel_8 = QtWidgets.QLabel(self.aciwidget)
        self.acilabel_8.setGeometry(QtCore.QRect(300, 340, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.acilabel_8.setFont(font)
        self.acilabel_8.setStyleSheet("color:rgba(0,0,0,200);")
        self.acilabel_8.setObjectName("acilabel_8")
        self.acilabel_9 = QtWidgets.QLabel(self.aciwidget)
        self.acilabel_9.setGeometry(QtCore.QRect(360, 340, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.acilabel_9.setFont(font)
        self.acilabel_9.setStyleSheet("color:rgba(0,0,0,200);")
        self.acilabel_9.setObjectName("acilabel_9")
        self.acilabel_10 = QtWidgets.QLabel(self.aciwidget)
        self.acilabel_10.setGeometry(QtCore.QRect(420, 340, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.acilabel_10.setFont(font)
        self.acilabel_10.setStyleSheet("color:rgba(0,0,0,200);")
        self.acilabel_10.setObjectName("acilabel_10")
        self.Generate = QtWidgets.QPushButton(self.aciwidget)
        self.Generate.setGeometry(QtCore.QRect(380, 80, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Generate.setFont(font)
        self.Generate.setStyleSheet("QPushButton{\n"
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
        self.Generate.setObjectName("Generate")
        self.Y2020S2 = QtWidgets.QLabel(self.aciwidget)
        self.Y2020S2.setGeometry(QtCore.QRect(300, 370, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Y2020S2.setFont(font)
        self.Y2020S2.setStyleSheet("color:rgba(255,255,255,220);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));")
        self.Y2020S2.setText("")
        self.Y2020S2.setObjectName("Y2020S2")
        self.Y2019S2 = QtWidgets.QLabel(self.aciwidget)
        self.Y2019S2.setGeometry(QtCore.QRect(360, 370, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Y2019S2.setFont(font)
        self.Y2019S2.setStyleSheet("color:rgba(255,255,255,220);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));")
        self.Y2019S2.setText("")
        self.Y2019S2.setObjectName("Y2019S2")
        self.Y2018S2 = QtWidgets.QLabel(self.aciwidget)
        self.Y2018S2.setGeometry(QtCore.QRect(420, 370, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Y2018S2.setFont(font)
        self.Y2018S2.setStyleSheet("color:rgba(255,255,255,220);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));")
        self.Y2018S2.setText("")
        self.Y2018S2.setObjectName("Y2018S2")
        self.Y2018S1 = QtWidgets.QLabel(self.aciwidget)
        self.Y2018S1.setGeometry(QtCore.QRect(420, 430, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Y2018S1.setFont(font)
        self.Y2018S1.setStyleSheet("color:rgba(255,255,255,220);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));")
        self.Y2018S1.setText("")
        self.Y2018S1.setObjectName("Y2018S1")
        self.Y2019S3 = QtWidgets.QLabel(self.aciwidget)
        self.Y2019S3.setGeometry(QtCore.QRect(360, 400, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Y2019S3.setFont(font)
        self.Y2019S3.setStyleSheet("color:rgba(255,255,255,220);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));")
        self.Y2019S3.setText("")
        self.Y2019S3.setObjectName("Y2019S3")
        self.Y2018S3 = QtWidgets.QLabel(self.aciwidget)
        self.Y2018S3.setGeometry(QtCore.QRect(420, 400, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Y2018S3.setFont(font)
        self.Y2018S3.setStyleSheet("color:rgba(255,255,255,220);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));")
        self.Y2018S3.setText("")
        self.Y2018S3.setObjectName("Y2018S3")
        self.Y2019S1 = QtWidgets.QLabel(self.aciwidget)
        self.Y2019S1.setGeometry(QtCore.QRect(360, 430, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Y2019S1.setFont(font)
        self.Y2019S1.setStyleSheet("color:rgba(255,255,255,220);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));")
        self.Y2019S1.setText("")
        self.Y2019S1.setObjectName("Y2019S1")
        self.Y2020S1 = QtWidgets.QLabel(self.aciwidget)
        self.Y2020S1.setGeometry(QtCore.QRect(300, 430, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Y2020S1.setFont(font)
        self.Y2020S1.setStyleSheet("color:rgba(255,255,255,220);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));")
        self.Y2020S1.setText("")
        self.Y2020S1.setObjectName("Y2020S1")
        self.Y2020S3 = QtWidgets.QLabel(self.aciwidget)
        self.Y2020S3.setGeometry(QtCore.QRect(300, 400, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Y2020S3.setFont(font)
        self.Y2020S3.setStyleSheet("color:rgba(255,255,255,220);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));")
        self.Y2020S3.setText("")
        self.Y2020S3.setObjectName("Y2020S3")
        self.Generate.clicked.connect(self.generate)
        self.aciback.clicked.connect(self.passage)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.acilabel_3.setText(_translate("Form", "College Information"))
        self.acilabel_5.setText(_translate("Form", "Entrée-in"))
        self.acilabel_6.setText(_translate("Form", "Admin"))
        self.aciback.setText(_translate("Form", "8"))
        self.College_name.setItemText(0, _translate("Form", "College Name"))
        conn = sqlite3.connect('Project.db')
        self.College_name.setItemText(0, _translate("Form", "College_Name"))
        c = conn.cursor()
        c.execute("SELECT College_Name FROM College_Registration")
        pmList = c.fetchall()
        List = []
        for i in pmList:
                for j in i:
                        if j != None:
                                List.append(j)
        print(List)
        Listlen = len(List)
        conn.commit()
        conn.close()
        for i in range(0, Listlen):
                self.College_name.setItemText(i + 1, _translate("Form", f"{List[i]}"))

        self.Address.setText(_translate("Form", "Address"))
        self.Website.setText(_translate("Form", "Website"))
        self.Email_ID.setText(_translate("Form", "Email-ID"))
        self.Description.setText(_translate("Form", "About College"))
        self.Contact_no.setText(_translate("Form", "Contact No."))
        self.acilabel_7.setText(_translate("Form", "Past year cutoffs:"))
        self.acilabel_12.setText(_translate("Form", "Mechanics"))
        self.acilabel_13.setText(_translate("Form", "Chemical"))
        self.acilabel_11.setText(_translate("Form", "Computer Science"))
        self.acilabel_8.setText(_translate("Form", "2020"))
        self.acilabel_9.setText(_translate("Form", "2019"))
        self.acilabel_10.setText(_translate("Form", "2018"))
        self.Generate.setText(_translate("Form", "Generate"))
        global check
        check = True
        if (check):
                global x
                x = Form
                check = False


    def passage(self):
        self.adminhome(x)

    def adminhome(self, x):
        self.window3 = QtWidgets.QMainWindow()
        self.ui = admin1.Ui_Form()
        self.ui.setupUi(self.window3)
        self.window3.show()
        x.close()

    def generate(self):
        college=self.College_name.currentText()
        try:
                connection = sqlite3.connect("Project.db")
                cursor = connection.cursor()
                data = cursor.execute(f"SELECT * FROM College_Registration WHERE College_Name = '{college}'")
                records = data.fetchone()
                address=records[2]
                website=records[3]
                contact=f"{records[4]}"
                Email_id=records[5]

                data1 = cursor.execute(f"SELECT * FROM College_Verification WHERE College_Name = '{college}'")
                records1 = data1.fetchone()
                Description=records1[1]
                Y2018S1=f"{records1[2]}"
                Y2018S2=f"{records1[3]}"
                Y2018S3=f"{records1[4]}"
                Y2019S1=f"{records1[5]}"
                Y2019S2=f"{records1[6]}"
                Y2019S3=f"{records1[7]}"
                Y2020S1=f"{records1[8]}"
                Y2020S2=f"{records1[9]}"
                Y2020S3=f"{records1[10]}"

                self.Address.setText(address)
                self.Website.setText(website)
                self.Email_ID.setText(Email_id)
                self.Contact_no.setText(contact)
                self.Description.setText(Description)
                self.Y2018S1.setText(Y2018S1)
                self.Y2018S2.setText(Y2018S2)
                self.Y2018S3.setText(Y2018S3)
                self.Y2019S1.setText(Y2019S1)
                self.Y2019S2.setText(Y2019S2)
                self.Y2019S3.setText(Y2019S3)
                self.Y2020S1.setText(Y2020S1)
                self.Y2020S2.setText(Y2020S2)
                self.Y2020S3.setText(Y2020S3)
        except Exception as e:
                print(e)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
