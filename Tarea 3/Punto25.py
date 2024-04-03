monto = float(input("Ingrese el monto por el que se efectúa la fianza: "))
cuota = 0
if monto < 50000:
    cuota = int(monto * 0.03)
else:
    cuota = int(monto * 0.02)  
print(f"Cuota a pagar por la fianza: ${cuota}")
