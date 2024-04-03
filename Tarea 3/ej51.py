# Ejercicio 51: Calcular el día siguiente

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

# Días por mes en un año no bisiesto
dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Solicitar al usuario el día, mes y año
dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
año = int(input("Ingrese el año: "))

# Incrementar el día
dia += 1

# Determinar si el año es bisiesto y ajustar el número de días en febrero
if es_bisiesto(año):
    dias_por_mes[2] = 29

# Verificar si se necesita ajustar el mes y/o el año
if dia > dias_por_mes[mes]:
    dia = 1
    mes += 1
    if mes > 12:
        mes = 1
        año += 1

# Mostrar el día siguiente
print(f"El día siguiente es: {dia}/{mes}/{año}")
