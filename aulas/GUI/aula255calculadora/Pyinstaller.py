# Instalar o Pyinstaller
# 1 - empacotando uma aplicação depende de cada aplicação
# 2 - depende do seu SO
# 3 - qualquer erro, procure no google
# https://www.pythonguis.com/tutorials/packaging-pyside6-applications-windows-pyinstaller-installforge/
# https://pyinstaller.org/en/stable/
# python -m pip install pyinstaller
# CAMINHO da pasta mãe é:
# PS C:\Users\acerc\OneDrive\Desktop\Aulas_python\Aulas_otavio_miranda> cd .\aulas\GUI\
# PS C:\Users\acerc\OneDrive\Desktop\Aulas_python\Aulas_otavio_miranda\aulas\GUI>
# Modo padrão
# python aula255calculadora/main.py
# Modo detalhado
# pyinstaller --name="Calculadora" --noconfirm --onefile --add-data="aula255calculadora/files/;files/" --icon="aula255calculadora/files/icon.png" --noconsole --clean --log-level=WARN --distpath="aula255calculadora/dist" --workpath="aula255calculadora/build" --specpath="aula255calculadora/" aula255calculadora/main.py
# Modo que deu certo
# pyinstaller --name="Calculadora" --onefile --add-data="C:/Users/acerc/OneDrive/Desktop/Aulas_python/Aulas_otavio_miranda/aulas/GUI/aula255calculadora/files/;files/" --icon="C:/Users/acerc/OneDrive/Desktop/Aulas_python/Aulas_otavio_miranda/aulas/GUI/aula255calculadora/files/icon.png" --distpath="aula255calculadora/dist" --workpath="aula255calculadora/build" --specpath="aula255calculadora/" aula255calculadora/main.py
# noconsole - sem console
# build - empacotar
# dist - distribuição, projeto empacotado - (mac.app), (windowns.exe)
# para o arquivo png funcionar, precisa ter o pillow instalado (python -m pip install pillow)
