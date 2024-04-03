import random

numeros = [[],
           [],
           []]

def NumeroRandom():
    return random.randint(0, 700)

for fila in numeros:
    for _ in range(3):  
        fila.append(NumeroRandom())

for fila in numeros:
    for columna in fila:
        print(columna, end=" ")
    print()

def Validar_Columnas(numeros):
    for col in range(3):
        if all(fila[col] == numeros[0][col] and numeros[0][col] != 0 for fila in numeros):
            return True

num_cols = 3  
if Validar_Columnas(numeros):
    print("¡Hay una columna válida!")
else:
    print("No hay columnas válidas.")

