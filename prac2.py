#creado por Lizbeth Quenta Legua

class EcuacionLineal:
    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def tieneSolucion(self):
        determinante = (self.a * self.d - self.b * self.c)
        if determinante != 0:
            return True
        else:
            return False

    def getX(self):
        if self.tieneSolucion() == True:
            determinante = (self.a * self.d - self.b * self.c)
            x = (self.e * self.d - self.b * self.f) / determinante
            return x
        else:
            return None

    def getY(self):
        if self.tieneSolucion() == True:
            determinante = (self.a * self.d - self.b * self.c)
            y = (self.a * self.f - self.e * self.c) / determinante
            return y
        else:
            return None
print("ingrese los valores que se le pida")

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
d = float(input("d: "))
e = float(input("e: "))
f = float(input("f: "))

ecuacion = EcuacionLineal(a, b, c, d, e, f)
if ecuacion.tieneSolucion() == True:
    x = ecuacion.getX()
    y = ecuacion.getY()
    print("x =", x, ", y =", y)
else:
    print("La ecuación no tiene solución")