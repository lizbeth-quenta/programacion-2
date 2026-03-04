#creado por Lizbeth Quenta Legua
# ejercicio 3
import math

class EcuacionLineal:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def getDiscriminante(self):
        return (self.__b * self.__b) - 4 * self.__a * self.__c

    def getRaiz1(self):
        d = self.getDiscriminante()
        if d > 0:
            raiz = (-self.__b + math.sqrt(d)) / (2 * self.__a)
            return raiz
        elif d == 0:
            raiz = -self.__b / (2 * self.__a)
            return raiz
        else:
            return 0

    def getRaiz2(self):
        d = self.getDiscriminante()
        if d > 0:
            raiz = (-self.__b - math.sqrt(d)) / (2 * self.__a)
            return raiz
        else:
            return 0

print("Ecuación cuadrática: ax² + bx + c = 0")
print("Ingrese los valores a, b, c:")

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

ecuacion = EcuacionLineal(a, b, c)

discriminante = ecuacion.getDiscriminante()

if discriminante > 0:
    r1 = ecuacion.getRaiz1()
    r2 = ecuacion.getRaiz2()
    print("La ecuación tiene dos raíces", r1, "y", r2)
elif discriminante == 0:
    r = ecuacion.getRaiz1()
    print("La ecuación tiene una raíz", r)
else:
    print("La ecuación no tiene raíces reales")