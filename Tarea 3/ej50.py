# Ejercicio 50: Determinar si un año es bisiesto

# Función para determinar si un año es bisiesto
def es_bisiesto(año):
    if año % 4 != 0:
        return False
    elif año % 100 != 0:
        return True
    elif año % 400 == 0:
        return True
    else:
        return False

# Solicitar al usuario el año
año = int(input("Ingrese un año: "))
# Determinar si el año es bisiesto
if es_bisiesto(año):
    print(f"{año} es un año bisiesto.")
else:
    print(f"{año} no es un año bisiesto.")
