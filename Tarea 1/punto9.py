print("Bienvenido este programa calcula el costo de un articulo")
costo_articulo=int(input("ponga el costo del articulo "))
costo_utilidad=costo_articulo * 1.50
costo_impuesto=costo_articulo * 0.15
total= int(costo_utilidad + costo_impuesto)
print("el costo del articulo es de ", costo_articulo)
print("el costo del utilidad es de ", costo_utilidad)
print("el costo del impuesto es de ", costo_impuesto)
print("el costo del total del articulo es de ", total)