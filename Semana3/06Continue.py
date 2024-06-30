#ejemplificaremos el uso de continue
#el programa solamente imprimira el valor de las variables cuando
#sean impares
for i in range(1,10):
    if i%2==0:
        print("Impresion omitida por el numero par .. ")
        continue
    print(f"la variable i , actualmente vale:{i}")