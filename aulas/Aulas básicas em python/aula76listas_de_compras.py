"""
Faça uma lista de compras com listas.
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista.
Não permita que o programa quebre com 
erros 
"""
import os

lista = []

while True:
    print("Escolha uma opção")
    opcao = input('[i]nserir [a]pagar [l]istar: ')
   
    if opcao == 'i':
        os.system('cls')
        valor = input('Qual valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input('Qual índice que deseja apagar? ')

        try:
            indice = int(indice_str) 
            del lista[indice]

        except ValueError:
            print('Por favor, digite número inteiro')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')

    elif opcao == 'l': 
        os.system('cls')
        if len(lista) == 0:
            print('Não há nada para listar')
        for i, valor in enumerate(lista):
            print(i, valor)

    else: 
        print('Por favor, escolha "i", "a" ou "l".')