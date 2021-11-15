# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createaccUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import test


class CreateAccUI_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 560)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, -2, 300, 560))
        self.label.setStyleSheet("background-color: rgb(248, 248, 248);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(110, 30, 111, 41))
        font = QtGui.QFont()
        font.setFamily("나눔고딕 ExtraBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.unameLineEdit = QtWidgets.QLineEdit(Dialog)
        self.unameLineEdit.setGeometry(QtCore.QRect(40, 190, 230, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.unameLineEdit.setFont(font)
        self.unameLineEdit.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
                                         "border:none;\n"
                                         "border-bottom: 2px solid rgba(46, 82, 101, 200);\n"
                                         "color: rgba(0, 0, 0, 240);\n"
                                         "padding-bottom:7px;")
        self.unameLineEdit.setText("")
        self.unameLineEdit.setObjectName("unameLineEdit")
        self.emailLineEdit = QtWidgets.QLineEdit(Dialog)
        self.emailLineEdit.setGeometry(QtCore.QRect(40, 260, 230, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.emailLineEdit.setFont(font)
        self.emailLineEdit.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
                                         "border:none;\n"
                                         "border-bottom: 2px solid rgba(46, 82, 101, 200);\n"
                                         "color: rgba(0, 0, 0, 240);\n"
                                         "padding-bottom:7px;")
        self.emailLineEdit.setText("")
        self.emailLineEdit.setObjectName("emailLineEdit")
        self.pwLineEdit = QtWidgets.QLineEdit(Dialog)
        self.pwLineEdit.setGeometry(QtCore.QRect(40, 330, 230, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pwLineEdit.setFont(font)
        self.pwLineEdit.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
                                      "border:none;\n"
                                      "border-bottom: 2px solid rgba(46, 82, 101, 200);\n"
                                      "color: rgba(0, 0, 0, 240);\n"
                                      "padding-bottom:7px;")
        self.pwLineEdit.setText("")
        self.pwLineEdit.setObjectName("pwLineEdit")
        self.confirmpwLineEdit = QtWidgets.QLineEdit(Dialog)
        self.confirmpwLineEdit.setGeometry(QtCore.QRect(40, 400, 230, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.confirmpwLineEdit.setFont(font)
        self.confirmpwLineEdit.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
                                             "border:none;\n"
                                             "border-bottom: 2px solid rgba(46, 82, 101, 200);\n"
                                             "color: rgba(0, 0, 0, 240);\n"
                                             "padding-bottom:7px;")
        self.confirmpwLineEdit.setText("")
        self.confirmpwLineEdit.setObjectName("confirmpwLineEdit")
        self.signupButton = QtWidgets.QPushButton(Dialog)
        self.signupButton.setGeometry(QtCore.QRect(40, 470, 230, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.signupButton.setFont(font)
        self.signupButton.setObjectName("signupButton")
        self.agreeCheckBox = QtWidgets.QCheckBox(Dialog)
        self.agreeCheckBox.setGeometry(QtCore.QRect(40, 530, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.agreeCheckBox.setFont(font)
        self.agreeCheckBox.setObjectName("agreeCheckBox")
        self.gobackButton = QtWidgets.QPushButton(Dialog)
        self.gobackButton.setGeometry(QtCore.QRect(30, 30, 30, 30))
        self.gobackButton.setStyleSheet("border-image: url(:/newPrefix/backarrow.png);\n"
                                        "background-color: rgb(248, 248, 248);\n"
                                        "")
        self.gobackButton.setText("")
        self.gobackButton.setObjectName("gobackButton")
        self.loadButton = QtWidgets.QPushButton(Dialog)
        self.loadButton.setGeometry(QtCore.QRect(140, 160, 50, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.loadButton.setFont(font)
        self.loadButton.setObjectName("loadButton")
        self.imageLabel = QtWidgets.QLabel(Dialog)
        self.imageLabel.setGeometry(QtCore.QRect(40, 100, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.imageLabel.setFont(font)
        self.imageLabel.setStyleSheet("border-width: 1px 1px 1px 1px;\n"
                                      "border-color: rgba(0, 0, 0, 255);\n"
                                      "border-style:dashed dashed dashed dashed;")
        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imageLabel.setObjectName("imageLabel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Sign Up"))
        self.unameLineEdit.setPlaceholderText(
            _translate("Dialog", "User name"))
        self.emailLineEdit.setPlaceholderText(
            _translate("Dialog", "Email Address"))
        self.pwLineEdit.setPlaceholderText(_translate("Dialog", "Password"))
        self.confirmpwLineEdit.setPlaceholderText(
            _translate("Dialog", "Confirm Password"))
        self.signupButton.setText(_translate("Dialog", "Sign Up"))
        self.agreeCheckBox.setText(_translate(
            "Dialog", "I agree to create account"))
        self.loadButton.setText(_translate("Dialog", "load"))
        self.imageLabel.setText(_translate("Dialog", "Image"))
