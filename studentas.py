# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'studentas.ui'
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
        Form.resize(793, 584)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.saswidget = QtWidgets.QWidget(Form)
        self.saswidget.setGeometry(QtCore.QRect(20, 20, 731, 541))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.saswidget.setFont(font)
        self.saswidget.setStyleSheet("QPushButton#alogin{\n"
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
        self.saswidget.setObjectName("saswidget")
        self.saslabel = QtWidgets.QLabel(self.saswidget)
        self.saslabel.setGeometry(QtCore.QRect(150, 30, 561, 471))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.saslabel.setFont(font)
        self.saslabel.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border-bottom-right-radius:50px")
        self.saslabel.setText("")
        self.saslabel.setObjectName("saslabel")
        self.saslabel_2 = QtWidgets.QLabel(self.saswidget)
        self.saslabel_2.setGeometry(QtCore.QRect(10, 20, 151, 501))
        self.saslabel_2.setStyleSheet("border-top-left-radius:50px;\n"
"background-color:rgba(0,0,0,80);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));")
        self.saslabel_2.setText("")
        self.saslabel_2.setObjectName("saslabel_2")
        self.saslabel_3 = QtWidgets.QLabel(self.saswidget)
        self.saslabel_3.setGeometry(QtCore.QRect(290, 40, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.saslabel_3.setFont(font)
        self.saslabel_3.setStyleSheet("color:rgba(0,0,0,200);")
        self.saslabel_3.setObjectName("saslabel_3")
        self.saslabel_5 = QtWidgets.QLabel(self.saswidget)
        self.saslabel_5.setGeometry(QtCore.QRect(20, 50, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.saslabel_5.setFont(font)
        self.saslabel_5.setStyleSheet("color:rgba(255,255,255,220);")
        self.saslabel_5.setObjectName("saslabel_5")
        self.saslabel_6 = QtWidgets.QLabel(self.saswidget)
        self.saslabel_6.setGeometry(QtCore.QRect(20, 230, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.saslabel_6.setFont(font)
        self.saslabel_6.setStyleSheet("color:rgba(255,255,255,220);")
        self.saslabel_6.setObjectName("saslabel_6")
        self.sasback = QtWidgets.QPushButton(self.saswidget)
        self.sasback.setGeometry(QtCore.QRect(620, 50, 81, 23))
        font = QtGui.QFont()
        font.setFamily("Wingdings 3")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.sasback.setFont(font)
        self.sasback.setStyleSheet("QPushButton{\n"
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
        self.sasback.setObjectName("sasback")
        self.saslabel_4 = QtWidgets.QLabel(self.saswidget)
        self.saslabel_4.setGeometry(QtCore.QRect(180, 70, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.saslabel_4.setFont(font)
        self.saslabel_4.setStyleSheet("color:rgba(0,0,0,200);")
        self.saslabel_4.setObjectName("saslabel_4")
        self.Pref2 = QtWidgets.QLabel(self.saswidget)
        self.Pref2.setGeometry(QtCore.QRect(200, 150, 501, 31))
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
        self.Pref4 = QtWidgets.QLabel(self.saswidget)
        self.Pref4.setGeometry(QtCore.QRect(200, 250, 501, 31))
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
        self.Pref1 = QtWidgets.QLabel(self.saswidget)
        self.Pref1.setGeometry(QtCore.QRect(200, 100, 501, 31))
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
        self.Pref3 = QtWidgets.QLabel(self.saswidget)
        self.Pref3.setGeometry(QtCore.QRect(200, 200, 501, 31))
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
        self.Submit = QtWidgets.QPushButton(self.saswidget)
        self.Submit.setGeometry(QtCore.QRect(410, 340, 101, 31))
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
        self.Pref5 = QtWidgets.QLabel(self.saswidget)
        self.Pref5.setGeometry(QtCore.QRect(200, 300, 501, 31))
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
        self.College_alloted = QtWidgets.QLabel(self.saswidget)
        self.College_alloted.setGeometry(QtCore.QRect(200, 380, 501, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.College_alloted.setFont(font)
        self.College_alloted.setStyleSheet("color:rgba(255,255,255,220);\n"
"border-radius:5px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"")
        self.College_alloted.setText("")
        self.College_alloted.setObjectName("College_alloted")
        self.Note = QtWidgets.QLabel(self.saswidget)
        self.Note.setGeometry(QtCore.QRect(200, 420, 491, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Note.setFont(font)
        self.Note.setStyleSheet("color:rgba(0,0,0,200);")
        self.Note.setText("")
        self.Note.setObjectName("Note")
        self.sasback.clicked.connect(self.passage)
        self.Submit.clicked.connect(self.Check_Status)

        self.messageLabel1 = QtWidgets.QLabel(Form)
        self.messageLabel1.setGeometry(QtCore.QRect(300, 530, 350, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.messageLabel1.setFont(font)
        self.messageLabel1.setStyleSheet("color: #000000;")
        self.messageLabel1.setText("")
        self.messageLabel1.setAlignment(QtCore.Qt.AlignCenter)
        self.messageLabel1.setWordWrap(False)
        self.messageLabel1.setObjectName("messageLabel")
        try:
                connection = sqlite3.connect("Project.db")
                cursor = connection.cursor()
                S_user = cursor.execute(f"SELECT * FROM Current_login WHERE No = '{1}'")
                record = S_user.fetchone()
                user = record[0]
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
                self.messageLabel1.setText(f"User '{user}' not filled College Preference List")
                print(e)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.saslabel_3.setText(_translate("Form", "My Allocation Status"))
        self.saslabel_5.setText(_translate("Form", "Entrée-in"))
        self.saslabel_6.setText(_translate("Form", "Student"))
        self.sasback.setText(_translate("Form", "8"))
        self.saslabel_4.setText(_translate("Form", "Your Preference List"))
        self.Submit.setText(_translate("Form", "Check Status"))
        global check
        check = True
        if (check):
                global x
                x = Form
                check = False

    def passage(self):
            self.studenthome(x)

    def studenthome(self,x):
        self.window = QtWidgets.QMainWindow()
        self.ui = student1.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()
        x.close()

    def Check_Status(self):
        connection = sqlite3.connect("Project.db")
        cursor = connection.cursor()
        S_user = cursor.execute(f"SELECT * FROM Current_login WHERE No = {1}")
        record = S_user.fetchone()
        user = record[0]
        print(user)
        check = cursor.execute(f"select * from Final_Generate where Student ='{user}'")
        result1 = check.fetchone()
        print(result1)
        if result1 != None and result1[1] != "Not_Qua":
                self.College_alloted.setText(f"                         College: '{result1[1]}' And Stream: '{result1[2]}'")
                self.Note.setText("  👍😊🥳Congratulations, you have been allotted the above mentioned college🥳😊👍.\n                                        👍👍All the best for your new journey🚶🏻🚶🏻\n                          🙏🙏🏫🏫 Thank You for Using Entrée-in🏫🏫🙏🙏")
        elif result1 == None:
                self.College_alloted.setText("                                          ⏳❎Process is not yet over❎⏳.")
                self.Note.setText("                                 💬Not getting the confirmation message?💬\n                               📝No worries, Try rechecking after some time.📝\n                           🙏🙏🏫🏫 Thank You for Using Entrée-in🏫🏫🙏🙏")
        elif result1[1] == "Not_Qua" :
                self.College_alloted.setText("          😟😌Sighhh, you didn't meet the eligibility criteria for admission😌😟")
                self.Note.setText("                                             ☺️Don't be disheartened☺️\n'                    🤗😳there's always a new ray of sunshine after a stormy night😳🤗'\n                           🙏🙏🏫🏫 Thank You for Using Entrée-in🏫🏫🙏🙏")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
