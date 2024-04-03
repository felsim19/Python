print("Bienvenido este programa declara numeros hasta que introduzca un numero negativo ")
numeros = []
while True:
    numero= int(input("Digite el numero "))
    if numero >= 0:
        print("genial el numero esta guardado")
        numeros.append(numero)
    else:
        print("bien usted puso un numero negativo por lo tanto sus numero son")
        for x in numeros:
            print(x)
        break