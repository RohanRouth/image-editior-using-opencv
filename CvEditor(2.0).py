# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'opencv_editor.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!



from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import cv2
from matplotlib import pyplot as plt
import numpy as np

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(550, 347)
        Form.setStyleSheet("font: italic 8pt \"Arial\";\n"
"")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(70, 20, 421, 161))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/opencv_logo.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(130, 210, 287, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"font: 9pt \"MS Shell Dlg 2\";\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.toolButton = QtWidgets.QToolButton(self.layoutWidget)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout_2.addWidget(self.toolButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(150, 280, 239, 38))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.push_original = QtWidgets.QPushButton(self.layoutWidget1)
        self.push_original.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.push_original.setObjectName("push_original")
        self.horizontalLayout_3.addWidget(self.push_original)
        self.push_convert = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_convert.sizePolicy().hasHeightForWidth())
        self.push_convert.setSizePolicy(sizePolicy)
        self.push_convert.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.push_convert.setObjectName("push_convert")
        self.horizontalLayout_3.addWidget(self.push_convert)
        self.toolButton.clicked.connect(self.select_photo)
        self.push_convert.clicked.connect(self.convert)
        self.push_original.clicked.connect(self.show_og)




        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "CvEditor-2.0"))
        self.label.setText(_translate("Form", "select image:"))
        self.toolButton.setText(_translate("Form", "..."))
        self.label_2.setText(_translate("Form", "select operation:"))
        self.comboBox.setItemText(0, _translate("Form", "greyscale"))
        self.comboBox.setItemText(1, _translate("Form", "histogram"))
        self.comboBox.setItemText(2, _translate("Form", "histogram-equalization"))
        self.comboBox.setItemText(3, _translate("Form", "negative"))
        self.comboBox.setItemText(4, _translate("Form", "face-eye-detection"))
        self.push_original.setText(_translate("Form", "show original"))
        self.push_convert.setText(_translate("Form", "convert!"))

    def select_photo(self):
        photo_path, ext = QFileDialog.getOpenFileName()
        if photo_path:
            self.lineEdit.setText(photo_path)

    def get_photo_path(self):
        photo_loc = self.lineEdit.text()
        return photo_loc

    def get_operation(self):
        opn = self.comboBox.currentText()
        return opn

    def photo_error(self):
        QMessageBox.about(self, "Error", "please select photo!")

    def opn_error(self):
        QMessageBox.about(self, "Title", "Message")

    def convert(self):
        photo = self.get_photo_path()
        option = self.get_operation()

        if option == "greyscale":
            img = cv2.imread(photo,0)
            cv2.imshow('greyscale',img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif option == "histogram":
            img = cv2.imread(photo,0)
            histr = cv2.calcHist([img],[0],None,[256],[0,256])
            plt.plot(histr)
            plt.show()
        elif option == "histogram-equalization":
            img = cv2.imread(photo, 0)
            equ = cv2.equalizeHist(img)
            res = np.hstack((img, equ))
            cv2.imshow('histogram-equalization', res)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif option == "negative":
            img = cv2.imread(photo,0)
            img = 255 - img
            cv2.imshow('lena',img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif option ==  "face-eye-detection":
            l1 = "C:\\Users\\Rohan\\Desktop\\opencv\\haarcascade_frontalface_default.xml"
            l2 =  "C:\\Users\\Rohan\\Desktop\\opencv\\haarcascade_eye.xml"
            face_cascade = cv2.CascadeClassifier(l1)
            eye_cascade = cv2.CascadeClassifier(l2)

            img = cv2.imread(photo)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]
                eyes = eye_cascade.detectMultiScale(roi_gray)
                for (ex,ey,ew,eh) in eyes:
                    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

                    cv2.imshow('img',img)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()

    def show_og(self):
        photo = self.get_photo_path()
        read_photo = cv2.imread(photo)
        cv2.imshow('original',read_photo)
        cv2.waitKey(0)
        cv2.destroyAllWindows()










import opencv_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
