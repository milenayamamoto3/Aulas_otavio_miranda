#Pergunte quantos km o usuário quer correr para calcular o valor da passagem que ele pagará, 
#Sabendo que até 200km, o km vale R$ 0,50 e acima disso, R$ 0,45
def calculo_preco(distancia):
    if distancia <= 200:
        preco = distancia * 0.5
    
    else:
        preco = distancia * 0.45
    return preco

def main():
    try:
        distancia = float(input('Qunatos km deseja correr? '))
        preco = calculo_preco(distancia)
        print(f'Sua distância de {distancia:.2f} tem valor de R$ {preco:.2f}')

    except:
        print('Digite um número válido')

if __name__ == "__main__":
    main()