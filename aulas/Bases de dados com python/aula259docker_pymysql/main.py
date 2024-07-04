# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypi: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
import os
import pymysql
import pymysql.cursors
import dotenv

TABLE_NAME = "customers"
dotenv.load_dotenv()
connection = pymysql.connect(
    host=os.environ["MYSQL_HOST"],
    user=os.environ["MYSQL_USER"],
    password=os.environ["MYSQL_PASSWORD"],
    database=os.environ["MYSQL_DATABASE"],
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor,
)

# Usando o gerenciador de contexto para a conexão e o cursor serem fechados depois
with connection:
    with connection.cursor() as cursor:
        # SQL
        cursor.execute(  # type: ignore
            f"CREATE TABLE IF NOT EXISTS {TABLE_NAME} ("
            "id INT NOT NULL AUTO_INCREMENT, "
            "nome VARCHAR(50) NOT NULL, "
            "idade INT NOT NULL, "
            "PRIMARY KEY (id)"
            ") "
        )

        # CUIDADO: ISSO LIMPA A TABELA
        cursor.execute(f"TRUNCATE TABLE {TABLE_NAME}")  # type: ignore
    connection.commit()

    # Começo a manipular dados a partir daqui

    # Inserindo um valor usando placeholder e um iterável
    with connection.cursor() as cursor:
        sql = (
            f"INSERT INTO {TABLE_NAME} "
            "(nome, idade) "
            "VALUES "
            "(%s, %s) "  # Placeholders p/ evitar injeção de SQL e melhorar a segurança
        )
        data = ("Luiz", 18)
        result = cursor.execute(sql, data)  # type: ignore
        print(sql, data)
        print(result)  # 1 value
    connection.commit()

    # Inserindo um valor usando placeholder e um dicionário
    with connection.cursor() as cursor:
        sql = (
            f"INSERT INTO {TABLE_NAME} "
            "(nome, idade) "
            "VALUES "
            "(%(name)s, %(age)s) "  # using only keys's name of dict
        )
        data2 = {  # the order doesn't matter
            "age": 37,
            "name": "Le",
        }
        result = cursor.execute(sql, data2)  # type: ignore
        print(sql)
        print(data2)
        print(result)  # 1 value
    connection.commit()

    # Inserindo vários valores usando placeholder e um tupla de dicionários
    with connection.cursor() as cursor:
        sql = (
            f"INSERT INTO {TABLE_NAME} "
            "(nome, idade) "
            "VALUES "
            "(%(name)s, %(age)s) "
        )
        data3 = (
            {
                "name": "Sah",
                "age": 33,
            },
            {
                "name": "Júlia",
                "age": 74,
            },
            {
                "name": "Rose",
                "age": 53,
            },
        )
        result = cursor.executemany(sql, data3)  # type: ignore
        # print(sql)
        # print(data3)
        # print(result) # 3 values
    connection.commit()

    # Inserindo vários valores usando placeholder e um tupla de tuplas
    with connection.cursor() as cursor:
        sql = f"INSERT INTO {TABLE_NAME} " "(nome, idade) " "VALUES " "(%s, %s) "
        data4 = (
            (
                "Siri",
                22,
            ),
            (
                "Helena",
                15,
            ),
        )
        result = cursor.executemany(sql, data4)  # type: ignore
        print(sql)
        print(data4)
        print(result)  # 2 values
    connection.commit()

    # Lendo os valores com SELECT
    with connection.cursor() as cursor:
        # menor_id = int(input('Digite o menor id: '))
        # maior_id = int(input('Digite o maior id: '))
        menor_id = 2
        maior_id = 4

        sql = f"SELECT * FROM {TABLE_NAME} " "WHERE id BETWEEN %s AND %s  "

        cursor.execute(sql, (menor_id, maior_id))  # type: ignore
        # print(cursor.mogrify(sql, (menor_id, maior_id)))  # leitura no terminal
        data5 = cursor.fetchall()  # type: ignore

        # for row in data5:
        #     print(row)

    # Apagando com DELETE, WHERE e placeholders no PyMySQL
    with connection.cursor() as cursor:
        sql = f"DELETE FROM {TABLE_NAME} " "WHERE id = %s"
        # print(cursor.execute(sql, (1,)))  # 1
        connection.commit()

        cursor.execute(f"SELECT * FROM {TABLE_NAME} ")  # type: ignore

        # for row in cursor.fetchall():  # type: ignore
        #     print(row)

    # Editando com UPDATE, WHERE e placeholders no PyMySQL
    with connection.cursor() as cursor:
        sql = f"UPDATE {TABLE_NAME} " "SET nome=%s, idade=%s " "WHERE id=%s"
        cursor.execute(sql, ("Eleonor", 102, 4))  # type: ignore
        cursor.execute(f"SELECT * FROM {TABLE_NAME} ")  # type: ignore

        # for row in cursor.fetchall():
        # criando variáveis aos valores
        #     _id, name, age = row.keys() # selecionando as chaves
        #     print(_id, name, age)
        #     _id, name, age = row.items() # selecionando os itens
        #     print(_id, name, age)
        #     _id, name, age = row.values() # selecionando os valores
        #     print(_id, name, age)

        for row in cursor.fetchall():  # type: ignore
            print(row)  # printa um dict
    connection.commit()  # commitando no final
