# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypi: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
import os
import pymysql
import dotenv

TABLE_NAME = "customers"
dotenv.load_dotenv()
connection = pymysql.connect(
    host=os.environ["MYSQL_HOST"],
    user=os.environ["MYSQL_USER"],
    password=os.environ["MYSQL_PASSWORD"],
    database=os.environ["MYSQL_DATABASE"],
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
