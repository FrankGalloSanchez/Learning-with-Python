#Genera una lista en rango de 10 pero detenlo en cuando llegue 6
for i in range(1,10):
    if i==6:
        print("Saliendo del sistema ...")
        break #No llegara al 10 sino se corta en 6
    print("La variable i ,tiene el valor de :",i)