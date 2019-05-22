from PyQt5.QtWidgets import QTableView, QPushButton
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QLineEdit
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QMessageBox, QInputDialog

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget1")
        self.tblViewDzialy1= QTableView()
        self.btnKoniec = QPushButton("Koniec")

        ukladPrzyciskow = QHBoxLayout()
        ukladPrzyciskow.addWidget(self.btnKoniec)

        ukladOkna = QVBoxLayout(self)
        ukladOkna.addLayout(ukladPrzyciskow)

        self.setWindowTitle("Uzytkownicy")
        self.resize(500, 300)

class Uzytkownicy(QWidget, Ui_Widget):
    def __init__(self, parent=None):
        super(Uzytkownicy, self).__init__(parent)
        self.setupUi(self)
        self.btnKoniec.clicked.connect(self.koniec)

    def koniec(self):
        self.close()
