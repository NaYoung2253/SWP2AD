# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'todolistUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import test


class TodolistUI_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 600)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 400, 200))
        self.label.setStyleSheet(
            "border-image: url(:/newPrefix/sky_background.jpg);")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.additemButton = QtWidgets.QPushButton(Dialog)
        self.additemButton.setGeometry(QtCore.QRect(290, 490, 80, 80))
        self.additemButton.setStyleSheet("border: 2px;\n"
                                         "border-radius: 40px;\n"
                                         "background-color: rgb(0, 180, 220);")
        self.additemButton.setText("")
        self.additemButton.setObjectName("additemButton")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 200, 400, 400))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 90, 90))
        self.label_3.setStyleSheet("border: 2px;\n"
                                   "border-radius: 40px;\n"
                                   "background-color: rgb(85, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label.raise_()
        self.label_2.raise_()
        self.additemButton.raise_()
        self.label_3.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "TextLabel"))