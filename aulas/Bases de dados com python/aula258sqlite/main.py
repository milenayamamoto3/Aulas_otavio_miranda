# Documento da sqlie https://www.sqlite.org/doclist.html
# tutorial https://www.techonthenet.com/sqlite/index.php

import sqlite3  # já vem com o python
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = "db.sqlite3"
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = "customers"

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# Cria a tabela (SQL)
# integer(int), text(str), real(float), autoincrement(autoincremento)
cursor.execute(
    f"CREATE TABLE IF NOT EXISTS {TABLE_NAME}"
    "("
    "id INTEGER PRIMARY KEY AUTOINCREMENT,"
    "name TEXT,"
    "weight REAL"
    ")"
)
connection.commit()

# CUIDADO: fazendo delete sem where

# Deleta os id da tabela, mas a sequencia para novos valores continua
cursor.execute(f"DELETE FROM {TABLE_NAME}")
connection.commit()

# Deleta os id da tabela "sequence"=tabela onde fica os id deletados
cursor.execute(f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"')
connection.commit()

# Registrar valores nas colunas da tabela
# cursor.executemany() # para vários valores
# é acumulativo, então, se comitar de nv, irá duplicar os valores abaixo
# CUIDADO: sql injection (quando o user digita algo em seu código)

# cursor.execute(
#     f"INSERT INTO {TABLE_NAME} "
#     "(id, name, weight) "
#     "VALUES "
#     '(NULL, "Helena", 4), (NULL, "Eduardo", 10)'
# )

# associando valores aos parâmetros na consulta SQL

# "?"=bindings posicionais, placeholders - valore em list or tuple
# sql = f"INSERT INTO {TABLE_NAME} " "(name, weight) " "VALUES " "(?, ?)"
# cursor.execute(sql, ["Joana", 4])  # adc valores de 1 id
# cursor.executemany(
#     sql, (("Isa", 4), ("Luiz", 5))
# )  # adc valores de muitos id

# ":nome específico"=bindings nomeados - valores em dict
sql = f"INSERT INTO {TABLE_NAME} " "(name, weight) " "VALUES " "(:nome, :peso)"
cursor.execute(sql, {"nome": "Sem nome", "peso": 3})
cursor.executemany(
    sql,
    (
        {"nome": "Joãozinho", "peso": 3},
        {"nome": "Maria", "peso": 2},
        {"nome": "Helena", "peso": 4},
        {"nome": "Joana", "peso": 5},
    ),
)

connection.commit()

cursor.close()
connection.close()
