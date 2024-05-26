"""
https://docs.python.org/pt-br/3/library/stdtypes.html
https://docs.python.org/3/library/pathlib.html
Imutáveis que vimos até agora: str, int, float, bool
"""
variavel = '6Luiz Otavio'
outra_variavel = f'{variavel[:3]}ABC{variavel[4:]}'
print(variavel)
print(outra_variavel)
print(variavel.capitalize()) #esse método faz apenas o primeiro índice maiúsculo e o resto minúsculo.
print(variavel.zfill(13)) #esse método preenche de 0 a parte esquerda,  
#obrigatório preencher o nº de caracters total, se não preencher, ele dará erro,
#nº de caracters precisa ser maior do que o objeto, se for menor, nada acontecerá.
