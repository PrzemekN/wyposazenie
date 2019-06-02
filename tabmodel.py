from PyQt5.QtCore import QAbstractTableModel, QModelIndex, Qt,QVariant
class TabModel(QAbstractTableModel):
    #Tabelaryczny model danych"""
    def __init__(self, pola=[], dane=[],parent=None):
        #konstr. opcjonalnie przyjmuje liste pol i rekordow
        super(TabModel,self).__init__()
        self.pola = pola
        self.tabela= dane

    def aktualizuj(self, dane):
        #Przypisuje zrodlo danych do modelu
        print(dane) #w celach testowych
        self.tabela = dane

    def rowCount(self, parent=QModelIndex()):
        # zwraca ilosc wierszy
        return len(self.tabela)

    def columnCount(self, parent=QModelIndex()):
        if self.tabela:
            return len(self.tabela[0])
        else:
            return 0

    def data(self, index, rola=Qt.DisplayRole):
        #wyswietlanie danych
        i = index.row()
        j = index.column()
        if rola == Qt.DisplayRole:
            return '{0}'.format(self.tabela[i][j])
        #else:
        #    return #QVariant

    def headerData(self, sekcja, kierunek, rola=Qt.DisplayRole):
        """ Zwraca nagłówki kolumn """
        if rola == Qt.DisplayRole and kierunek == Qt.Horizontal:
            return self.pola[sekcja]
        elif rola == Qt.DisplayRole and kierunek == Qt.Vertical:
            return sekcja + 1
        else:
            return QVariant()
