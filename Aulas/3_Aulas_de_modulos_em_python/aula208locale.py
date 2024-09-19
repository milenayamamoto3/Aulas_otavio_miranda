# locale para internacionalização (tradução)
# https://docs.python.org/3/library/locale.html
# https://learn.microsoft.com/fr-fr/powershell/module/international/get-winsystemlocale?view=windowsserver2022-ps&viewFallbackFrom=win10-ps
# Get-WinSystemLocale -> no terminal, executando sairá o locale do seu windowns (SO)
import calendar
import locale

locale.setlocale(locale.LC_ALL, '') #usando o locale padrão do meu sistema operacional
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8') #usando o português do BR especificando
         #o "utf8" 
print(locale.getlocale()) #imprime o locale

print(calendar.calendar(2022))