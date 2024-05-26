#exercício de maior número e o menor dentro de 3 números digitados pelo usuário
try:
    a = int(input('Digite um número inteiro: '))
    b = int(input('Digite outro número inteiro: '))
    c = int(input('Digite outro número inteiro: '))
    if a < b < c:
        print(f'{c} é o maior e {a} o menor')
    elif b < c < a:
        print(f'{a} é o maior e {b} o menor')
    elif c < a < b:
        print(f'{b} é o maior e {c} o menor')
    elif a < c < b:
        print(f'{b} é o maior e {a} o menor')
    elif b < a < c:
        print(f'{c} é o maior e {b} o menor')
    elif c < b < a:
        print(f'{a} é o maior e {c} o menor')
    else:
        print('Não digite números iguais')
except:
    print('Digite um número inteiro')

