Numeros = []
NumerosNuevos = []

while(True):
    n = int(input("digite el numero"))
    if(n >= 0):
        print("El numero a sido a gregado")
        Numeros.append(n)
    else:
        print("usted ha puesto un numero negativo por lo tanto el sistema ha parado")
        break


for num in Numeros:
    if num not in NumerosNuevos:
        NumerosNuevos.append(num)

print(Numeros)
print(NumerosNuevos)
