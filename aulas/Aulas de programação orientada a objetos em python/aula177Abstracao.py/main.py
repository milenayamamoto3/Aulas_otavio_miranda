# from log import LogPrintMixin, LogFileMixin
#from (pasta) import (classe)

# lp = LogPrintMixin()
# lp.log_error('qualquer coisa')
# lp.log_sucess('Que legal!')

# lf = LogFileMixin()
# lf.log_error('qualquer coisa')
# lf.log_sucess('Que legal!')

from eletronico import Smartphone

galaxy_s = Smartphone('Galaxy S')
iphone = Smartphone('Iphone')

galaxy_s.ligar()
iphone.desligar()

