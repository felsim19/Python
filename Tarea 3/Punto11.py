tiempo_lunes = int(input("Digite el tiempo del lunes en minutos "))
tiempo_miercoles = int(input("Digite el tiempo del miercoles en minutos "))
tiempo_viernes = int(input("Digite el tiempo del viernes en minutos "))
tiempo_promedio = (tiempo_lunes + tiempo_miercoles + tiempo_viernes) / 3
print(tiempo_promedio)
print(f"El tiempo promedio de la persona en recorrer la ruta en una semana es de: {tiempo_promedio} minutos.")
