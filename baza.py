# http://docs.peewee-orm.com/en/latest/peewee/models.html
import os
from peewee import *
from playhouse.reflection import generate_models, print_model, print_table_sql, Introspector

baza = SqliteDatabase("wyposazenie.db")
models = generate_models(baza)
globals().update(models) # Inject models into namespace
#print(models)
#print(models["dzialy"])
#print_model(models["dzialy"])
#print_table_sql(models["dzialy"])

class Dzialy(dzialy): #tworze klase Dzialy na podstawie modelu dzialy
    pass
class Stanowiska(stanowiska):
    pass
class Uzytkownicy(uzytkownicy):
    pass
class Sprzety(sprzety):
    pass

if not baza.is_closed():
    baza.close()
# ========= funkcja polacz =============
def polacz(nazwa_bazy_danych):
    if nazwa_bazy_danych.connect(): #nawiązujemy polaczenie z bazą danych
        print("polaczono za baza")
        print(models)
        return True
# ========= koniec funkcji polacz ======
def czytajDane():
    lista_wyp = []
    wpisy = Sprzety.select(Sprzety.id,Sprzety.nazwa,Sprzety.opis,Uzytkownicy.nazwisko,Uzytkownicy.imie,Uzytkownicy.id).\
        join(Uzytkownicy, on=(Sprzety.uzytkownicy_id == Uzytkownicy.id))
    for z in wpisy:
        lista_wyp.append([
            z.id,
            z.nazwa,
            z.opis,
            z.uzytkownicy.nazwisko,
            z.uzytkownicy.imie,
            z.uzytkownicy.id
        ])
    return lista_wyp
def czytajDaneFiltr1(nr_inw):
    lista_wyp1 = []
    rekordy = Sprzety.select().where(Sprzety.id==nr_inw)
    for r in rekordy:
        lista_wyp1.append([
            r.id,
            r.nazwa,
            r.opis,
            r.uzytkownicy.nazwisko,
            r.uzytkownicy.imie,
            r.uzytkownicy_id ])
    return lista_wyp1

pola = ['Nr inwent.', 'Nazwa', 'Opis', 'Nazwisko','Imie','id uzytkownika']