numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
if numero1 > numero2:
    numero1, numero2 = numero2, numero1
print(f"Los números en forma ascendente son: {numero1}, {numero2}")
