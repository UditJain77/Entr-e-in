# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'studentreg.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import sys
import studentlog
import re
import datetime
check = True

class Ui_Form(object):
        
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(729, 549)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.srwidget = QtWidgets.QWidget(Form)
        self.srwidget.setGeometry(QtCore.QRect(20, 20, 661, 481))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.srwidget.setFont(font)
        self.srwidget.setStyleSheet("QPushButton#srback{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#srback:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150,123,111,255);\n"
"}\n"
"QPushButton#srback:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#pushButton_Register{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#pushButton_Register:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150,123,111,255);\n"
"}\n"
"QPushButton#pushButton_Register:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}")
        self.srwidget.setObjectName("srwidget")
        self.srlabel = QtWidgets.QLabel(self.srwidget)
        self.srlabel.setGeometry(QtCore.QRect(229, 9, 421, 451))
        self.srlabel.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border-bottom-right-radius:50px")
        self.srlabel.setText("")
        self.srlabel.setObjectName("srlabel")
        self.srlabel_2 = QtWidgets.QLabel(self.srwidget)
        self.srlabel_2.setGeometry(QtCore.QRect(40, 25, 201, 421))
        self.srlabel_2.setStyleSheet("border-top-left-radius:50px;\n"
"background-color:rgba(0,0,0,80);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));")
        self.srlabel_2.setText("")
        self.srlabel_2.setObjectName("srlabel_2")
        self.srlabel_3 = QtWidgets.QLabel(self.srwidget)
        self.srlabel_3.setGeometry(QtCore.QRect(250, 10, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.srlabel_3.setFont(font)
        self.srlabel_3.setStyleSheet("color:rgba(0,0,0,200);")
        self.srlabel_3.setObjectName("srlabel_3")
        self.lineEdit_Uname = QtWidgets.QLineEdit(self.srwidget)
        self.lineEdit_Uname.setGeometry(QtCore.QRect(250, 60, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_Uname.setFont(font)
        self.lineEdit_Uname.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit_Uname.setObjectName("lineEdit_Uname")
        self.lineEdit_Fname = QtWidgets.QLineEdit(self.srwidget)
        self.lineEdit_Fname.setGeometry(QtCore.QRect(250, 110, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_Fname.setFont(font)
        self.lineEdit_Fname.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;\n"
"")
        self.lineEdit_Fname.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_Fname.setObjectName("lineEdit_Fname")
        self.srlabel_5 = QtWidgets.QLabel(self.srwidget)
        self.srlabel_5.setGeometry(QtCore.QRect(60, 50, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.srlabel_5.setFont(font)
        self.srlabel_5.setStyleSheet("color:rgba(255,255,255,220);")
        self.srlabel_5.setObjectName("srlabel_5")
        self.srlabel_6 = QtWidgets.QLabel(self.srwidget)
        self.srlabel_6.setGeometry(QtCore.QRect(60, 180, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.srlabel_6.setFont(font)
        self.srlabel_6.setStyleSheet("color:rgba(255,255,255,220);")
        self.srlabel_6.setObjectName("srlabel_6")
        self.pushButton_Register = QtWidgets.QPushButton(self.srwidget)
        self.pushButton_Register.setGeometry(QtCore.QRect(350, 410, 191, 40))
        self.pushButton_Register.clicked.connect(self.insertdata)
        
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Register.setFont(font)
        self.pushButton_Register.setObjectName("pushButton_Register")
        self.srlabel_7 = QtWidgets.QLabel(self.srwidget)
        self.srlabel_7.setGeometry(QtCore.QRect(40, 220, 191, 221))
        font = QtGui.QFont()
        font.setFamily("Webdings")
        font.setPointSize(150)
        font.setBold(False)
        font.setWeight(50)
        self.srlabel_7.setFont(font)
        self.srlabel_7.setObjectName("srlabel_7")
        self.lineEdit_Mother = QtWidgets.QLineEdit(self.srwidget)
        self.lineEdit_Mother.setGeometry(QtCore.QRect(250, 260, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_Mother.setFont(font)
        self.lineEdit_Mother.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit_Mother.setObjectName("lineEdit_Mother")
        self.lineEdit_Father = QtWidgets.QLineEdit(self.srwidget)
        self.lineEdit_Father.setGeometry(QtCore.QRect(250, 210, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_Father.setFont(font)
        self.lineEdit_Father.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit_Father.setObjectName("lineEdit_Father")
        self.lineEdit_Lname = QtWidgets.QLineEdit(self.srwidget)
        self.lineEdit_Lname.setGeometry(QtCore.QRect(250, 160, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_Lname.setFont(font)
        self.lineEdit_Lname.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit_Lname.setObjectName("lineEdit_Lname")
        self.lineEdit_mobile = QtWidgets.QLineEdit(self.srwidget)
        self.lineEdit_mobile.setGeometry(QtCore.QRect(250, 310, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_mobile.setFont(font)
        self.lineEdit_mobile.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit_mobile.setObjectName("lineEdit_mobile")
        self.lineEdit_Passwd = QtWidgets.QLineEdit(self.srwidget)
        self.lineEdit_Passwd.setGeometry(QtCore.QRect(450, 60, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_Passwd.setFont(font)
        self.lineEdit_Passwd.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit_Passwd.setObjectName("lineEdit_Passwd")
        self.lineEdit_district = QtWidgets.QLineEdit(self.srwidget)
        self.lineEdit_district.setGeometry(QtCore.QRect(450, 260, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_district.setFont(font)
        self.lineEdit_district.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit_district.setObjectName("lineEdit_district")
        self.lineEdit_address = QtWidgets.QLineEdit(self.srwidget)
        self.lineEdit_address.setGeometry(QtCore.QRect(450, 210, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_address.setFont(font)
        self.lineEdit_address.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit_address.setObjectName("lineEdit_address")
        self.lineEdit_aadhar = QtWidgets.QLineEdit(self.srwidget)
        self.lineEdit_aadhar.setGeometry(QtCore.QRect(450, 160, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_aadhar.setFont(font)
        self.lineEdit_aadhar.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit_aadhar.setObjectName("lineEdit_aadhar")
        self.lineEdit_Email = QtWidgets.QLineEdit(self.srwidget)
        self.lineEdit_Email.setGeometry(QtCore.QRect(450, 110, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_Email.setFont(font)
        self.lineEdit_Email.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit_Email.setObjectName("lineEdit_Email")
        self.comboBox_Gender = QtWidgets.QComboBox(self.srwidget)
        self.comboBox_Gender.setGeometry(QtCore.QRect(450, 310, 191, 41))
        self.comboBox_Gender.setMouseTracking(False)
        self.comboBox_Gender.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));")
        self.comboBox_Gender.setObjectName("comboBox_Gender")
        self.comboBox_Gender.addItem("")
        self.comboBox_Gender.addItem("")
        self.comboBox_Gender.addItem("")
        self.dateEdit_DOB = QtWidgets.QDateEdit(self.srwidget)
        self.dateEdit_DOB.setGeometry(QtCore.QRect(250, 360, 191, 41))
        self.dateEdit_DOB.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));")
        self.dateEdit_DOB.setObjectName("dateEdit_DOB")
        self.comboBox_State = QtWidgets.QComboBox(self.srwidget)
        self.comboBox_State.setGeometry(QtCore.QRect(450, 360, 191, 41))
        self.comboBox_State.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));")
        self.comboBox_State.setObjectName("comboBox_State")
        self.comboBox_State.addItem("")
        self.comboBox_State.addItem("")
        self.comboBox_State.addItem("")
        self.comboBox_State.addItem("")
        self.comboBox_State.addItem("")
        self.srback = QtWidgets.QPushButton(self.srwidget)
        self.srback.setGeometry(QtCore.QRect(554, 20, 81, 23))
        font = QtGui.QFont()
        font.setFamily("Wingdings 3")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.srback.setFont(font)
        self.srback.setStyleSheet("")
        self.srback.setObjectName("srback")
        self.srback.clicked.connect(self.passage5)

        self.messageLabel = QtWidgets.QLabel(Form)
        self.messageLabel.setGeometry(QtCore.QRect(280, 480, 371, 40))
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.srlabel_3.setText(_translate("Form", "Registration Form"))
        self.lineEdit_Uname.setPlaceholderText(_translate("Form", "User ID"))
        self.lineEdit_Fname.setPlaceholderText(_translate("Form", "First Name"))
        self.srlabel_5.setText(_translate("Form", "Entrée-in"))
        self.srlabel_6.setText(_translate("Form", "Student"))
        self.pushButton_Register.setText(_translate("Form", "Register"))
        self.srlabel_7.setText(_translate("Form", "&"))
        self.lineEdit_Mother.setPlaceholderText(_translate("Form", "Mother\'s Name"))
        self.lineEdit_Father.setPlaceholderText(_translate("Form", "Father\'s Name"))
        self.lineEdit_Lname.setPlaceholderText(_translate("Form", "Last Name"))
        self.lineEdit_mobile.setPlaceholderText(_translate("Form", "Mobile No."))
        self.lineEdit_Passwd.setPlaceholderText(_translate("Form", "Password"))
        self.lineEdit_district.setPlaceholderText(_translate("Form", "District"))
        self.lineEdit_address.setPlaceholderText(_translate("Form", "Address"))
        self.lineEdit_aadhar.setPlaceholderText(_translate("Form", "Aadhar No."))
        self.lineEdit_Email.setPlaceholderText(_translate("Form", "Email-ID"))
        self.comboBox_Gender.setItemText(0, _translate("Form", "Male"))
        self.comboBox_Gender.setItemText(1, _translate("Form", "Female"))
        self.comboBox_Gender.setItemText(2, _translate("Form", "Others"))
        self.comboBox_State.setItemText(0, _translate("Form", "Maharashtra"))
        self.comboBox_State.setItemText(1, _translate("Form", "Karnataka"))
        self.comboBox_State.setItemText(2, _translate("Form", "Gujarat"))
        self.comboBox_State.setItemText(3, _translate("Form", "Rajasthan"))
        self.comboBox_State.setItemText(4, _translate("Form", "Tamil Nadu"))
        self.srback.setText(_translate("Form", "8"))
        global check
        check = True
        if(check):
                global x
                x = Form
                check = False

    def studentlog(self,x):                            
        self.window3 = QtWidgets.QMainWindow()
        self.ui = studentlog.Ui_Form()
        self.ui.setupUi(self.window3)
        self.window3.show()
        x.close()

    def passage5(self):
        self.studentlog(x)

    def insertdata(self):
        Username = self.lineEdit_Uname.text()
        Password = self.lineEdit_Passwd.text()
        First_Name = self.lineEdit_Fname.text()
        Last_Name = self.lineEdit_Lname.text()
        Father_Name = self.lineEdit_Father.text()
        Mother_Name = self.lineEdit_Mother.text()
        Gender = self.comboBox_Gender.currentText()
        self.date1=datetime.date.today()
        self.date=self.date1.replace(year=2003)
        dob1 = self.dateEdit_DOB.date()
        dob = dob1.toPyDate()
        datediff=dob > self.date
        Aadhar_no = self.lineEdit_aadhar.text()
        Mobile_no = self.lineEdit_mobile.text()
        Email_ID = self.lineEdit_Email.text()
        Address = self.lineEdit_address.text()
        District = self.lineEdit_district.text()
        State = self.comboBox_State.currentText()

        if Username== "":
            self.lineEdit_Uname.setText("Field Cannot Be Empty")
            return
        if Password== "":
            self.lineEdit_Passwd.setText("Field Cannot Be Empty")
            return
        if First_Name== "":
            self.lineEdit_Fname.setText("Field Cannot Be Empty")
            return
        if Last_Name== "":
            self.lineEdit_Lname.setText("Field Cannot Be Empty")
            return
        if Father_Name== "":
            self.lineEdit_Father.setText("Field Cannot Be Empty")
            return
        if Mother_Name== "":
            self.lineEdit_Mother.setText("Field Cannot Be Empty")
            return
        if Aadhar_no== "":
            self.lineEdit_aadhar.setText("Field Cannot Be Empty")
            return
        if Mobile_no== "":
            self.lineEdit_mobile.setText("Field Cannot Be Empty")
            return
        if Email_ID== "":
            self.lineEdit_Email.setText("Field Cannot Be Empty")
            return
        if Address== "":
            self.lineEdit_address.setText("Field Cannot Be Empty")
            return
        if District== "":
            self.lineEdit_district.setText("Field Cannot Be Empty")
            return
        # def Exception():
        #     self.messageLabel.setText("Try Again!!")
        if datediff ==True:
            self.messageLabel.setText("Age must be greater than 18")
        else:
            try:
                int(Mobile_no,16)
                if len(Mobile_no)!=10:
                    self.lineEdit_mobile.setText("Invalid Mobile No.")
                else:
                    try:
                        int(Aadhar_no,16)
                        if len(Aadhar_no)!=12:
                            self.lineEdit_aadhar.setText("Invalid Aadhar No.")
                        else:
                            regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
                            if(re.search(regex,str(Email_ID))):
                                try:

                                    connection = sqlite3.connect("Project.db")
                                    connection.execute("INSERT INTO Student_Registration (Username, Password, First_Name, Last_Name, Father_Name, Mother_Name, Gender, DOB, Aadhar_no, Mobile_no, Email_ID, Address, District, State)VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(Username, Password, First_Name, Last_Name, Father_Name, Mother_Name,Gender, dob, Aadhar_no, Mobile_no, Email_ID, Address, District, State))
                                    connection.commit()
                                    connection.close()
                                    self.passage5()
                                except:
                                    self.lineEdit_Uname.setText("User ID Already Exists")
                            else:
                                self.lineEdit_Email.setText("Invalid Email-ID")

                    except:
                        self.lineEdit_aadhar.setText("Invalid Aadhar No.")
            except:
                self.lineEdit_mobile.setText("Invalid Mobile No.")
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
