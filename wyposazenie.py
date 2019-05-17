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

    def koniec(self):
        self.close()
    def dalej(self):
        wpisanyText, czyOk = QInputDialog.getText(self,'Test','wpr cos:')
        if czyOk:
            wyp =baza.czytajDane()
            model.aktualizuj(wyp)
            model.layoutChanged.emit()
            self.odswiezWidok()

    def odswiezWidok(self):
        #ograniczenie szer. ostatniej kolumny
        self.tblViewDzialy1.horizontalHeader().setStretchLastSection(True)
        # dopasowanie szer. kol do zawartosci
        self.tblViewDzialy1.resizeColumnsToContents()
        self.tblViewDzialy1.setModel(model) #przekazanie modelu do widoku
        # self.tblViewDzialy1.hideColumn(0) #ukrycie kolumn id (0)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    baza.polacz(baza.baza)
    model = TabModel()
    oknoGlowne = Wyposazenie()
    oknoGlowne.show()
    oknoGlowne.move(350, 200)
    sys.exit(app.exec_())

