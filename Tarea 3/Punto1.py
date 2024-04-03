sueldo_base = int(input("Digite su sueldo base "))
ventas = int(input("Digite el valor 3 de las 3 ventas "))
comisiones = ventas * 0.10
total = sueldo_base + comisiones
print(f"El vendedor recibirá ${comisiones} por concepto de comisiones en el mes.")
print(f"El total que recibirá en el mes será de ${total}")
