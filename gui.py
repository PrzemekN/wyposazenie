from PyQt5.QtWidgets import QTableView, QPushButton
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QLineEdit

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        self.tblViewDzialy1= QTableView()
        self.btnKoniec = QPushButton("Koniec")
        self.btnAll = QPushButton("Pokaz wszystko")
        self.btnSzukaj = QPushButton("Szukaj nr inw")
        self.btnDodaj = QPushButton("Dodaj")
        self.lneWprowadz = QLineEdit()
        self.lneWprowadz.setToolTip('wprowadz szukany nr inwentarzowy')

        ukladPrzyciskow = QHBoxLayout()
        ukladPrzyciskow.addWidget(self.btnKoniec)
        ukladPrzyciskow.addWidget(self.btnDodaj)
        ukladPrzyciskow.addWidget(self.btnAll)
        uklSzukaj = QHBoxLayout()
        uklSzukaj.addWidget((self.lneWprowadz))
        uklSzukaj.addWidget(self.btnSzukaj)

        ukladOkna = QVBoxLayout(self)
        ukladOkna.addLayout(uklSzukaj)
        ukladOkna.addWidget(self.tblViewDzialy1)
        ukladOkna.addLayout(ukladPrzyciskow)

        self.setWindowTitle("Wyposazenie")
        self.resize(500, 300)