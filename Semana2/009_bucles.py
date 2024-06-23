# el programa contiene un numero secreto que el usuario debe adivinar 
# tendra 3 oportunidades
numero_secreto = 9
adivinado=False
intentos=0
quedan=3

while not(adivinado) and (intentos<3):
        dato = int(input("Adivina el numero (Es menor que 10) : "))
        if(dato == numero_secreto): #si lo adivino
                print("Felicitaciones has adivinado el numero.. ")
                adivinado=True
        else: #si no lo adivino
            intentos+=1
            if(intentos==3):#si ya llego a los 3 intentos
                print("Juego Terminado ..")
            else:
                print("Por favor intentalo de nuevo")
                quedan-=1 #2,1
                print(f"Te quedan {quedan} intentos")
            
#Evaluación en el bucle while:
#La condición del bucle es while not(adivinado) and (intentos < 3):.
#Al inicio, adivinado es False.
#Por lo tanto, not(adivinado) será not(False), lo que se evalúa como True.
#Si intentos es menor que 3, (intentos < 3) también será True.
#Entonces, la condición completa not(adivinado) and (intentos < 3) será True and True, lo que resulta en True, y el bucle se ejecuta.