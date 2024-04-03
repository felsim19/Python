
nombre_articulo = input("Ingrese el nombre del artículo: ")
clave = input("Ingrese la clave del artículo (01 o 02): ")
precio_original = float(input("Ingrese el precio original del artículo: "))
precio_descuento = 0

if clave == "01":
    descuento = precio_original * 0.10
    precio_descuento = precio_original - descuento
elif clave == "02":
    descuento = precio_original * 0.20
    precio_descuento = precio_original - descuento

print(f"Nombre del artículo: {nombre_articulo}")
print(f"Clave: {clave}")
print(f"Precio original: ${precio_original}")
print(f"Precio con descuento: ${precio_descuento}")
