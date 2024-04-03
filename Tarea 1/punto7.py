print("Bienvenido Al Sistema De notas")
calificacion_uno=float(input("Digite su primera Nota en el examen "))
calificacion_dos=float(input("Digite su segunda Nota en el examen "))
calificacion_tres=float(input("Digite su tercera Nota en el examen "))
calificacion_cuatro=float(input("Digite su cuarta Nota en el examen "))
promedio_uno= calificacion_uno*0.30
promedio_dos= calificacion_dos*0.20
promedio_tres= calificacion_tres*0.10
promedio_cuatro= calificacion_cuatro*0.40
promedio_total= promedio_uno + promedio_dos + promedio_tres + promedio_cuatro
print("Señor usuario su promedio es ", + promedio_total)