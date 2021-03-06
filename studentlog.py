# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'studentlog.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import home
import studentreg
import student1
check = True

class Ui_Form(object):

    def messagebox(self, title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(650, 450)
        self.swidget = QtWidgets.QWidget(Form)
        self.swidget.setGeometry(QtCore.QRect(20, 20, 590, 420))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.swidget.setFont(font)
        self.swidget.setStyleSheet("QPushButton#slogin{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#slogin:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150,123,111,255);\n"
"}\n"
"QPushButton#slogin:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#sreg{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#sreg:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150,123,111,255);\n"
"}\n"
"QPushButton#sreg:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#slback{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#slback:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150,123,111,255);\n"
"}\n"
"QPushButton#slback:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}")
        self.swidget.setObjectName("swidget")
        self.label = QtWidgets.QLabel(self.swidget)
        self.label.setGeometry(QtCore.QRect(290, 40, 260, 330))
        self.label.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border-bottom-right-radius:50px")
        self.label.setText("")
        self.label.setObjectName("label")
        self.slabel_2 = QtWidgets.QLabel(self.swidget)
        self.slabel_2.setGeometry(QtCore.QRect(40, 25, 270, 360))
        self.slabel_2.setStyleSheet("border-top-left-radius:50px;\n"
"background-color:rgba(0,0,0,80);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));")
        self.slabel_2.setText("")
        self.slabel_2.setObjectName("slabel_2")
        self.slabel_3 = QtWidgets.QLabel(self.swidget)
        self.slabel_3.setGeometry(QtCore.QRect(330, 60, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.slabel_3.setFont(font)
        self.slabel_3.setStyleSheet("color:rgba(0,0,0,200);")
        self.slabel_3.setObjectName("slabel_3")
        self.suserid = QtWidgets.QLineEdit(self.swidget)
        self.suserid.setGeometry(QtCore.QRect(330, 110, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.suserid.setFont(font)
        self.suserid.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.suserid.setObjectName("suserid")
        self.spass = QtWidgets.QLineEdit(self.swidget)
        self.spass.setGeometry(QtCore.QRect(330, 170, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.spass.setFont(font)
        self.spass.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;\n"
"")
        self.spass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.spass.setObjectName("spass")
        self.slogin = QtWidgets.QPushButton(self.swidget)
        self.slogin.setGeometry(QtCore.QRect(330, 220, 191, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.slogin.setFont(font)
        self.slogin.setObjectName("slogin")
        self.slabel_4 = QtWidgets.QLabel(self.swidget)
        self.slabel_4.setGeometry(QtCore.QRect(330, 270, 191, 16))
        self.slabel_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.slabel_4.setStyleSheet("color:rgba(0,0,0,200);")
        self.slabel_4.setAlignment(QtCore.Qt.AlignCenter)
        self.slabel_4.setObjectName("slabel_4")
        self.slabel_5 = QtWidgets.QLabel(self.swidget)
        self.slabel_5.setGeometry(QtCore.QRect(60, 50, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.slabel_5.setFont(font)
        self.slabel_5.setStyleSheet("color:rgba(255,255,255,220);")
        self.slabel_5.setObjectName("slabel_5")
        self.slabel_6 = QtWidgets.QLabel(self.swidget)
        self.slabel_6.setGeometry(QtCore.QRect(60, 180, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.slabel_6.setFont(font)
        self.slabel_6.setStyleSheet("color:rgba(255,255,255,220);")
        self.slabel_6.setObjectName("slabel_6")
        self.sreg = QtWidgets.QPushButton(self.swidget)
        self.sreg.setGeometry(QtCore.QRect(330, 300, 191, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.sreg.setFont(font)
        self.sreg.setAutoRepeat(False)
        self.sreg.setObjectName("sreg")
        self.slabel_7 = QtWidgets.QLabel(self.swidget)
        self.slabel_7.setGeometry(QtCore.QRect(50, 150, 251, 231))
        font = QtGui.QFont()
        font.setFamily("Webdings")
        font.setPointSize(150)
        font.setBold(False)
        font.setWeight(50)
        self.slabel_7.setFont(font)
        self.slabel_7.setObjectName("slabel_7")
        self.slback = QtWidgets.QPushButton(self.swidget)
        self.slback.setGeometry(QtCore.QRect(460, 60, 81, 23))
        font = QtGui.QFont()
        font.setFamily("Wingdings 3")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.slback.setFont(font)
        self.slback.setStyleSheet("")
        self.slback.setObjectName("slback")

        self.messageLabel = QtWidgets.QLabel(Form)
        self.messageLabel.setGeometry(QtCore.QRect(200, 400, 371, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.messageLabel.setFont(font)
        self.messageLabel.setStyleSheet("color: #6B6B6B;")
        self.messageLabel.setText("")
        self.messageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.messageLabel.setWordWrap(False)
        self.messageLabel.setObjectName("messageLabel")

        self.sreg.clicked.connect(self.passage1)
        self.slogin.clicked.connect(self.passage7)
        self.slback.clicked.connect(self.passage)

        self.retranslateUi(Form)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
            
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.slabel_3.setText(_translate("Form", "Log In"))
        self.suserid.setPlaceholderText(_translate("Form", "User ID"))
        self.spass.setPlaceholderText(_translate("Form", "Password"))
        self.slogin.setText(_translate("Form", "L o g In"))
        self.slabel_4.setText(_translate("Form", "Not registered yet?"))
        self.slabel_5.setText(_translate("Form", "Entr??e-in"))
        self.slabel_6.setText(_translate("Form", "Student"))
        self.sreg.setText(_translate("Form", "Register"))
        self.slabel_7.setText(_translate("Form", " &"))
        self.slback.setText(_translate("Form", "8"))

        global check
        check = True
        if(check):
                global x
                x = Form
                check = False


    def passage7(self):
        self.student1_logincheck(x)

    def post_student_login(self,x):
        self.window3 = QtWidgets.QMainWindow()
        self.ui = student1.Ui_Form()
        self.ui.setupUi(self.window3)
        self.window3.show()
        x.close()


    def student1_logincheck(self, x):
        usern = self.suserid.text()
        pass11 = self.spass.text()
        check = False
        if (usern != "" and pass11 != ""):
            check = True
        # try:
        connection = sqlite3.connect("Project.db")
        result_user = connection.execute(f"SELECT Username FROM Student_Registration WHERE Username = '{usern}'")
        result_pass = connection.execute(f"SELECT Password FROM Student_Registration WHERE Password = '{pass11}'")
        usern = result_user.fetchone()
        pass11 = result_pass.fetchone()
        if (usern != None and pass11 != None):
            try:
                user = usern[0]
                connection = sqlite3.connect("Project.db")
                connection.execute(f"Update Current_login set Currentlog_in='{user}' WHERE No = '{1}'")
                connection.commit()
                connection.close()
            except Exception as e:
                print(e)
            self.window3 = QtWidgets.QMainWindow()
            self.ui = student1.Ui_Form()
            self.ui.setupUi(self.window3)
            self.window3.show()
            x.close()
        else:
            if ((usern == None) and (pass11 == None) and (check == False)):
                self.messageLabel.setText("Please Enter Credentials")
            elif ((usern == None) and (pass11 == None) and (check == True)):
                # self.messageLabel.setStyleSheet("font-size:29px;\n"
                #                                 "color: #6B6B6B;")
                self.messageLabel.setText("Invalid Username and Password")
            elif (usern == None):
                self.messageLabel.setText("Invalid Username")
            else:
                self.messageLabel.setText("Invalid Password")
        connection.close()
        # except Exception as e:
        #     print(e)

    def passage(self):
        self.home(x)
        
    def home(self,x):                            
        self.window1 = QtWidgets.QMainWindow()
        self.ui = home.Ui_Form()
        self.ui.setupUi(self.window1)
        self.window1.show()
        x.close()

    def studentreg(self,x):                            
        self.window5 = QtWidgets.QMainWindow()
        self.ui = studentreg.Ui_Form()
        self.ui.setupUi(self.window5)
        self.window5.show()
        x.close()

    def passage1(self):
        self.studentreg(x)    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
