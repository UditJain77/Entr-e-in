# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'studentpl.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets

import student1


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(764, 549)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.splwidget = QtWidgets.QWidget(Form)
        self.splwidget.setGeometry(QtCore.QRect(20, 20, 731, 491))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.splwidget.setFont(font)
        self.splwidget.setStyleSheet("QPushButton#alogin{\n"
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
        self.splwidget.setObjectName("splwidget")
        self.spllabel = QtWidgets.QLabel(self.splwidget)
        self.spllabel.setGeometry(QtCore.QRect(150, 30, 561, 441))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.spllabel.setFont(font)
        self.spllabel.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border-bottom-right-radius:50px")
        self.spllabel.setText("")
        self.spllabel.setObjectName("spllabel")
        self.spllabel_2 = QtWidgets.QLabel(self.splwidget)
        self.spllabel_2.setGeometry(QtCore.QRect(10, 20, 151, 461))
        self.spllabel_2.setStyleSheet("border-top-left-radius:50px;\n"
"background-color:rgba(0,0,0,80);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));")
        self.spllabel_2.setText("")
        self.spllabel_2.setObjectName("spllabel_2")
        self.spllabel_3 = QtWidgets.QLabel(self.splwidget)
        self.spllabel_3.setGeometry(QtCore.QRect(260, 40, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.spllabel_3.setFont(font)
        self.spllabel_3.setStyleSheet("color:rgba(0,0,0,200);")
        self.spllabel_3.setObjectName("spllabel_3")
        self.spllabel_5 = QtWidgets.QLabel(self.splwidget)
        self.spllabel_5.setGeometry(QtCore.QRect(20, 50, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.spllabel_5.setFont(font)
        self.spllabel_5.setStyleSheet("color:rgba(255,255,255,220);")
        self.spllabel_5.setObjectName("spllabel_5")
        self.spllabel_6 = QtWidgets.QLabel(self.splwidget)
        self.spllabel_6.setGeometry(QtCore.QRect(20, 200, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.spllabel_6.setFont(font)
        self.spllabel_6.setStyleSheet("color:rgba(255,255,255,220);")
        self.spllabel_6.setObjectName("spllabel_6")
        self.splback = QtWidgets.QPushButton(self.splwidget)
        self.splback.setGeometry(QtCore.QRect(620, 50, 81, 23))
        font = QtGui.QFont()
        font.setFamily("Wingdings 3")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.splback.setFont(font)
        self.splback.setStyleSheet("QPushButton{\n"
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
        self.splback.setObjectName("splback")
        self.College_name = QtWidgets.QComboBox(self.splwidget)
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
        for i in range(0,Listlen):
                self.College_name.addItem("")

        self.spllabel_4 = QtWidgets.QLabel(self.splwidget)
        self.spllabel_4.setGeometry(QtCore.QRect(180, 120, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.spllabel_4.setFont(font)
        self.spllabel_4.setStyleSheet("color:rgba(0,0,0,200);")
        self.spllabel_4.setObjectName("spllabel_4")
        self.Pref2 = QtWidgets.QLabel(self.splwidget)
        self.Pref2.setGeometry(QtCore.QRect(200, 210, 501, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Pref2.setFont(font)
        self.Pref2.setStyleSheet("color:rgba(255,255,255,220);\n"
"border-radius:5px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"")
        self.Pref2.setText("")
        self.Pref2.setObjectName("Pref2")
        self.Pref4 = QtWidgets.QLabel(self.splwidget)
        self.Pref4.setGeometry(QtCore.QRect(200, 310, 501, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Pref4.setFont(font)
        self.Pref4.setStyleSheet("color:rgba(255,255,255,220);\n"
"border-radius:5px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"")
        self.Pref4.setText("")
        self.Pref4.setObjectName("Pref4")
        self.Pref1 = QtWidgets.QLabel(self.splwidget)
        self.Pref1.setGeometry(QtCore.QRect(200, 160, 501, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Pref1.setFont(font)
        self.Pref1.setStyleSheet("color:rgba(255,255,255,220);\n"
"border-radius:5px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"")
        self.Pref1.setText("")
        self.Pref1.setObjectName("Pref1")
        self.Pref3 = QtWidgets.QLabel(self.splwidget)
        self.Pref3.setGeometry(QtCore.QRect(200, 260, 501, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Pref3.setFont(font)
        self.Pref3.setStyleSheet("color:rgba(255,255,255,220);\n"
"border-radius:5px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"")
        self.Pref3.setText("")
        self.Pref3.setObjectName("Pref3")
        self.Select = QtWidgets.QPushButton(self.splwidget)
        self.Select.setGeometry(QtCore.QRect(560, 80, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Select.setFont(font)
        self.Select.setStyleSheet("QPushButton{\n"
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
        self.Select.setObjectName("Select")
        self.Stream = QtWidgets.QComboBox(self.splwidget)
        self.Stream.setGeometry(QtCore.QRect(370, 80, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Stream.setFont(font)
        self.Stream.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"color:rgba(255,255,255,220);")
        self.Stream.setObjectName("Stream")
        self.Stream.addItem("")
        self.Stream.addItem("")
        self.Stream.addItem("")
        self.Stream.addItem("")
        self.Submit = QtWidgets.QPushButton(self.splwidget)
        self.Submit.setGeometry(QtCore.QRect(460, 405, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Submit.setFont(font)
        self.Submit.setStyleSheet("QPushButton{\n"
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
        self.Submit.setObjectName("Submit")
        self.Clear = QtWidgets.QPushButton(self.splwidget)
        self.Clear.setGeometry(QtCore.QRect(320, 405, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Clear.setFont(font)
        self.Clear.setStyleSheet("QPushButton{\n"
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
        self.Clear.setObjectName("Clear")
        self.Pref5 = QtWidgets.QLabel(self.splwidget)
        self.Pref5.setGeometry(QtCore.QRect(200, 360, 501, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Pref5.setFont(font)
        self.Pref5.setStyleSheet("color:rgba(255,255,255,220);\n"
"border-radius:5px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"")
        self.Pref5.setText("")
        self.Pref5.setObjectName("Pref5")

        self.messageLabel1 = QtWidgets.QLabel(Form)
        self.messageLabel1.setGeometry(QtCore.QRect(210, 460, 500, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.messageLabel1.setFont(font)
        self.messageLabel1.setStyleSheet("color: #6B6B6B;")
        self.messageLabel1.setText("")
        self.messageLabel1.setAlignment(QtCore.Qt.AlignCenter)
        self.messageLabel1.setWordWrap(False)
        self.messageLabel1.setObjectName("messageLabel")


        connection = sqlite3.connect("Project.db")
        cursor = connection.cursor()
        S_user = cursor.execute(f"SELECT * FROM Current_login WHERE No = '{1}'")
        record = S_user.fetchone()
        user = record[0]
        try:
            Spl_user = cursor.execute(f"SELECT * FROM Col_Pref_list where Username = '{user}'")
            recordpl = Spl_user.fetchone()
            userpl = recordpl[0]
            if userpl== user:
                self.messageLabel1.setText(f"User '{user}' Already Filled Preference List")
                self.Select.setEnabled(False)
                self.Submit.setEnabled(False)
                self.Clear.setEnabled(False)
                try:
                    Spl_user = cursor.execute(f"SELECT * FROM Col_Pref_list where Username = '{user}'")
                    recordpl = Spl_user.fetchone()
                    self.Pref1.setText(f"'{recordpl[1]}':'{recordpl[2]}'")
                    self.Pref2.setText(f"'{recordpl[3]}':'{recordpl[4]}'")
                    self.Pref3.setText(f"'{recordpl[5]}':'{recordpl[6]}'")
                    self.Pref4.setText(f"'{recordpl[7]}':'{recordpl[8]}'")
                    self.Pref5.setText(f"'{recordpl[9]}':'{recordpl[10]}'")
                    connection.commit()
                    connection.close()
                except Exception as e:
                    print(e)
        except Exception as e:
            self.Select.clicked.connect(self.Enter_pref)
            self.Clear.clicked.connect(self.Clearall)
            self.Submit.clicked.connect(self.Submit_Check)
            print(e)
            connection.commit()
            connection.close()


        self.splback.clicked.connect(self.passage1)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.spllabel_3.setText(_translate("Form", "College Preference List"))
        self.spllabel_5.setText(_translate("Form", "Entrée-in"))
        self.spllabel_6.setText(_translate("Form", "Student"))
        self.splback.setText(_translate("Form", "8"))
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
        Listlen = len(List)
        conn.commit()
        conn.close()
        for i in range(0,Listlen):
                self.College_name.setItemText(i+1 , _translate("Form", f"{List[i]}"))
        self.spllabel_4.setText(_translate("Form", "Display:"))
        self.Select.setText(_translate("Form", "Select"))
        self.Stream.setItemText(0, _translate("Form", "Stream"))
        self.Stream.setItemText(1, _translate("Form", "Computer Science"))
        self.Stream.setItemText(2, _translate("Form", "Mechanics"))
        self.Stream.setItemText(3, _translate("Form", "Chemical"))
        self.Submit.setText(_translate("Form", "Submit"))
        self.Clear.setText(_translate("Form", "Clear"))
        global check
        check = True
        if (check):
                global x
                x = Form
                check = False

    def passage1(self):
            self.studenthome(x)

    def studenthome(self, x):
            self.window3 = QtWidgets.QMainWindow()
            self.ui = student1.Ui_Form()
            self.ui.setupUi(self.window3)
            self.window3.show()
            x.close()


    def Enter_pref(self):
        college = self.College_name.currentText()
        stream=self.Stream.currentText()
        if stream != "Stream" and college != "College_Name" and self.Pref1.text()== "":
            self.Pref1.setText(f"{college}:{stream}")
        elif stream != "Stream" and college != "College_Name" and self.Pref2.text()== "":
            self.Pref2.setText(f"{college}:{stream}")
        elif stream != "Stream" and college != "College_Name" and self.Pref3.text()== "":
            self.Pref3.setText(f"{college}:{stream}")
        elif stream != "Stream" and college != "College_Name" and self.Pref4.text()== "":
            self.Pref4.setText(f"{college}:{stream}")
        elif stream != "Stream" and college != "College_Name" and self.Pref5.text()== "":
            self.Pref5.setText(f"{college}:{stream}")
        elif stream == "Stream":
                return
        else:
                return
        # self.coldic.update({college1:stream1},{college2:stream2},{college3:stream3},{college4:stream4},{college5:stream5})

    def Clearall(self):
            self.Pref1.setText("")
            self.Pref2.setText("")
            self.Pref3.setText("")
            self.Pref4.setText("")
            self.Pref5.setText("")

    def Submit_Check(self):
        pref1=self.Pref1.text()
        col1=pref1.split(':')
        pref2=self.Pref2.text()
        col2=pref2.split(':')
        pref3=self.Pref3.text()
        col3=pref3.split(':')
        pref4=self.Pref4.text()
        col4=pref4.split(':')
        pref5=self.Pref5.text()
        col5=pref5.split(':')

        if pref1 == "":
                self.messageLabel1.setText("Atleast One College Is Requried")
                return
        if pref1 == pref2:
                self.messageLabel1.setText("Preference Must be unique")
                return
        if pref1 == pref3:
                self.messageLabel1.setText("Preference Must be unique")
                return
        if pref1 == pref4:
                self.messageLabel1.setText("Preference Must be unique")
                return
        if pref1 == pref5:
                self.messageLabel1.setText("Preference Must be unique")
                return
        if pref2 == pref1:
                self.messageLabel1.setText("Preference Must be unique")
                return
        if pref2 == pref3:
                self.messageLabel1.setText("Preference Must be unique")
                return
        if pref2 == pref4:
                self.messageLabel1.setText("Preference Must be unique")
                return
        if pref2 == pref5:
                self.messageLabel1.setText("Preference Must be unique")
                return
        if pref3 == pref2:
                self.messageLabel1.setText("Preference Must be unique")
                return
        if pref3 == pref1:
                self.messageLabel1.setText("Preference Must be unique")
                return
        if pref3 == pref4:
                self.messageLabel1.setText("Preference Must be unique")
                return
        if pref3 == pref5:
                self.messageLabel1.setText("Preference Must be unique")
                return
        if pref4 == pref1:
                self.messageLabel1.setText("Preference Must be unique")
                return
        if pref4 == pref3:
                self.messageLabel1.setText("Preference Must be unique")
                return
        if pref4 == pref2:
                self.messageLabel1.setText("Preference Must be unique")
                return
        if pref4 == pref5:
                self.messageLabel1.setText("Preference Must be unique")
                return
        if pref5 == pref1:
                self.messageLabel1.setText("Preference Must be unique")
                return
        if pref5 == pref3:
                self.messageLabel1.setText("Preference Must be unique")
                return
        if pref5 == pref2:
                self.messageLabel1.setText("Preference Must be unique")
                return
        if pref5 == pref4:
                self.messageLabel1.setText("Preference Must be unique")
                return
        try:
                connection = sqlite3.connect("Project.db")
                cursor = connection.cursor()
                S_user = cursor.execute(f"SELECT * FROM Current_login WHERE No = '{1}'")
                record = S_user.fetchone()
                self.user = record[0]

                connection = sqlite3.connect("Project.db")
                connection.execute(
                        "Insert into  Col_Pref_list(Username,College1 ,Stream1 ,College2 ,Stream2 ,College3 ,Stream3 ,College4 ,Stream4 ,College5 ,Stream5 )VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(self.user,col1[0],col1[1],col2[0],col2[1],col3[0],col3[1],col4[0],col4[1],col5[0],col5[1]))
                self.messageLabel1.setText("Registration Successfull")
                connection.commit()
                connection.close()
        except Exception as e:
                        self.messageLabel1.setText("References must be unique")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
