import os
from peewee import *
if os.path.exists('test.db'):
    os.remove('test.db')

baza = SqliteDatabase('test.db')

class BazaModel(Model):
    class Meta:
        database = baza

class Klasa(BazaModel):

    nazwa = CharField(null=False)
    profil = CharField(default='')

class Uczen(BazaModel):
    imie = CharField(null=False)
    nazwisko = CharField(null=False)
    klasa = ForeignKeyField(Klasa,related_name='uczniowie')

baza.connect()
baza.create_tables([Klasa, Uczen])

# jeseli tabela jest pusta dodajemy dwa wiersze
if Klasa().select().count() == 0:
    inst_klasa = Klasa(nazwa='1A', profil='matematyczny')
    inst_klasa.save()
    inst_klasa = Klasa(nazwa='1B', profil='humanistyczny')
    inst_klasa.save()
    inst_klasa = Klasa(nazwa='1C', profil='informatyczny')
    inst_klasa.save()

# tworzymy instancje klasy Klasa reprezentująca szkolna klasę 1A
inst_klasa = Klasa.select().where(Klasa.nazwa == '1A').get()
print(inst_klasa)
# get() zwraca tu rekordu dla nazwa='1A' ,natomiast samo inst_klasa zwraca id tak samo jak bys napisał inst_klasa.id
# ale mozna tez tak inst_klasa.id lub inst_klasa.nazwa

# przygotowujemy liste uczniow
uczniowie = [
    {'imie':'Tomasz','nazwisko':'Nowak','klasa': inst_klasa},
    {'imie':'Jan','nazwisko':'Kos','klasa': inst_klasa},
    {'imie':'Piotr','nazwisko':'Kowalski','klasa':2}
]

# dodamy teraz do bazy liste uczniow wczesniej przygotowaną
Uczen.insert_many(uczniowie).execute()

# odczytujemy dane z klasy
def czytajdane():
    for uczen in Uczen.select().join(Klasa):
        print(uczen.id, uczen.imie, uczen.nazwisko, uczen.klasa.nazwa)
    print()
czytajdane()

# zmiana klasy przypisanej uczniow o identyfikatorze id=2
inst_uczen = Uczen().select().join(Klasa).where(Uczen.id == 2).get()
print(inst_uczen.klasa)
print(Uczen().select().join(Klasa).where(Uczen.id == 2))
wynik = Uczen().select().join(Klasa).where(Uczen.id == 2)
print("tak tez mozna",wynik[0].id,wynik[0].nazwisko,wynik[0].imie,wynik[0].klasa)
inst_uczen.klasa = Klasa.select().where(Klasa.nazwa == '1B').get()


# usuniecie ucznia o identyfikatorze 3
Uczen.select().where(Uczen.id == 3).get().delete_instance()

inst_uczen.save()
czytajdane()
print(inst_uczen)
print(inst_uczen.klasa)
baza.close()


# ok ale jak zrobic by nie tworzyl nowej bazy danych a wykorzystal istniejaca i odczytał jej strukture.