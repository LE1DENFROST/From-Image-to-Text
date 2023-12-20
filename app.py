from PyQt6 import QtCore, QtGui, QtWidgets
import os
import pytesseract

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(984, 428)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor(0, 0, 0))  
        palette.setColor(QtGui.QPalette.ColorRole.WindowText, QtGui.QColor(255, 255, 255)) 
        MainWindow.setPalette(palette)
        

        self.upload_image = QtWidgets.QLabel(parent=self.centralwidget)
        self.upload_image.setGeometry(QtCore.QRect(10, 10, 360, 351))
        self.upload_image.setObjectName("resim_yukleme_alani")


        self.varsayilan_resim = QtGui.QPixmap("Default_image\\default_image.jpg")
        self.upload_image.setPixmap(self.varsayilan_resim)
        self.upload_image.setScaledContents(True)
        self.upload_image.mousePressEvent = self.resim_yukle

        self.donustur = QtWidgets.QPushButton(parent=self.centralwidget)
        self.donustur.setGeometry(QtCore.QRect(380, 100, 101, 41))
        self.donustur.setObjectName("donustur")
        self.donustur.clicked.connect(self.resimden_yaziya)  

        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(490, 10, 481, 351))
        self.textEdit.setObjectName("textEdit")

        self.clear = QtWidgets.QPushButton(parent=self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(380, 150, 101, 41))
        self.clear.setObjectName("clear")
        self.clear.clicked.connect(self.temizle)  

        self.exit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(380, 200, 101, 41))
        self.exit.setObjectName("exit")
        self.exit.clicked.connect(self.cikis)  

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 984, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Savitar Resimden >> Yazıya v1.0"))
        self.donustur.setText(_translate("MainWindow", ">>>"))
        self.clear.setText(_translate("MainWindow", "CLEAR"))
        self.exit.setText(_translate("MainWindow", "EXIT"))


    def resim_yukle(self, event): 
        dosya_adı, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Resim Seç", "", "Resim Dosyaları (*.png *.jpg *.bmp);;Tüm Dosyalar (*)")
        if dosya_adı:
            resim = QtGui.QImage(dosya_adı)
            pixmap = QtGui.QPixmap.fromImage(resim)
            self.upload_image.setPixmap(pixmap)
            self.upload_image.setScaledContents(True)

    def resimden_yaziya(self):
        pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
        pixmap = self.upload_image.pixmap()
        image = pixmap.toImage()

        temp_file = "temp\\temp_image.png"
        image.save(temp_file, "PNG")

        a = pytesseract.image_to_string(temp_file, lang="tur")
        self.textEdit.setPlainText(a)

    def temizle(self):
        self.upload_image.setPixmap(self.varsayilan_resim)
        self.textEdit.clear()

    def cikis(self):
        if os.path.exists("temp\\temp_image.png") and os.path.isfile("temp\\temp_image.png"):
            os.remove("temp\\temp_image.png")
        QtWidgets.QApplication.quit()
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())