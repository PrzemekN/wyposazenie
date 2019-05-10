from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QMessageBox, QInputDialog
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
            QMessageBox.information(self,'Potwierdzenie','Wprowadzono:'+wpisanyText,
                                    QMessageBox.Ok)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    baza.polacz(baza.baza)
    oknoGlowne = Wyposazenie()
    oknoGlowne.show()
    oknoGlowne.move(350, 200)
    sys.exit(app.exec_())

