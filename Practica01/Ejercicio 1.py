# Acho Lugarani Emanuel Adrian
# Cronómetro
import time
import random


class Cronometro:
    def __init__(self):
        self.__inicia = time.time() * 1000
        self.__finaliza = 0

    def getInicia(self):
        return self.__inicia

    def getFinaliza(self):
        return self.__finaliza

    def inicia(self):
        self.__inicia = time.time() * 1000

    def detener(self):
        self.__finaliza = time.time() * 1000

    def lapsoDeTiempo(self):
        return self.__finaliza - self.__inicia


# Programa de prueba

numeros = []
i = 0
while i < 10000:
    numeros.append(random.randint(1, 100000))
    i += 1

cron = Cronometro()

cron.inicia()

# Ordenación por selección
n = len(numeros)
i = 0
while i < n - 1:
    minimo = i
    j = i + 1
    while j < n:
        if numeros[j] < numeros[minimo]:
            minimo = j
        j += 1

    aux = numeros[i]
    numeros[i] = numeros[minimo]
    numeros[minimo] = aux

    i += 1


cron.detener()

print("Tiempo de ejecución en milisegundos:", cron.lapsoDeTiempo())