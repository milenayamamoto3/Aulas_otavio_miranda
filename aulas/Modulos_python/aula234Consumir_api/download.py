import requests

url = "https://images.creativefabrica.com/products/previews/2023/08/25/9X2NldtE4/2UTyMBQuEE2whnoF29YyXyNAFOQ-desktop.jpg"
nome_arquivo = url.split("/")[-1]

response = requests.get(url)

if response.status_code >= 200 and response.status_code <= 299:
    # Sucesso
    print(response.status_code)
    print(response.reason)

    with open(nome_arquivo, "wb") as file:  # "write binary" (escrever binário)
        file.write(response.content)
else:
    # Erros
    print(response.status_code)
    print(response.reason)
