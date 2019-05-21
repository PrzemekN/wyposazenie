from PyQt5.QtWidgets import QTableView, QPushButton
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QLineEdit

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        self.tblViewDzialy1= QTableView()
        self.btnKoniec = QPushButton("Koniec")
        self.btnDalej = QPushButton("Dalej")
        self.btnSzukaj = QPushButton("Szukaj")
        self.btnDodaj = QPushButton("Dodaj")
        self.lneWprowadz = QLineEdit()
        self.lneWprowadz.setToolTip('wprowadz szukany ciag')

        ukladPrzyciskow = QHBoxLayout()
        ukladPrzyciskow.addWidget(self.btnKoniec)
        ukladPrzyciskow.addWidget(self.btnDodaj)
        ukladPrzyciskow.addWidget(self.btnDalej)
        uklSzukaj = QHBoxLayout()
        uklSzukaj.addWidget((self.lneWprowadz))
        uklSzukaj.addWidget(self.btnSzukaj)

        ukladOkna = QVBoxLayout(self)
        ukladOkna.addLayout(uklSzukaj)
        ukladOkna.addWidget(self.tblViewDzialy1)
        ukladOkna.addLayout(ukladPrzyciskow)

        self.setWindowTitle("widokDzialow")
        self.resize(800, 300)