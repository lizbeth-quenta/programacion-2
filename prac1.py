#creado por Lizbeth Quenta Legua

import time     # para que mida en tiempo real
import random   # para que genere numeros aleatorios 


class Cronometro:

    def __init__(self):
        self.__inicia = time.time()
        self.__finaliza = 0

    def getInicia(self):
        return self.__inicia

    def getFinaliza(self):
        return self.__finaliza

    def inicia(self):
        self.__inicia = time.time()

    def detener(self):
        self.__finaliza = time.time()

    def lapsoDeTiempo(self):
        return (self.__finaliza - self.__inicia) * 1000


def ordenacionSeleccion(lista):
    n = len(lista)
    for i in range(n):
        minimo = i
        for j in range(i + 1, n):
            if lista[j] < lista[minimo]:
                minimo = j
        lista[i], lista[minimo] = lista[minimo], lista[i]


numeros = []

for i in range(10000):  # <-- aquí reducimos de 100,000 a 10,000
    numeros.append(random.randint(1, 100000))

print("Primeros 20 números generados:") # solo imprimimos los primeros 20 num. para que no se sature la pantalla
for i in range(20):
    print(numeros[i])

cron = Cronometro()

print("Iniciando ordenación...")

cron.inicia()
ordenacionSeleccion(numeros)
cron.detener()

print("Ordenación terminada.")

print("Primeros 20 números ya ordenados:")
for i in range(20):
    print(numeros[i])

print("Tiempo en milisegundos:", cron.lapsoDeTiempo())
print("Tiempo en segundos:", cron.lapsoDeTiempo() / 1000)
print("esta ejecucucion es de 10000 datos por q python tarda al hacer correr de ora camtidad pero en  ")