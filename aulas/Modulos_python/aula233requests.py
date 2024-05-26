# requests para requisições HTTP
# Tutorial -> https://youtu.be/Qd8JT0bnJGs
import requests

# http:// -> 80
# https:// -> 443
url = "http://localhost:8000/"
response = requests.get(url)

# print(response) #da a resposta do servidor
print(response.status_code)  # da apenas a resposta código de status HTTP
# print(response.headers) # informações
# print(response.content) #conteúdo em bytes
# print(response.json())  # quando seu API vier em json, consegue responder
# print(response.text)  # html
