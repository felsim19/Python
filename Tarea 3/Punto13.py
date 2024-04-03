examen_matematicas = int(input("digite lo que saco en el examen matematicas "))
tarea1_matematicas = int(input("digite la nota de la tarea1 matematicas "))
tarea2_matematicas = int(input("digite la nota de la tarea2 matematicas "))
tarea3_matematicas = int(input("digite la nota de la tarea3 matematicas "))
promedio_tareas_matematicas = (tarea1_matematicas + tarea2_matematicas + tarea3_matematicas)/3

examen_fisica = int(input("digite lo que saco en el examen fisica "))
tarea1_fisica = int(input("digite lo que saco en el tarea1 fisica"))
tarea2_fisica = int(input("digite lo que saco en el tarea2 fisica"))
promedio_tareas_fisica = (tarea2_fisica + tarea1_fisica)/2

examen_quimica = int(input("digite lo que saco en el examen quimica "))
tarea1_quimica = int(input("digite la nota de la tarea1 quimica"))
tarea2_quimica = int(input("digite la nota de la tarea2 quimica"))
tarea3_quimica = int(input("digite la nota de la tarea3 quimica"))
promedio_tareas_quimica = (tarea1_quimica + tarea2_quimica + tarea3_quimica)

promedio_matematicas = (examen_matematicas * 0.9 + promedio_tareas_matematicas * 0.1)
promedio_fisica = (examen_fisica * 0.8 + promedio_tareas_fisica * 0.2)
promedio_quimica = (examen_quimica * 0.85 + promedio_tareas_quimica * 0.15)

promedio_general = (promedio_matematicas + promedio_fisica + promedio_quimica)/ 3

print(f"Promedio general: {promedio_general}")
print(f"Promedio en Matemáticas: {promedio_matematicas}")
print(f"Promedio en Física: {promedio_fisica}")
print(f"Promedio en Química: {promedio_quimica}")
