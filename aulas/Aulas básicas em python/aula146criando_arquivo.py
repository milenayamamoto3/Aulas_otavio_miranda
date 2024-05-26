# Criando arquivos com Python + Context Manager with
# with open (context manager) e métodos úteis do TextIOWrapper(type(arquivo))
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo

# Leia também: https://www.otaviomiranda.com.br/2020/normalizacao-unicode-em-python/

caminho_arquivo = 'C:\\Users\\acerc\\OneDrive\\Área de Trabalho\\Aulas Python\\aulas'
caminho_arquivo += 'aula146.txt'

# arquivo = open(caminho_arquivo, 'w')
# #
# arquivo.close()

with open(caminho_arquivo, 'w+', encoding='utf8') as arquivo: #abre um novo arquivo para escrever e +
    print(type(arquivo)) #tipo de arquivo
    arquivo.write('Atenção\n') #cedilha e tio precisa "encoding='utf8'"
    arquivo.write('Linha 1\n') #escrevendo uma linha
    arquivo.write('Linha 2\n')
    arquivo.writelines(        #escrevendo várias linhas
        ('Linha 3\n', 'Linha 4\n') 
    )
    arquivo.seek(0, 0) #volta o cursor para cima
    print(arquivo.read()) #lendo o arquivo todo
    print('Lendo')     #esse print só sai aqui
    arquivo.seek(0, 0)
    print(arquivo.readline(), end='') # ler uma linha apenas, igual "next"(interator), 
    print(arquivo.readline().strip()) # end e strip para não pular pra outra linha
    print(arquivo.readline().strip()) # excluindo o "\n" que o cursor faz automat.

    print('READLINES')
    arquivo.seek(0, 0)
    for linha in arquivo.readlines():#todas as linhas
        print(linha.strip())

print('#' * 10) #print fora do with

with open(caminho_arquivo, 'r') as arquivo: # abre o arquivo para ler
    print(arquivo.read())

# os dois métodos excluem o arquivo
# os.remove(caminho_arquivo)
# os.unlink(caminho_arquivo)

# método de mover e renomear o arquivo
# os.rename(caminho_arquivo, "aula1462.txt") -> primeiro parâmetro é o caminho
#e o segundo o novo nome.