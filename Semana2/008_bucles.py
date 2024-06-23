#el programa pedira numero y los ira sumando en una varibale que
#que tecnicamente se conoce como acumulaodr
suma = 0
numero = 1

while numero !=0: #Mientras numero no sea igual a cero
    numero = int(input("Ingresa un numero para sumarlo , (ingresa 0 para salir) :"))
    suma+=numero #suma=suma+numero

print("la suma de los numeros introducidos es : ",suma)