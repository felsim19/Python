print("bienvenido usuario")
cantidad_computadoras = int(input("¿cuantas computadoras deseas llevar?"))
precio_computadoras = 11000
if cantidad_computadoras <= 0:
    print("usted no puede pedir menos de 0 o cero ya que no son validas")
elif cantidad_computadoras < 5:
    print("usted va a llevar ", str(cantidad_computadoras), "computadoras")
    subtotal = int(precio_computadoras*cantidad_computadoras)
    subdescuento = int(subtotal * 0.10)
    total = int(subtotal - subdescuento)
    print("su cuenta sin el descuento es de ", str(subtotal))
    print("usted lleva menos de 5 productos por lo tanto tiene un descuento del 10% que equivale a ", str(subdescuento))
    print("y eso le cuesta", str(total))
elif cantidad_computadoras < 10:
    print("usted va a llevar ", str(cantidad_computadoras), "computadoras")
    subtotal = int(precio_computadoras*cantidad_computadoras)
    subdescuento = int(subtotal * 0.20)
    total = int(subtotal - subdescuento)
    print("su cuenta sin el descuento es de ", str(subtotal))
    print("usted lleva menos de 10 productos por lo tanto tiene un descuento del 20% que equivale a ", str(subdescuento))
    print("y eso le cuesta", str(total))
else:
    print("usted va a llevar ", str(cantidad_computadoras), "computadoras")
    subtotal = int(precio_computadoras*cantidad_computadoras)
    subdescuento = int(subtotal * 0.40)
    total = int(subtotal - subdescuento)
    print("su cuenta sin el descuento es de ", str(subtotal))
    print("usted lleva mas de 10 productos por lo tanto tiene un descuento del 40% que equivale a ", str(subdescuento))
    print("y eso le cuesta", str(total))