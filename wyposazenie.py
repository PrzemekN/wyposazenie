from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QMessageBox, QInputDialog
from tabmodel import TabModel
from gui import *
import baza
import uzytkownicy

class Wyposazenie(QWidget, Ui_Widget):
    def __init__(self, parent=None):
        super(Wyposazenie, self).__init__(parent)
        self.setupUi(self)
        self.btnKoniec.clicked.connect(self.koniec)
        self.btnAll.clicked.connect(self.wszystkieRecSprzety)
        self.btnDodaj.clicked.connect(self.dodaj)
        self.btnSzukaj.clicked.connect(self.szukaj_nr_inw)
        self.btnUzytkownicy.clicked.connect(self.btnUzytkownicyClick)

# metoda wywolywana po nacisnieciu przycisku btnUzytkownicy
    def btnUzytkownicyClick(self):
        self.oknoUzytkownicy = uzytkownicy.Uzytkownicy()
        #self.oknoUzytkownicy.wszystkieRecUzytkownicy()
        self.oknoUzytkownicy.show()
        self.oknoUzytkownicy.move(360, 230)

    def dodaj(self):
        '''dodawanie nowego wpisu'''
    def szukaj_nr_inw(self):
        if (self.lneWprowadz.text()):
            w = baza.czytajDaneFiltr1(self.lneWprowadz.text())
            modelSprzety.aktualizuj(w)
            modelSprzety.layoutChanged.emit()
            self.odswiezWidok()
        else:
            print("wprowadz nr inw")

    def koniec(self):
        self.close()
    def wszystkieRecSprzety(self):
            wyp = baza.czytajDane()
            modelSprzety.aktualizuj(wyp)
            modelSprzety.layoutChanged.emit()
            self.odswiezWidok()
    def odswiezWidok(self):
        self.tblViewSprzety.resizeColumnsToContents()
        self.tblViewSprzety.horizontalHeader().setStretchLastSection(True)
        self.tblViewSprzety.setModel(modelSprzety)  # przekazanie modelu do widoku
        #self.tblViewSprzety.hideColumn(3) #ukrycie kolumn id (0)
# ---------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    baza.polacz(baza.baza)
    modelSprzety = TabModel(baza.polaSprzety)
    modelUzytkownicy = TabModel(baza.polaUzytkownicy)
    oknoGlowne = Wyposazenie()
    oknoGlowne.wszystkieRecSprzety()
    oknoGlowne.show()
    oknoGlowne.move(350, 200)
    sys.exit(app.exec_())

