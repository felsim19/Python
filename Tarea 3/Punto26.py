promedio = float(input("Ingrese el promedio del alumno: "))
colegiatura = int(input("Ingrese el valor de la colegiatura "))
descuento = 0
iva = 0
total = 0
if promedio >= 9:
    descuento = colegiatura *0.30
    iva = 0
    total = colegiatura - descuento
elif promedio < 9:
    descuento = 0
    iva = colegiatura * 0.19
    total = colegiatura + iva
print(f"el iva es de ${iva}")
print(f"el descuento es de ${descuento}") 
print(f"Total a pagar por la colegiatura: ${total}")
