print("Bienvenido, este programa da el costo del alquiler")
modelo = input("Ingrese el modelo (BMW, MEGANE, MERCEDES, TWINGO, CHEVROLET AVEO): ").upper()
print(modelo)
dias = int(input("Ingrese el número de días de alquiler: "))
seguro_todo_riesgo = input("¿Desea seguro todo riesgo? (sí/no): ").lower() == "sí"
precio_bmw = 650000
precio_megane = 120000
precio_mercedes = 700000
precio_twingo = 100000
precio_aveo = 150000
descuento_3_5_dias = 0.10
descuento_6_10_dias = 0.15
descuento_mas_10_dias = 0.20
incremento_seguro = 0.05

if modelo == "BMW":
    precio_base = precio_bmw
elif modelo == "MEGANE":
    precio_base = precio_megane
elif modelo == "MERCEDES":
    precio_base = precio_mercedes
elif modelo == "TWINGO":
    precio_base = precio_twingo
elif modelo == "CHEVROLET AVEO":
    precio_base = precio_aveo
else:
    print("Modelo no válido.")
    exit()

descuento = 0
if 3 <= dias <= 5:
    descuento = descuento_3_5_dias
elif 6 <= dias <= 10:
    descuento = descuento_6_10_dias
elif dias > 10:
    descuento = descuento_mas_10_dias


precio_descuento = precio_base - (precio_base * descuento)

costo_seguro = precio_descuento * incremento_seguro if seguro_todo_riesgo else 0

costo_total = (precio_descuento + costo_seguro) * dias

print("Cliente con modelo " + modelo + ", " + str(dias) + " días de alquiler y " + ("con" if seguro_todo_riesgo else "sin") + " seguro todo riesgo:")
print("Precio con descuento: $" + str(precio_descuento))
print("Descuento aplicado: " + str(descuento * 100) + "%")
print("Costo del seguro: $" + str(costo_seguro))
print("Costo total: $" + str(costo_total))