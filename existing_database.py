# http://docs.peewee-orm.com/en/latest/peewee/models.html
import os
from peewee import *
from playhouse.reflection import generate_models, print_model , print_table_sql, Introspector
from pwiz import print_models

if os.path.exists('test.db'):
    baza = SqliteDatabase('test.db')
    if baza.connect():
        print('polaczenie do bazy danych udane')
        # http://docs.peewee-orm.com/en/latest/peewee/playhouse.html#pwiz
        models = generate_models(baza) # returns a dict mapping names to model classes
        print(models, models.keys())
        globals().update(models)
        # http://docs.peewee-orm.com/en/latest/peewee/playhouse.html#pwiz
        print_model(uczen)
        print_table_sql(uczen)
        Uczen = models['uczen']
        Klasa = models['klasa']
        print( Uczen._meta.fields )

        inst_klasa = klasa().select().where(klasa.id==2).get()
        print(inst_klasa)

        print('='*10,'sekcja introspector', '='*10)
        introspector1 = Introspector.from_database(baza)
        models1 = introspector1.generate_models()
        print(models1)

        if klasa().select().count() == 0:
            print("puste")

        if not baza.is_closed():
            print('zamykam polaczenie')
            baza.close()