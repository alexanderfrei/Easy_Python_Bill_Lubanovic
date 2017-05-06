# SQLite

import sqlite3
conn = sqlite3.connect('enterprise.db')
curs = conn.cursor()
print(type(conn))
print(type(curs))

curs.execute('''
CREATE TABLE zoo (critter VARCHAR(20) PRIMARY KEY, count INT, damages FLOAT)
''')

curs.execute('INSERT INTO zoo VALUES("duck", 5, 0.0)')
curs.execute('INSERT INTO zoo VALUES("bear", 2, 1000.0)')

# заполнитель, маска для защиты от SQL-инъекций

ins = 'INSERT INTO zoo (critter, count, damages) VALUES(?, ?, ?)'
curs.execute(ins, ('weasel', 1, 2000.0))
try:
    curs.execute(ins, ('vvvvv', 2000.0)) # запрос с ошибкой
except:
    print('Неверное число аргументов!')

curs.execute('SELECT * FROM zoo')
rows = curs.fetchall()
print(rows)

curs.execute('SELECT * FROM zoo ORDER BY count')
rows = curs.fetchall()
print(rows)

curs.execute('SELECT * FROM zoo WHERE damages = (SELECT MAX(damages) FROM zoo)')
rows = curs.fetchall()
print(rows)

curs.execute('DROP TABLE zoo')

curs.close()
conn.close()

# SQLAlchemy

print('------ SQL Alchemy ------')

import sqlalchemy as sa
conn = sa.create_engine('sqlite:///:memory:') # создание базы SQLlite в памяти
print(type(conn))
conn.execute('''
CREATE TABLE zoo (critter VARCHAR(20) PRIMARY KEY, count INT, damages FLOAT)
''')
ins = 'INSERT INTO zoo (critter, count, damages) VALUES(?, ?, ?)'

conn.execute(ins, ('duck', 5, 0.0))
conn.execute(ins, ('bear', 2, 1000.0))
conn.execute(ins, ('weasel', 1, 2000.0))

rows = conn.execute('SELECT * FROM zoo')
for row in rows:
    print(row)

# Язык выражений SQL

conn = sa.create_engine('sqlite:///:memory:')
meta = sa.MetaData() # используем схему языка выражений
zoo = sa.Table('zoo', meta,
               sa.Column('Critter', sa.String, primary_key=True),
               sa.Column('count', sa.Integer),
               sa.Column('damages', sa.Float))
meta.create_all(conn)
conn.execute(zoo.insert(('bear', 2, 1000.0)))
conn.execute(zoo.insert(('duck', 10, 0.0)))
conn.execute(zoo.insert(('weasel', 1, 2000.0)))
result = conn.execute(zoo.select())
rows = result.fetchall()
print(rows)

# ORM, Object-Relational Mapper
# вместо таблиц создаются классы, данные в таблицу добавляются объектами

from sqlalchemy.ext.declarative import declarative_base
conn = sa.create_engine('sqlite:///zoo.db')
Base = declarative_base()

class Zoo(Base): # класс таблицы
    __tablename__ = 'zoo'
    critter = sa.Column('critter', sa.String, primary_key=True)
    count = sa.Column('count', sa.Integer)
    damages = sa.Column('damages', sa.Float)
    def __init__(self, critter, count, damages):
        self.critter = critter
        self.count = count
        self.damages = damages
    def __repr__(self):
        return "<Zoo({}, {}, {})>".format(self.critter, self.count, self.damages)

Base.metadata.create_all(conn) # создание БД и таблицы
first = Zoo('duck', 10, 0.0) # создание объектов-записей
sec = Zoo('bear', 2, 1000.0)
thr = Zoo('weasel', 1, 2000.0)

print('---- ORM zoo.db ----')
print(first)
print(type(first))

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=conn)
session = Session()
session.add(first)
session.add_all([sec,thr])
session.commit()

# проверим содержимое zoo.db

conn = sqlite3.connect('zoo.db')
curs = conn.cursor()

curs.execute('SELECT * FROM zoo')
rows = curs.fetchall()
print(rows)
