print("Bienvenido usuario, este programa es para calcular el precio de estereo ")
valor_estereo_si = int(input("Digite el valor del producto sin iva "))
Marca_Producto = str(input("digite la marca del producto ").upper())

if valor_estereo_si > 2000:
    print("bien por la compra de su producto usted tiene descuento del 10% ")
    descuento_siniva = valor_estereo_si * 0.10
    total_siniva = valor_estereo_si - descuento_siniva
    print("El valor del producto sin iva es de ", str(total_siniva))
    descuento_marca = valor_estereo_si * 0.05
    iva = valor_estereo_si * 0.19
    if Marca_Producto == "NOSY":
        print("usted tiene un 5% de descuento por la marca ")
        descuento_total_si = total_siniva - descuento_marca
        print("Su proucto con los descuento quedaria en ", descuento_total_si)
        total = descuento_total_si + iva
        print("Su producto con iva y los descuento es de ", total)
    else:
        total = total_siniva + iva
        print("Su producto con iva y los descuento es de ", total)
else:
    print("usted no tiene descuento")
    total = valor_estereo_si
    print("El valor del producto es de ", str(total))