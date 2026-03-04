# Acho Lugarani Emanuel Adrian
# Estadísticas

#Programación Modular
import math

def promedio(valores):
    suma = 0
    i = 0
    while i < len(valores):
        suma += valores[i]
        i += 1
    return suma / len(valores)

def desviacion(valores):
    prom = promedio(valores)
    suma = 0
    i = 0
    while i < len(valores):
        suma += (valores[i] - prom) ** 2
        i += 1
    return math.sqrt(suma / (len(valores) - 1))


# main

datos = input("Ingrese 10 numeros: ").split()

numeros = []
i = 0
while i < len(datos):
    numeros.append(float(datos[i]))
    i += 1

print("El promedio es", round(promedio(numeros), 2))
print("La desviacion estandar es", round(desviacion(numeros), 5))

# Programación Orientada a Objetos
import math

class Estadistica:
    def __init__(self, valores):
        self.__valores = valores

    def promedio(self):
        suma = 0
        i = 0
        while i < len(self.__valores):
            suma += self.__valores[i]
            i += 1
        return suma / len(self.__valores)

    def desviacion(self):
        prom = self.promedio()
        suma = 0
        i = 0
        while i < len(self.__valores):
            suma += (self.__valores[i] - prom) ** 2
            i += 1
        return math.sqrt(suma / (len(self.__valores) - 1))


# Programa de prueba

datos = input("Ingrese 10 numeros: ").split()

numeros = []
i = 0
while i < len(datos):
    numeros.append(float(datos[i]))
    i += 1

estad = Estadistica(numeros)

print("El promedio es", round(estad.promedio(), 2))
print("La desviacion estandar es", round(estad.desviacion(), 5))