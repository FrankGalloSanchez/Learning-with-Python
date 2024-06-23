#simularemos el conteo regresivo del despegue del cohete
import time

contador = 5

print("Inicia el conteo regresivo ...")
while(contador>0): #mientras el contador sea mayor que 0
    print(contador)
    time.sleep(1)
    contador-=1
print("El cohete ah despegado con exito")