# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import os
from PyQt5 import QtCore, QtGui, QtWidgets
CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

class Ui_Translator(object):
    def setupUi(self, Translator):
        Translator.setObjectName("Translator")
        Translator.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setBold(False)
        font.setWeight(50)
        Translator.setFont(font)
        icon = QtGui.QIcon()
        print('cd in gui: {}'.format(CURRENT_DIRECTORY))
        #icon_path=CURRENT_DIRECTORY+"'/gov_logo4.ico'"
        icon_path="'gov_logo4.ico'"
        icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Normal)
        
        Translator.setWindowIcon(icon)
        Translator.setStyleSheet("QTextEdit\n"
"{\n"
"    background-color:white;\n"
"    padding:15px 15px;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    background-color:rgb(52, 101, 164);\n"
"    color:white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color:rgb(115, 210, 22);\n"
"}")
        self.label = QtWidgets.QLabel(Translator)
        self.label.setGeometry(QtCore.QRect(170, 40, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Translator)
        self.textEdit.setGeometry(QtCore.QRect(30, 160, 350, 250))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Translator)
        self.textEdit_2.setGeometry(QtCore.QRect(420, 160, 350, 250))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(12)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_2 = QtWidgets.QLabel(Translator)
        self.label_2.setGeometry(QtCore.QRect(39, 133, 131, 17))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(Translator)
        self.comboBox.setGeometry(QtCore.QRect(110, 127, 271, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(Translator)
        self.comboBox_2.setGeometry(QtCore.QRect(493, 126, 271, 25))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_3 = QtWidgets.QLabel(Translator)
        self.label_3.setGeometry(QtCore.QRect(422, 132, 131, 17))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Translator)
        self.pushButton.setGeometry(QtCore.QRect(340, 451, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Translator)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 420, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(Translator)
        self.label_4.setGeometry(QtCore.QRect(445, 40, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Jameel Noori Kasheeda")
        font.setPointSize(20)
        #font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Translator)
        self.label_5.setGeometry(QtCore.QRect(220, 530, 330, 51))
        font = QtGui.QFont()
        font.setFamily("Jameel Noori Kasheeda")
        font.setPointSize(22)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(Translator)
        self.label_7.setGeometry(QtCore.QRect(550, 440, 131, 131))
        self.label_7.setText("")
        #label7_path=CURRENT_DIRECTORY+"/gov_logo3.png"
        label7_path="gov_logo3.png"
        self.label_7.setPixmap(QtGui.QPixmap(label7_path))
        self.label_7.setScaledContents(True)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Translator)
        QtCore.QMetaObject.connectSlotsByName(Translator)

    def retranslateUi(self, Translator):
        _translate = QtCore.QCoreApplication.translate
        Translator.setWindowTitle(_translate("Translator", "Python Google Translator by Mohammad Ayyaz Azeem Version 1"))
        self.label.setText(_translate("Translator", "Python Google Translator"))
        self.textEdit.setPlaceholderText(_translate("Translator", "Write your text here!"))
        self.label_2.setText(_translate("Translator", "Select Language"))
        self.label_3.setText(_translate("Translator", "Select Language"))
        self.pushButton.setText(_translate("Translator", "Translation"))
        self.pushButton_2.setText(_translate("Translator", "Clear"))
        self.label_4.setText(_translate("Translator", "پاہتھن گوگل مترجم"))
        self.label_5.setText(_translate("Translator", "ادارۂ فروغِ قومی زبان (مقتدرہ قومی زبان)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Translator = QtWidgets.QWidget()
    ui = Ui_Translator()
    ui.setupUi(Translator)
    Translator.show()
    sys.exit(app.exec_())
