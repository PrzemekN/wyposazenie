from PyQt5.QtWidgets import QTableView, QPushButton
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        self.tblViewDzialy1= QTableView()

        self.btnKoniec = QPushButton("Koniec")
        self.btnDalej = QPushButton("Dalej")

        ukladPrzyciskow = QHBoxLayout()
        ukladPrzyciskow.addWidget(self.btnKoniec)
        ukladPrzyciskow.addWidget(self.btnDalej)

        ukladOkna = QVBoxLayout(self)
        ukladOkna.addWidget(self.tblViewDzialy1)
        ukladOkna.addLayout(ukladPrzyciskow)

        self.setWindowTitle("widokDzialow")
        self.resize(500, 300)