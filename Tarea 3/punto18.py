tiempo_actividad = int(input("Ingrese el tiempo de la actividad en minutos: "))
if tiempo_actividad > 0:
    actividad = input("Ingrese la actividad (dormir/reposo): ")
    if actividad.lower() == "dormir":
        calorias_consumidas = tiempo_actividad * 1.08
    elif actividad.lower() == "reposo":
        calorias_consumidas = tiempo_actividad * 1.66
    else:
        calorias_consumidas = 0
else:
    calorias_consumidas = 0

print(f"La cantidad de calorías consumidas es: {calorias_consumidas}")
