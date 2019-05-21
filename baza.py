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
    wpisy = Sprzety.select()
    for z in wpisy:
        lista_wyp.append([
            z.id,
            z.nazwa,
            z.opis,
            z.uzytkownicy_id ])
    return lista_wyp

pola = ['Nr inwentarzowy', 'Nazwa', 'Opis', 'Zrobione', ]