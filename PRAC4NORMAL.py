#creado por Lizbeth Quenta Legua
# ejercicio 4 estructurada
import math

def promedio(lista):
    suma = 0
    for num in lista:
        suma = suma + num
    return suma / len(lista)

def desviacion(lista):
    prom = promedio(lista)
    suma_cuadrados = 0
    n = len(lista)
    for num in lista:
        suma_cuadrados = suma_cuadrados + (num - prom) ** 2
    desviacion = math.sqrt(suma_cuadrados / (n - 1))
    return desviacion

print("Vamos a calcular el promedio y la desviación estándar de 10 números.")

numeros = []

for i in range(10):
    valor = float(input("Número " + str(i+1) + ": "))
    numeros.append(valor)

print("El promedio es:", promedio(numeros))
print("La desviación estándar es:", desviacion(numeros))
