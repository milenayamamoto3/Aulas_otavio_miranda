#o __init__.py (arquivo padrão de inicialização) modulariza o package (teste)
import teste  #importa só o package, que tudo que está no __init__.py consegue usar aqi
print(teste.variavel) #pegando 
#diretamente a variável de outro módulo que foi importado para o __init__.py