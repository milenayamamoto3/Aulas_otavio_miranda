import sqlite3

from main import DB_FILE, TABLE_NAME

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# SELECT serve para consulta
cursor.execute(f"SELECT * FROM {TABLE_NAME}")  # *(all)
# cursor.execute(
#     f'SELECT * FROM {TABLE_NAME} LIMIT 2'
# ) # limita até os dois primeiros registros

# fechall = todos os registros
for row in cursor.fetchall():
    _id, name, weight = row
    print(_id, name, weight)

print()

# fechone() = 1º registro sem o WHERE
cursor.execute(f"SELECT * FROM {TABLE_NAME} " 'WHERE id = "3"')
row = cursor.fetchone()  # não pega argumento
_id, name, weight = row
print(_id, name, weight)

cursor.close()
connection.close()
