# Threads - Executando processamentos em paralelo
from threading import Thread
from time import sleep

# Exemplo 1
"""
class MeuThread(Thread):
    def __init__(self, texto: str, tempo: int):
        self.texto = texto
        self.tempo = tempo  # int em segundos

        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)


t1 = MeuThread("Thread 1", 5)
t1.start()

t2 = MeuThread("Thread 2", 3)
t2.start()

t3 = MeuThread("Thread 3", 2)
t3.start()

for i in range(20):  # 0->19
    print(i)
    sleep(1)
"""

# Exemplo 2
"""
def vai_demorar(texto: str, tempo: int):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar, args=('Olá mundo 1!', 5))
t1.start()

t2 = Thread(target=vai_demorar, args=('Olá mundo 2!', 1))
t2.start()

t3 = Thread(target=vai_demorar, args=('Olá mundo 3!', 2))
t3.start()

for i in range(20):
    print(i)
    sleep(.5)
"""

# Exemplo 3


def vai_demorar(texto: str, tempo: int):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar, args=("Olá mundo 1!", 10))
t1.start()
t1.join()  # da uma segurada até o sleep do "t1.start()"" terminar

# while t1.is_alive():  # is_alive -> enquanto estiver viva
#     print("Esperando a Thread")
#     sleep(2)

print("Thread acabou")
