from PyQt5.QtWidgets import QTableView, QPushButton
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QLineEdit
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QMessageBox, QInputDialog
import wyposazenie,baza
class Ui_Widget(object):
    def setupUi2(self, Widget):
        Widget.setObjectName("Widget1")
        self.tblViewUzytkownicy= QTableView()
        self.btnKoniec = QPushButton("Koniec")

        ukladPrzyciskow = QHBoxLayout()
        ukladPrzyciskow.addWidget(self.btnKoniec)

        ukladOkna = QVBoxLayout(self)
        ukladOkna.addWidget(self.tblViewUzytkownicy)
        ukladOkna.addLayout(ukladPrzyciskow)

        self.setWindowTitle("Uzytkownicy")
        self.resize(500, 300)

class Uzytkownicy(QWidget, Ui_Widget):
    def __init__(self, parent=None):
        super(Uzytkownicy, self).__init__(parent)
        self.setupUi2(self)
        self.btnKoniec.clicked.connect(self.koniec)
    def koniec(self):
        self.close()
    def odswiezWidokUzytkownicy(self):
        pass
    def wszystkieRecUzytkownicy(self):
            # zwraca listę wyp z przeczytanymi rekordami
            wyp = baza.czytajUzytkownicy()
            print(wyp)
            wyposazenie.modelUzytkownicy.aktualizuj(wyp)
            wyposazenie.modelUzytkownicy.layoutChanged.emit()
            #self.odswiezWidokUzytkownicy()
            self.tblViewUzytkownicy.resizeColumnsToContents()
            self.tblViewUzytkownicy.horizontalHeader().setStretchLastSection(True)
            self.tblViewUzytkownicy.setModel(wyposazenie.modelUzytkownicy)  # przekazanie modelu do widoku
            # self.tblViewUzytkownicy.hideColumn(3) #ukrycie kolumn id (0)
