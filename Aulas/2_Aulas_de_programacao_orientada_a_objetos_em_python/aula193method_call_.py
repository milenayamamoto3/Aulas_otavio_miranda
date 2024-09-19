class Callme:
    def __init__(self, phone):
        self.phone = phone
    def __call__(self, nome):
        print(f'{nome} está ligando {self.phone}')
        return 123 #só será impresso se chmar o "print"

call1 = Callme('3456') #3456 -> objeto da classe
retorno = call1('Milena') #Milena -> objeto do método "call"
print(retorno)