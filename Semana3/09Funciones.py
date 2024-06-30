#este programa calcula el area cuando le das el radio
import math

def calcular_area_circulo(radio):
    area = math.pi * radio ** 2
    return area

radio=float(input("Escribe el radio del circulo y calculare su area :"))

#llamamos a la funcion
areaCir=calcular_area_circulo(radio)

print("El valor del area es",round(areaCir,2))