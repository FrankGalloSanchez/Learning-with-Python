matriz = [[1, 2, 3],
          [1, 2, 3],
          [1, 2, 3]]

elemento = matriz[1][2]
print("El elemento que está en la fila 1 columna 2 es:", elemento)

for fila in matriz:
    for elemento in fila:
        print(elemento, end=' ')
    print()  # Imprime una nueva línea después de cada fila
