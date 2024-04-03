import random

def tiradaDados():
    global dado1, dado2
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    print(f"La tirada de del dado 1 es de: {dado1}")
    print(f"La tirada de del dado 1 es de: {dado2}")     

def NumeroSuma(dado1, dado2):
    sumaDados = dado1 + dado2
    return sumaDados
    
    
print("Bienvenido al juego de crups ")
Inicio = int(input("presione 1 para jugar "))

if (Inicio == 1):
    print("usted va a tirar los dados")
    tiradaDados()
    numero = NumeroSuma(dado1, dado2)
    print(f"la suma de los dados es {numero}")
    if (numero == 7 or numero == 11):
        print("Felicidades ha ganado el juego")
    elif(numero == 2 or numero == 3 or numero == 12):
        print("caieste en craps la casa gana, prediste!!")
    else:
        print(f"el {numero} es un numero dela tirada\npara ganar le vas a volver a dar y tiene que repetir el mismo numero\nsi sacas el 7 pierdes")
        while(True):
            tiradaDados()
            numero2 = NumeroSuma(dado1, dado2)
            print(f"la suma de los dados es {numero2}")
            if(numero2 == 7):
                print(f"El jugador perdio por que saco el numero {numero2}")
                break
            if(numero == numero2):
                print(f"El jugador gano por que saco el numero {numero2}")
                break

        
