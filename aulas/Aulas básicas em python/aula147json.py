# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load = Carrega o json para o python
import json

pessoa = {
    'nome': 'Luiz Otávio 2',
    'sobrenome': 'Miranda',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

caminho_arquivo1 = 'C:\\Users\\acerc\\OneDrive\\Área de Trabalho\\Aulas Python\\aulas'
caminho_arquivo1 += 'aula147.json'

with open(caminho_arquivo1, 'w', encoding='utf8') as arquivo1:
    json.dump(pessoa,              #método escreve dados em formato JSON
              arquivo1,            #(JavaScript Object Notation) para arquivo json
              ensure_ascii=False,  #para os str se manter 
              indent=2,            #para a estrutura se manter no arquivo criado
    ) 
                                
with open(caminho_arquivo1, 'r', encoding='utf8') as arquivo1:
    pessoa = json.load(arquivo1)
    # print(pessoa) #a tupla que era antes virou lista! Cuidado!
    # print(type(pessoa)) #dict
    print(pessoa['nome']) #retorna o valor da chave "nome"