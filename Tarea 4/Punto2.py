#///////////////////////CICLO WHILE///////////////////////////////
print("Bienvenido a continuacion digitira 10 numeros y le dire el promedio de los numeros")
contador = 1
promedio_suma = 0
while contador <= 10:
    numero = int(input("Digite el numero "))
    promedio_suma += numero  
    contador += 1
    print(f" el numero es {numero} y el promedio es {promedio_suma}")
promedio_Final = promedio_suma / 10 
print(f"el numero en promedio fue {promedio_suma} El promedio de los numeros es de {promedio_Final}")

#/////////////////////CICLO FOR/////////////////////////////////

promedio_suma = 0
for x in range(1,11,1):
    numero = int(input("Digite el numero "))
    promedio_suma += numero
    print(f" el numero es {numero} y el promedio es {promedio_suma}")
promedio_final = promedio_suma/10
print(f"el numero en promedio fue {promedio_suma} El promedio de los numeros es de {promedio_final}")