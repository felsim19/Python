print("Bienvenido usuario, este progrma calcula el nuevo valor del perro")
raza = input("Ingrese la raza del perro: ")
valor_original = int(input("Ingrese el valor original del perro: "))
puesto_obtenido = int(input("Ingrese el puesto obtenido: "))

if puesto_obtenido == 1:
    nuevo_valor = valor_original * 2
elif puesto_obtenido == 2:
    nuevo_valor = valor_original + 800000
elif puesto_obtenido == 3:
    nuevo_valor = valor_original + 200000
else:
    nuevo_valor = valor_original

print("Raza: ",  str(raza))
print("Valor Original: $" + str(valor_original))
print("Puesto Obtenido: " + str(puesto_obtenido))
print("Nuevo Valor: $" + str(nuevo_valor))