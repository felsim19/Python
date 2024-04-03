num_hombres = int(input("Digite numero de hombres  "))
num_mujeres = int(input("Digite numero de mujeres  "))
total_estudiantes = num_hombres + num_mujeres  
porcentaje_hombres = (num_hombres / total_estudiantes) * 100
porcentaje_mujeres = (num_mujeres / total_estudiantes) * 100
print(f"Porcentaje de hombres: {porcentaje_hombres}%")
print(f"Porcentaje de mujeres: {porcentaje_mujeres}%")
