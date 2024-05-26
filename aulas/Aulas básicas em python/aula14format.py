a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
)

print(formato)

#nome1, nome2, e nome3 são chamados de parâmetros, ou seja, nome dado às variáveis
#quando uma função está dentro de um objeto, ela é chamada de método
#argumento é o objeto dado para uma variável
#exemplo usando índices:
#nome = "Luiz"
#idade = 23
#formato = '{1} tem {0} anos'
#print(formato.format(nome, idade))
#saída: 23 tem Luiz anos