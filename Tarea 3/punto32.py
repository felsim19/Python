valor_automovil = float(input("Ingrese el valor del automóvil: "))
valor_terreno = float(input("Ingrese el valor del terreno: "))
devaluacion_automovil = valor_automovil * 0.10 * 3
incremento_terreno = valor_terreno * 0.05 * 3
if devaluacion_automovil <= 0.5 * incremento_terreno:
    print("Es recomendable comprar el automóvil.")
else:
    print("Es recomendable comprar el terreno.")
