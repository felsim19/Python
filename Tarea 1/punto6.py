print("Bienvenido este programa calcula el precio de venta de un articulo")
nombre_articulo=str(input("Digite el nombre del articulo "))
costo_produccion=int(input("Digite cuanto es el costo de produccion "))
calcular_utilidad=costo_produccion * 1.20
calcular_impuesto=costo_produccion * 0.15
total= int(calcular_utilidad + calcular_impuesto)
print("Usted esta vendiendo", nombre_articulo)
print("y lo tiene que vender en", total)