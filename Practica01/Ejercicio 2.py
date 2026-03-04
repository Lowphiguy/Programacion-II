# Acho Lugarani Emanuel Adrian
# Álgebra
class EcuacionLineal:
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    def tieneSolucion(self):
        return (self.__a * self.__d - self.__b * self.__c) != 0

    def getX(self):
        determinante = self.__a * self.__d - self.__b * self.__c
        return (self.__e * self.__d - self.__b * self.__f) / determinante

    def getY(self):
        determinante = self.__a * self.__d - self.__b * self.__c
        return (self.__a * self.__f - self.__e * self.__c) / determinante


# Programa de prueba

datos = input("Ingrese a, b, c, d, e, f: ").split()

a = float(datos[0])
b = float(datos[1])
c = float(datos[2])
d = float(datos[3])
e = float(datos[4])
f = float(datos[5])

ecuacion = EcuacionLineal(a, b, c, d, e, f)

if ecuacion.tieneSolucion():
    print("x =", ecuacion.getX(), ", y =", ecuacion.getY())
else:
    print("La ecuacion no tiene solucion")