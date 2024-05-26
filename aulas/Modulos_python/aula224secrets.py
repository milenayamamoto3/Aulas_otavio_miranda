# secrets gera números aleatórios seguros
import secrets
import string as s
from secrets import SystemRandom as Sr

print(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=12)) #retorna uma lista
print(''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=12))) #tira a list

# comando pronto para senha aleatória de 12 caracters para o terminal
# python -c "import string as s;from secrets import SystemRandom as Sr; print(''.join(Sr().choices(s.ascii_letters + s.punctuation + s.digits,k=12)))"

# print(secrets.randbelow(100)) #pega um nº aleatório de 0 a 99
# print(secrets.choice([10, 11, 12])) #pega um nº aleatório nesta list

random = secrets.SystemRandom()
"""
secrets.SystemRandom não é a mesma coisa que importar o módulo random.
secrets.SystemRandom é uma classe dentro do módulo secrets do Python que 
fornece funcionalidades para gerar números aleatórios de forma segura,
utilizando o gerador de números aleatórios do sistema operacional. 
Esta classe é útil quando você precisa de números aleatórios para propósitos 
criptográficos ou de segurança.
"""
random.seed(10) #seed não tem mais funcionalidade

# o exemplo abaixo funciona independente do seed
r_range = random.randrange(10, 20, 2)
print(r_range)



