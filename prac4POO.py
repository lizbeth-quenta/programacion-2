#creado por Lizbeth Quenta Legua
# ejercicio 4 en poo
import math

class Estadistica:
    def __init__(self, datos):
        self.datos = datos

    def promedio(self):
        suma = 0
        for numero in self.datos:
            suma = suma + numero
        promedio = suma / len(self.datos)
        return promedio

    def desviacion(self):
        prom = self.promedio()
        suma_cuadrados = 0
        n = len(self.datos)
        for numero in self.datos:
            suma_cuadrados = suma_cuadrados + (numero - prom) ** 2
        desviacion = math.sqrt(suma_cuadrados / (n - 1))
        return desviacion

print("Vamos a calcular el promedio y la desviación estándar de 10 números.")
numeros = []

for i in range(10):
    valor = float(input("Número " + str(i+1) + ": "))
    numeros.append(valor)

estadistica = Estadistica(numeros)

print("El promedio es", estadistica.promedio())
print("La desviación standard es", estadistica.desviacion())
