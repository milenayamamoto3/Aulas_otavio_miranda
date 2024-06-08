import re

# REGEX -> EXPRESSÃO REGULAR
NUM_OR_DOT_REGEX = re.compile(r"^[0-9.]$")
# ^...$ -> aceita apenas 1 str
# nº de 0 a 9 OU .
# r -> raw string (string bruta/crua)
# conclusão: só aceita uma str que pode ser um nº ou .


# função para detectar números e ponto
def isNumOrDot(string: str):
    return bool(NUM_OR_DOT_REGEX.search(string))


# função para detectar "nada"
def isEmpty(string: str):
    return len(string) == 0


# função para detectar se o nº é float
def isValidNumber(string: str):
    valid = False
    try:
        float(string)
        valid = True
    except ValueError:
        valid = False
    return valid


# função para converter a str para float e se for inteiro, converte para inteiro
def converToNumber(string: str):
    number = float(string)

    if number.is_integer():
        number = int(number)

    return number
