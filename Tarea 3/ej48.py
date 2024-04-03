# Ejercicio 48: Calcular el total de una factura

# Función para validar el IVA
def validar_iva(iva):
    return iva in [4, 7, 16]

# Función para calcular el descuento
def calcular_descuento(total):
    if total < 1000:
        descuento = 0
    elif total < 10000:
        descuento = 0.05
    else:
        descuento = 0.1
    return descuento * total

# Variables de control
total_factura = 0
total_iva = 0

while True:
    importe = float(input("Ingrese el importe (0 para salir): "))
    if importe == 0:
        break
    iva = int(input("Ingrese el IVA (4, 7, 16): "))
    if not validar_iva(iva):
        print("IVA inválido. Por favor, introduzca 4, 7, o 16.")
        continue
    total_factura += importe
    total_iva += importe * (iva / 100)

descuento = calcular_descuento(total_factura)

print(f"Total factura: {total_factura:.2f}")
print(f"Total IVA: {total_iva:.2f}")
print(f"Descuento: {descuento:.2f}")
print(f"Total a pagar: {(total_factura + total_iva - descuento):.2f}")
