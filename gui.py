from PyQt5.QtWidgets import QTableView, QPushButton
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QLineEdit

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        self.tblViewSprzety= QTableView()
        self.btnKoniec = QPushButton("Koniec")
        self.btnAll = QPushButton("pokaz Sprzet")
        self.btnSzukaj = QPushButton("Szukaj nr inw")
        self.btnDodaj = QPushButton("dodaj Sprzet")
        self.btnUzytkownicy = QPushButton("Uzytkownicy")
        self.btnDzialy = QPushButton("Dzialy")
        self.btnStanowiska = QPushButton("Stanowiska")
        self.lneWprowadz = QLineEdit()
        self.lneWprowadz.setToolTip('wprowadz szukany nr inwentarzowy')

        ukladPrzyciskow = QHBoxLayout()
        ukladPrzyciskow.addWidget(self.btnUzytkownicy)
        ukladPrzyciskow.addWidget(self.btnDzialy)
        ukladPrzyciskow.addWidget(self.btnStanowiska)

        ukladPrzyciskow.addWidget(self.btnAll)
        ukladPrzyciskow.addWidget(self.btnDodaj)
        ukladPrzyciskow.addWidget(self.btnKoniec)
        uklSzukaj = QHBoxLayout()
        uklSzukaj.addWidget((self.lneWprowadz))
        uklSzukaj.addWidget(self.btnSzukaj)

        ukladOkna = QVBoxLayout(self)
        ukladOkna.addLayout(uklSzukaj)
        ukladOkna.addWidget(self.tblViewSprzety)
        ukladOkna.addLayout(ukladPrzyciskow)

        self.setWindowTitle("Wyposazenie")
        self.resize(500, 300)