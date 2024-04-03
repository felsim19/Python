print("Bienvenido usuario")
cantidas_llantas = int(input("¿cuantas llantas deseas llevar?"))
if cantidas_llantas <= 0:
    print("no puede llevar menos de 0 o cero llantas")
elif cantidas_llantas < 5:
    precio_llanta = 300
    total = int(cantidas_llantas * precio_llanta)
    print("usted lleva ", str(cantidas_llantas), "llantas")
    print("las llantas le salen a un precio de ", str(precio_llanta))
    print("y el costo que va a pagar es de $", str(total), "dolares")
elif cantidas_llantas < 10:
    precio_llanta = 250
    total = int(cantidas_llantas * precio_llanta)
    print("usted lleva ", str(cantidas_llantas), "llantas")
    print("las llantas le salen a un precio de ", str(precio_llanta))
    print("y el costo que va a pagar es de $", str(total), "dolares")
else:
    precio_llanta = 200
    total = int(cantidas_llantas * precio_llanta)
    print("usted lleva ", str(cantidas_llantas), "llantas")
    print("las llantas le salen a un precio de ", str(precio_llanta))
    print("y el costo que va a pagar es de $", str(total), "dolares")