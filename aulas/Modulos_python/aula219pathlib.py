# https://docs.python.org/3/library/pathlib.html
from pathlib import Path
# from shutil import rmtree

#manipulação de caminhos
#exemplo de caminho: '/Users', 'luizotavio', 'Desktop', 'PROJETO', 'SCR', 'ESTEARQUIVO'

# caminho_projeto = Path()
# print(caminho_projeto) #caminho relativo, retorna "."
# print(caminho_projeto.absolute()) #caminho até a pasta do projeto
 
# caminho_arquivo = Path(__file__)
# print(caminho_arquivo) #caminho até o atual arquivo ('ESTEARQUIVO')
# print(caminho_arquivo.parent) #caminho até a pasta mãe ('SCR')
# print(caminho_arquivo.parent.parent) #caminho até a pasta mãe da pasta mãe e assim 
# por diante ('PROJETO')

#criação de caminhos
# ideias = caminho_arquivo.parent / 'ideias'
# print(ideias / 'arquivo.txt')  

# print(Path.home() / 'Desktop') #criando o caminho "desktop" a partir da home

# arquivo = Path.home() / 'Desktop' / 'arquivo1.txt' criando caminho de um arquivo

#maneira 1 de abrir um arquivo

# arquivo.touch() #criou arquivo "arquivo1.txt"
# print(arquivo) #imprimi o caminho apenas 
# arquivo.write_text('Olá') #escreveu um texto
# arquivo.write_text('Olá de nv') #substitui o texto anterior
# print(arquivo.read_text()) #ler no terminal o que está escrito
# arquivo.unlink() #apagou arquivo "arquivo1.txt"

#maneira 2 de abrir um arquivo

# with arquivo.open('a+') as file:
#     file.write('Olá\n')
#     file.write('mundo\n')
# print(arquivo.read_text())

pasta = Path.home() / 'OneDrive' / 'Área de Trabalho' / 'NovaPasta'

#maneira 1 de abrir uma pasta

# pasta.mkdir() # cria a pasta, se executar de novo, dará erro, pois falará que a pasta
#já existe
pasta.mkdir(exist_ok=True) # Para não dá erro que a pasta já existe. Não duplica
# pasta.rmdir() # se a pasta estiver vazia, conseguirá deletar, mas caso tenha
#arquivo ou outras coisas dentro, dará erro

#Criando pastas dentro da pasta mãe

files = pasta / 'files'
files.mkdir(exist_ok=True) #files = nome do diretório

#criando arquivos dentro da pasta

for i in range(10):
    file = files / f'file{i}.txt' #file = arquivo

    if file.exists(): # Se ele existe
        file.unlink()
    else:
        file.touch() #cria ou atualiza

    with file.open('a+') as text_file:
        text_file.write('Olá, você está\n')
        text_file.write(f'no arquivo{i}')

# rmtree(pasta) #apaga a pasta mesmo tendo arquivos dentro

# descobrindo a função rmtree em detalhes:
def rmtree(root: Path, remove_root=True): #root seria a pasta mãe
    for file in root.glob('*'): #asterisco -> pega tudo no root
        if file.is_dir(): # Bool se for um diretório
            print('DIR: ',file)
            rmtree(file, False)
            file.rmdir()
        else:
            print('FILE: ',file)
            file.unlink()
    
    if remove_root:
        root.rmdir()
        
rmtree(pasta)