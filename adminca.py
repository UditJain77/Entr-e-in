# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminca.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import admin1


class Ui_Form(object):

    def loadData(self):
        connection = sqlite3.connect("Project.db")
        sqlquery = "SELECT * FROM Final_Generate"
        result = connection.execute(sqlquery)
        self.asatableWidget.setRowCount(0)
        x = 0
        for row_number, row_data in enumerate(result):
            self.asatableWidget.insertRow(row_number)
            for x, data in enumerate(row_data):
                self.asatableWidget.setItem(row_number, x, QtWidgets.QTableWidgetItem(str(data)))
                x += 1
        connection.close()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(637, 549)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.asawidget = QtWidgets.QWidget(Form)
        self.asawidget.setGeometry(QtCore.QRect(20, 20, 601, 491))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.asawidget.setFont(font)
        self.asawidget.setStyleSheet("QPushButton#alogin{\n"
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
        self.asawidget.setObjectName("asawidget")
        self.asalabel = QtWidgets.QLabel(self.asawidget)
        self.asalabel.setGeometry(QtCore.QRect(170, 40, 411, 401))
        self.asalabel.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border-bottom-right-radius:50px")
        self.asalabel.setText("")
        self.asalabel.setObjectName("asalabel")
        self.asalabel_2 = QtWidgets.QLabel(self.asawidget)
        self.asalabel_2.setGeometry(QtCore.QRect(10, 20, 171, 431))
        self.asalabel_2.setStyleSheet("border-top-left-radius:50px;\n"
"background-color:rgba(0,0,0,80);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));")
        self.asalabel_2.setText("")
        self.asalabel_2.setObjectName("asalabel_2")
        self.asalabel_3 = QtWidgets.QLabel(self.asawidget)
        self.asalabel_3.setGeometry(QtCore.QRect(250, 50, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.asalabel_3.setFont(font)
        self.asalabel_3.setStyleSheet("color:rgba(0,0,0,200);")
        self.asalabel_3.setObjectName("asalabel_3")
        self.asalabel_5 = QtWidgets.QLabel(self.asawidget)
        self.asalabel_5.setGeometry(QtCore.QRect(20, 50, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.asalabel_5.setFont(font)
        self.asalabel_5.setStyleSheet("color:rgba(255,255,255,220);")
        self.asalabel_5.setObjectName("asalabel_5")
        self.asalabel_6 = QtWidgets.QLabel(self.asawidget)
        self.asalabel_6.setGeometry(QtCore.QRect(20, 200, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.asalabel_6.setFont(font)
        self.asalabel_6.setStyleSheet("color:rgba(255,255,255,220);")
        self.asalabel_6.setObjectName("asalabel_6")
        self.asaback = QtWidgets.QPushButton(self.asawidget)
        self.asaback.setGeometry(QtCore.QRect(470, 50, 81, 23))
        font = QtGui.QFont()
        font.setFamily("Wingdings 3")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.asaback.setFont(font)
        self.asaback.setStyleSheet("QPushButton{\n"
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
        self.asaback.setObjectName("asaback")
        self.asatableWidget = QtWidgets.QTableWidget(self.asawidget)
        self.asatableWidget.setGeometry(QtCore.QRect(190, 90, 311, 301))
        self.asatableWidget.setStyleSheet("border: 1px solid black;\n"
"")
        self.asatableWidget.setObjectName("asatableWidget")
        self.asatableWidget.setColumnCount(3)
        self.asatableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.asatableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.asatableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.asatableWidget.setHorizontalHeaderItem(2, item)
        self.asaback_2 = QtWidgets.QPushButton(self.asawidget)
        self.asaback_2.setGeometry(QtCore.QRect(290, 400, 111, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.asaback_2.setFont(font)
        self.asaback_2.setStyleSheet("QPushButton{\n"
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
        self.asaback_2.setObjectName("asaback_2")
        self.asaback.clicked.connect(self.passage3)
        self.asaback_2.clicked.connect(self.generate)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.asalabel_3.setText(_translate("Form", "Student Allocation"))
        self.asalabel_5.setText(_translate("Form", "Entrée-in"))
        self.asalabel_6.setText(_translate("Form", "Admin"))
        self.asaback.setText(_translate("Form", "8"))
        item = self.asatableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Name"))
        item = self.asatableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "College"))
        item = self.asatableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Stream"))
        self.asaback_2.setText(_translate("Form", "Generate List"))
        global check
        check = True
        if (check):
            global x
            x = Form
            check = False

    def adminca(self, x):
        self.window1 = QtWidgets.QMainWindow()
        self.ui = admin1.Ui_Form()
        self.ui.setupUi(self.window1)
        self.window1.show()
        x.close()

    def passage3(self):
        self.adminca(x)

    def generate(self):
        connection = sqlite3.connect("Project.db")
        sqlquery = "SELECT Total FROM Student_Information"
        result = connection.execute(sqlquery)
        total=result.fetchall()
        connection.commit()
        connection.close()
        list=[]
        for i in range(0,len(total)):
            list.append(total[i][0])
        list1=sorted(list,reverse=True)
        for i in list1:
            connection = sqlite3.connect("Project.db")
            student= connection.execute(f"SELECT S_Name FROM Student_Information where Total={i}")
            stu=student.fetchone()
            print(stu[0])
            connection.commit()
            connection.close()
            connection = sqlite3.connect("Project.db")
            Spl_user = connection.execute(f"SELECT * FROM Student_Verification where Username = '{stu[0]}'")
            recordpl = Spl_user.fetchone()
            per12=recordpl[12]
            print(per12)
            connection.commit()
            connection.close()
            connection = sqlite3.connect("Project.db")
            Spl_user = connection.execute(f"SELECT * FROM Col_Pref_list where Username = '{stu[0]}'")
            recordpl = Spl_user.fetchone()
            connection.commit()
            connection.close()
            for j in range(1,len(recordpl),2):
                college1=recordpl[j]
                stream1=recordpl[j+1]
                if stream1 == "Computer Science":
                    var=1
                elif stream1 == "Mechanics":
                    var=2
                    print("I am")
                else :
                    var=3
                    print("Dip")
                connection = sqlite3.connect("Project.db")
                check=connection.execute(f"select * from C_Stream_Count where College_Name ='{college1}'")
                result1=check.fetchone()
                connection.commit()
                connection.close()
                # s_count=result1[]
                if result1[var]<6:
                    print(college1)
                    print(stream1)
                    STUDENT=stu[0]
                    connection = sqlite3.connect("Project.db")
                    if per12 < 50:
                        print("12 th per i <50 not_qua")
                        connection = sqlite3.connect("Project.db")
                        connection.execute(f"Insert into Final_Generate (Student, College, Stream)VALUES(?, ?, ?)",(STUDENT, "Not_Qua",""))
                        connection.commit()
                        connection.close()
                        break
                    else:
                        connection = sqlite3.connect("Project.db")
                        connection.execute(f"Insert into Final_Generate (Student, College, Stream)VALUES(?, ?, ?)",(STUDENT, college1, stream1))
                        count=result1[var]+1
                        connection.commit()
                        connection.close()
                        print(count)
                        if var==1:
                            connection = sqlite3.connect("Project.db")
                            connection.execute(f"Update C_Stream_count set Count_Stream1={count} where College_Name = '{college1}'")
                            connection.commit()
                            connection.close()
                        elif var==2:
                            connection = sqlite3.connect("Project.db")
                            connection.execute(f"Update C_Stream_count set Count_Stream2={count} where College_Name = '{college1}'")
                            connection.commit()
                            connection.close()
                        else:
                            connection = sqlite3.connect("Project.db")
                            connection.execute(f"Update C_Stream_count set Count_Stream3={count} where College_Name = '{college1}'")
                            connection.commit()
                            connection.close()
                        print(result1)
                        break
                else:
                    print("hello")
        self.loadData()
            # except Exception as e:
            #     print(e)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
