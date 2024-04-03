import random
NumerosAleatorios = []
for x in range(1,10 + 1):
    numero_random = random.randint(1,10)
    cuadrado = numero_random ** 2
    cubo = numero_random ** 3 
    NumerosAleatorios.append(f"el numero random es {numero_random}")
    NumerosAleatorios.append(f"el cuadrado de este numero es {cuadrado}")
    NumerosAleatorios.append(f"el cubo de este numero es {cubo}")

for elemnt in NumerosAleatorios:
    print(elemnt) 