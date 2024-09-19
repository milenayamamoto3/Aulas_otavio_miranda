"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade_carro = 103 # velocidade atual do carro (km/h)
local_carro = 99  # local em que o carro está na estrada (km)

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # faixa onde o radar pega

if velocidade_carro > RADAR_1 and \
   local_carro >= (LOCAL_1 - RADAR_RANGE) and \
   local_carro <= (LOCAL_1 + RADAR_RANGE): 
    print('Ultrapassou o radar dentro do local - multado')

if velocidade_carro <= RADAR_1 and \
   local_carro >= (LOCAL_1 - RADAR_RANGE) and \
   local_carro <= (LOCAL_1 + RADAR_RANGE):
    print('Passou no local mas não foi multado')

if not \
   (local_carro >= (LOCAL_1 - RADAR_RANGE) and \
   local_carro <= (LOCAL_1 + RADAR_RANGE)):
    print('O carro está fora do local')
