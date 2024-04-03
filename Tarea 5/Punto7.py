print("Bienvenido en este programa dejara su nombre y su edad hasta que le de el simbolo (*)")
nombres = []
edades = []
while True:
    nombre = str(input("Digite su nombre "))
    if nombre == "*":
        print("Usted a salido del programa ")
        break

    nombres.append(nombre)
    edad = int(input("Digite su edad "))
    edades.append(edad)

for i in range(len(nombres)):
    if edades[i] >= 18:
        print(f"Este estudiante {nombres[i]} es mayor de edad y tiene {edades[i]}") 

    if edades[i] < 18:
        print(f"Este estudiante {nombres[i]} es menor de edad y tiene {edades[i]}")   

    

