from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QMessageBox, QInputDialog
from tabmodel import TabModel
from gui import *
import baza

class Wyposazenie(QWidget, Ui_Widget):
    def __init__(self, parent=None):
        super(Wyposazenie, self).__init__(parent)
        self.setupUi(self)
        self.btnKoniec.clicked.connect(self.koniec)
        self.btnDalej.clicked.connect(self.dalej)
        self.btnDodaj.clicked.connect(self.dodaj)
    def dodaj(self):
        '''dodawanie nowego wpisu'''

    def koniec(self):
        self.close()
    def dalej(self):
            wyp = baza.czytajDane()
            model.aktualizuj(wyp)
            model.layoutChanged.emit()
            self.odswiezWidok()
    def odswiezWidok(self):
        self.tblViewDzialy1.resizeColumnsToContents()
        self.tblViewDzialy1.horizontalHeader().setStretchLastSection(True)
        self.tblViewDzialy1.setModel(model)  # przekazanie modelu do widoku
        self.tblViewDzialy1.hideColumn(3) #ukrycie kolumn id (0)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    baza.polacz(baza.baza)
    model = TabModel(baza.pola)
    oknoGlowne = Wyposazenie()
    oknoGlowne.dalej()
    oknoGlowne.show()
    oknoGlowne.move(350, 200)

    sys.exit(app.exec_())

