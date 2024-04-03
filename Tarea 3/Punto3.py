parcial1 = float(input("Diigite la nota del primer parcial "))
parcial2 = float(input("Diigite la nota del segundo parcial "))
parcial3 = float(input("Diigite la nota del tercer parcial "))
examen_final = float(input("Diigite la nota del examen final "))
trabajo_final = float(input("Diigite la nota del trabajo final "))
promedio_parciales = (parcial1 + parcial2 + parcial3) / 3
calificacion_final = (promedio_parciales * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15)
print(f"La calificación final en Algoritmos es: {calificacion_final}")

