"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

seu_nome = input('Digite seu nome: ')
sua_idade = input('Digite sua idade: ')

if seu_nome and sua_idade:
    print(f'Seu nome é {seu_nome}')
    print(f'Seu nome invertido é {seu_nome[::-1]}')
    if " " in seu_nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')

    print(f'Seu nome tem {len(seu_nome)} letras')
    print(f'A primeira letra do seu nome é {seu_nome[0]}')
    print(f'A última letra do seu nome é {seu_nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios.')
        