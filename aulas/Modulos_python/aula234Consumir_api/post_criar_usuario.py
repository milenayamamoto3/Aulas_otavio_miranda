import requests
from pprint import pprint

url = "http://127.0.0.1:3001/users"

user_data = {"nome": "Luiz Otávio", "password": "123456", "email": "luiz@email.com"}

response = requests.post(url=url, json=user_data)

if response.status_code >= 200 and response.status_code <= 299:
    # Sucesso
    print("Status:", response.status_code)
    print("Reason:", response.reason)
    print("Text:", response.text)
    print("JSON:", response.json())
    # print('Bytes:', response.content)
else:
    # Erros
    print("Status:", response.status_code)
    print("Reason:", response.reason)
    print("Text:", response.text)
    # print('Bytes', response.content)
