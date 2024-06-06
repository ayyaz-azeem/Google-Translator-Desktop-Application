import sys
import gui
import googletrans
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox
import os

CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

class Main(QtWidgets.QMainWindow, gui.Ui_Translator):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)

        print('cd: {}'.format(CURRENT_DIRECTORY))
        #icon_path = CURRENT_DIRECTORY+'/gov_logo4.ico'
        icon_path = 'gov_logo4.ico'
        self.setWindowIcon(QtGui.QIcon(icon_path))
        print('icon_path: {}'.format(icon_path))
        
        self.setupUi(self)
        self.textEdit.clear()
        self.add_languages()

        self.pushButton.clicked.connect(self.translate)
        self.pushButton_2.clicked.connect(self.clear)

    def add_languages(self):
        for x in googletrans.LANGUAGES.values():
            self.comboBox.addItem(x.capitalize())
            self.comboBox_2.addItem(x.capitalize())
    
    def translate(self):
        try:
            text_1 = self.textEdit.toPlainText()
            lang_1 = self.comboBox.currentText()
            lang_2 = self.comboBox_2.currentText()

            #font=QtGui.QFont()
            #print('current font: {}'.format(font.getFont))
            font_size = 15
            if(lang_1=="Urdu"):
                print('lang_1 is {}'.format(lang_1))
                #font.setCurrentFont("Jameel Noori Nastaleeq")
                #self.textEdit.setFont(font)
                #Jameel Noori Kasheeda
                #self.textEdit.setFont(QtGui.QFont("Jameel Noori Nastaleeq",font_size))
                self.textEdit.setFont(QtGui.QFont("Jameel Noori Kasheeda",font_size))

            if(lang_2=="Urdu"):
                print('lang_2 is {}'.format(lang_2))
                #font.setCurrentFont("Jameel Noori Nastaleeq")
                #self.textEdit_2.setFont(font)
                #self.textEdit_2.setFont(QtGui.QFont("Jameel Noori Nastaleeq",font_size))
                self.textEdit_2.setFont(QtGui.QFont("Jameel Noori Kasheeda",font_size))

            translator = googletrans.Translator()
            translate = translator.translate(text_1, src = lang_1, dest = lang_2)
            self.textEdit_2.setText(translate.text)
        except Exception as e:
            print(f'Exception thrown at point A: {e}')
            self.error_message(e)
            #pass

    def error_message(self,text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle('Error')
        msg.setText(str(text))
        msg.exec_()
    
    def clear(self):
        self.textEdit.clear()
        self.textEdit_2.clear()

if __name__ == '__main__':
    a=QtWidgets.QApplication(sys.argv)
    
    font_path=os.path.join(CURRENT_DIRECTORY,"JameelNooriNastaleeqKasheeda.ttf")
    #JJameelNooriKasheedaRegular.ttf
    font_path_2=os.path.join(CURRENT_DIRECTORY,"JJameelNooriKasheedaRegular.ttf")
    print('font_path: {}'.format(font_path))
    print('font_path: {}'.format(font_path_2))
    _id = QtGui.QFontDatabase.addApplicationFont(font_path)
    if (QtGui.QFontDatabase.applicationFontFamilies(_id)==-1):
        print("problem loading font 1")
        sys.exit(-1)
    _id_2 = QtGui.QFontDatabase.addApplicationFont(font_path_2)
    if (QtGui.QFontDatabase.applicationFontFamilies(_id_2)==-1):
        print("problem loading font 2")
        sys.exit(-1)
    
    app=Main()
    app.show()
    a.exec_()
