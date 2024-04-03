#////////////////////////////////CICLO WHILE///////////////////

print("Bienvenido usuario digite cuantos datos va a procesar")
contador = 1
Cantidad_Procesar = int(input("Digite la cantidad "))
suma_digitos = 0
while contador <= Cantidad_Procesar:
    contador += 1
    Numero = int(input("Digite el numero para el promedio "))
    suma_digitos += Numero
    print(f"El numero es {Numero} y la suma de los numeros {suma_digitos}") 
promedio_Final= suma_digitos/Cantidad_Procesar
print(f"la suma de los numeros es {suma_digitos} y el promedio {promedio_Final}")


#/////////////////////////CICLOS FOR/////////////////////////////////////

print("Bienvenido usuario digite cuantos datos va a procesar")
Cantidad_p = int(input("Digite la cantidad "))
suma_d = 0
for x in range(1,Cantidad_p + 1,1):
    Numero_F = int(input("Digite el numero para el promedio "))
    suma_d += Numero_F
    print(f"El numero es {Numero_F} y la suma de los numeros {suma_d}") 
promedio_F= suma_d/Cantidad_p
print(f"la suma de los numeros es {suma_d} y el promedio {promedio_F}")
