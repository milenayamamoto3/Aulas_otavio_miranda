"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[4]) #pega o índice 4
print(variavel[0:4]) #pega a partir do primeiro até o índice 3
print(variavel[:4]) #pega a partir do primeiro (omitido) até o índice 3
print(variavel[4:]) #pega do índice 4 até o último (omitido)
print(variavel[2:5]) #pega do índice 2 até o índide 4
print(variavel[:-1]) #pega a partir do primeiro até o índice-2
print(variavel[:]) #pega do início ao fim
print(len(variavel)) #quantidade de caracteres
print(variavel[0:len(variavel):1]) #a saída vai trazer igual a variável, pois vai pegar 1 por 1
print(variavel[0:9:2]) #a saída vai trazer "Oámno", pois vai pegar 2 em 2
print(variavel[::-1]) #pega o final para iniciar até o início para finalizar(omitido) com -1 pegando 1 por 1 recuando-> odnum álO (inverte)
print(variavel[0:9:-1]) #não exibirá nada, pois como ele está recuando com -1, é como se pegasse 1 por 1 fora da str
print(variavel[-1:-10:-1]) #pega o final para iniciar até o início para finalizar com -1 pegando 1 por 1 recuando -> odnum álO (inverte)
print(variavel[-1:-10:-2]) #pega o final para iniciar até o início para finalizar com -2 pegando 2 por 2 recuando
print(variavel[::]) #Olá mundo