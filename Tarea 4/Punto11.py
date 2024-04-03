#//////////////////////CICLO WHILE//////////////////////////////

'''print("Bienvenido este progrma es para 10 usuarios y saber cual es el mayor sueldo")
mayor = 1
nombreGanador = ""
cantidadgente = 1
while(cantidadgente <= 10):
    nombre = str(input("Digite su nombre"))
    salario = int(input("Digite su salario"))
    cantidadautos = int(input("Digite la cantidad de autos que vendio"))
    salariosubfinal = (cantidadautos * 100000) + salario
    y = 0
    x = 1
    while(x <= cantidadautos):
        precioautos = int(input("Digite el precio del auto "))
        y += (precioautos*0.02)
        x += 1
    cantidadgente += 1
    salarioFinal = int(salariosubfinal + y)
    if mayor < salarioFinal:
        mayor = salarioFinal
        nombreGanador = nombre
print(f"el nombre del ganador es {nombreGanador}")
print(f"el mayor salario que usted se saco es de {salarioFinal}")'''

#///////////////////////7CICLO FOR/////////////////////////////////////

print("Bienvenido este progrma es para 10 usuarios y saber cual es el mayor sueldo")
mayor = 1
nombreGanador = ""
for x in range(9,10 + 1):
    nombre = str(input("Digite su nombre"))
    salario = int(input("Digite su salario"))
    cantidadautos = int(input("Digite la cantidad de autos que vendio"))
    salariosubfinal = (cantidadautos * 100000) + salario
    y = 0
    for z in range(1,cantidadautos + 1):
        precioautos = int(input("Digite el precio del auto "))
        y += (precioautos*0.02)
    salarioFinal = int(salariosubfinal + y)
    if mayor < salarioFinal:
        mayor = salarioFinal
        nombreGanador = nombre
print(f"el nombre del ganador es {nombreGanador}")
print(f"el mayor salario que usted se saco es de {salarioFinal}")