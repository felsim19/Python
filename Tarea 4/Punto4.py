#////////////////////////////////////Ciclo WHILE///////////////////
'''
EstuiantesPromedio = 750
Año = 2023
Creacimiento_Anual = int(EstuiantesPromedio * 0.12)
print(f"hay de estudiantes {EstuiantesPromedio} y el crecimiento anual {Creacimiento_Anual} y es el año {Año}")

while Año < 2035:
    Año += 1
    EstuiantesPromedio += Creacimiento_Anual
    Creacimiento_Anual = int(EstuiantesPromedio * 0.12)
    print(f"hay de estudiantes {EstuiantesPromedio} y el crecimiento anual {Creacimiento_Anual} y es el año {Año}")
'''

#///////////////////////////////////////CICLO FOR///////////////////
    
EstudiantesP = 750
CreacimientoA = int(EstudiantesP * 0.12)
año = 2023
print(f"hay de estudiantes {EstudiantesP} y el crecimiento anual {CreacimientoA} y es el año {año}")
for año in range(2024, 2036, 1):
    EstudiantesP += CreacimientoA
    CreacimientoA= int(EstudiantesP * 0.12)
    print(f"hay de estudiantes {EstudiantesP} y el crecimiento anual {CreacimientoA} y es el año {año}")
