# Positional-Only Parameters (/) e Keyword-Only Arguments (*)
# *args (ilimitado de argumentos posicionais)
# **kwargs (ilimitado de argumentos nomeados)
# 🟢 Positional-only Parameters (/) - Tudo antes da barra deve
# ser ❗️APENAS❗️ posicional.
# Antes da barra não pode nomear os argumentos
# PEP 570 – Python Positional-Only Parameters
# https://peps.python.org/pep-0570/
# 🟢 Keyword-Only Arguments (*) - * sozinho ❗️NÃO SUGA❗️ valores.
# PEP 3102 – Keyword-Only Arguments
# https://peps.python.org/pep-3102/
def soma(a, b, /, *, c, **kwargs):  #antes do asterisco deve ter apenas argumentos 
                                    #posicionais e pode ter arg nomeados
    print(kwargs)#retorna dict      #depois do asterisco deve ter apenas argumentos nomeados
    print(a + b + c)

soma(1, 2, c=3, nome='teste')


def diminuir(a, b, *args):

    print(args) #retorna uma tupla
    print(a-b) #1
    
diminuir(5, 4, 'qualquer', 'coisa')