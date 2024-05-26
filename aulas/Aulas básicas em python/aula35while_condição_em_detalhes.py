"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
contador = 0

while contador <= 10:
    contador = contador + 1
    print(contador) #vai de 1 até 11

while contador <= 10: #Durante a execusão do código, esse código(<-) não vai entrar, pois a 
    print(contador) #variável vai ter valor 11.
    contador = contador + 1 #vai de 0 até 10

print('Acabou')