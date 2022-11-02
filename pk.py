import sqlite3 as sql 

odamlar = sql.connect("odamlar.db")

malumot = odamlar.cursor()

malumot.execute('''
CREATE TABLE IF NOT EXISTS Programmistlar(
    ism TEXT,
    familya TEXT,
    yosh INTEGER
)

''')

malumot.execute('''
CREATE TABLE IF NOT EXISTS Studentlar(
    ism TEXT,
    familya TEXT,
    yosh INTEGER
)

''')

malumot.execute('''
CREATE TABLE IF NOT EXISTS Bekorchilar(
    ism TEXT,
    familya TEXT,
    yosh INTEGER
)

''')