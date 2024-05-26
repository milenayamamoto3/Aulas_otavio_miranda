# Os 4 pilares da Programação Orientada a Objetos
# Encapsulamento, Herança, Abstração e Polimorfismo

#Abstração
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'
# print(LOG_FILE)

class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log')
    
    def log_error(self,msg):
        return self._log(f'Error:{msg}')

    def log_sucess(self,msg):
        return self._log(f'Sucess:{msg}')

class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        print('Salvando no log:', msg_formatada)
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})') 
        # print(msg) # aqui retorna "Error:qualquer coisa"

if __name__ == '__main__': #main é este módulo
    # l = Log() 
    
    lp = LogPrintMixin()
    lp.log_error('qualquer coisa')
    lp.log_sucess('Que legal!')

    lf = LogFileMixin()
    lf.log_error('qualquer coisa')
    lf.log_sucess('Que legal!')

    