import sys
import time

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QObject, QThread, Signal
from workerui import Ui_myWidget


class Worker1(QObject):
    started = Signal(str)  # str por causa do labels
    progressed = Signal(str)
    finished = Signal(str)

    def run1(self):
        value = "0"
        self.started.emit(value)
        for i in range(5):
            value = str(i)
            self.progressed.emit(value)
            time.sleep(1)
        self.finished.emit(value)


class Worker2(QObject):
    started = Signal(str)  # str por causa do labels
    progressed = Signal(str)
    finished = Signal(str)

    def run2(self):
        value = "0"
        self.started.emit(value)
        for i in range(50, 100, 5):
            value = str(i)
            self.progressed.emit(value)
            time.sleep(0.3)
        self.finished.emit(value)


class MyWidget(QWidget, Ui_myWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.button1.clicked.connect(self.hardWork1)
        self.button2.clicked.connect(self.hardWork2)

    def hardWork1(self):
        # self.label1.setText('1 iniciado') # não da tempo disso ser exec
        # time.sleep(5) # isso executa ao mesmo tempo do de cima

        # for i in range(5):
        #     print(i)
        #     time.sleep(1) # para cada i passa 1 segundo
        # self.label1.setText("1 terminado")

        self._worker1 = Worker1()
        self._thread1 = QThread()
        # Isso garante que o widget vai ter uma referência para worker e thread
        worker = self._worker1
        thread = self._thread1

        # Worker é movido para a thread. Todas as funções e métodos do
        # objeto de worker serão executados na thread criado pela QThread.
        worker.moveToThread(thread)

        # Quando uma QThread é iniciada, emite o sinal started automaticamente.
        thread.started.connect(worker.run1)
        # O sinal finished é emitido pelo objeto worker quando o trabalho que
        # ele está executando é concluído. Isso aciona o método quit da qthread
        # que interrompe o loop de eventos dela.
        worker.finished.connect(thread.quit)

        # deleteLater solicita a exclusão do objeto worker do sistema de
        # gerenciamento de memória do Python. Quando o worker finaliza, ele
        # emite um sinal finished que vai executar o método deleteLater.
        # Isso garante que objetos sejam removidos da memória corretamente.
        thread.finished.connect(thread.deleteLater)
        worker.finished.connect(worker.deleteLater)

        # Aqui estão seus métodos e início, meio e fim
        # execute o que quiser
        worker.started.connect(self.worker1Started)
        worker.progressed.connect(self.worker1Progressed)
        worker.finished.connect(self.worker1Finished)

        # Inicie a thread
        thread.start()

    def worker1Started(self, value):
        self.button1.setDisabled(True)  # desativou o button para nao ser clicado de nv
        self.label1.setText(value)
        print("worker 1 iniciado", value)

    def worker1Progressed(self, value):
        self.label1.setText(value)
        print("worker 1 em progresso", value)

    def worker1Finished(self, value):
        self.label1.setText(value)
        self.button1.setDisabled(False)  # ativou o button para nao ser clicado de nv
        print("worker 1 finalizado", value)

    ######################################################################

    def hardWork2(self):
        # for i in range(5):
        #     print(i)
        #     time.sleep(i) # para cada i é acumulativo,
        # i=0 -> 0s, i=1 -> 1s, -> i=2 -> 2s, i=3 -> 3s...
        # self.label2.setText("2 terminado")

        self._worker2 = Worker2()
        self._thread2 = QThread()

        worker = self._worker2
        thread = self._thread2

        # Mover o worker para a thread
        worker.moveToThread(thread)

        # Run
        thread.started.connect(worker.run2)
        worker.finished.connect(thread.quit)

        thread.finished.connect(thread.deleteLater)
        worker.finished.connect(worker.deleteLater)

        worker.started.connect(self.worker2Started)
        worker.progressed.connect(self.worker2Progressed)
        worker.finished.connect(self.worker2Finished)

        thread.start()

    def worker2Started(self, value):
        self.button2.setDisabled(True)
        self.label2.setText(value)
        print("worker 2 iniciado", value)

    def worker2Progressed(self, value):
        self.label2.setText(value)
        print("worker 2 em progresso", value)

    def worker2Finished(self, value):
        self.label2.setText(value)
        self.button2.setDisabled(False)
        print("worker 2 finalizado", value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWidget = MyWidget()
    myWidget.show()
    app.exec()
