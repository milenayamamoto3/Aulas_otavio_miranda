# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()

# datetime.fromtimestamp(Unix Timestamp)
# https://pt.wikipedia.org/wiki/Era_Unix
# documento sobre o datetime com os formatos
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

# Instalando o pytz (python -m pip install pytz types-pytz) no terminal com ambiente 
# virtual ativo

from datetime import datetime
# from pytz import timezone # type: ignore

# data_str_data = '2022-04-20 07:49:23'
# data_str_fmt = '%Y-%m-%d %H:%M:%S'

# data = datetime(2022, 4, 20, 7, 49, 23)
# data = datetime.strptime(data_str_data, data_str_fmt)
# data = datetime.now(timezone('America/Sao_Paulo'))
# data = datetime(2022, 4, 20, 7, 49, 23, tzinfo=timezone('Asia/Tokyo'))
data = datetime.now() #para saber a data e hora de agora

# print(data)
print(data.timestamp()) #saber os segundos a partir do 01/01/70(está na base de dados)
print(data.fromtimestamp(1712144181))  # esses segundos, te dará a data e hora exata