import random

print("Bienvenido este sistema hara 10 numeros al azar y le mostra del menor al mayor ")
numeros=[]
for x in range(1,10 + 1):
    numero_Random = random.randint(1,100)
    numeros.append(numero_Random)
print("Los numeros random son ")    
for j in numeros:
    print(j)    
numeros.sort()
print("Los numeros de menor a mayor ")
for j in numeros:
    print(j)