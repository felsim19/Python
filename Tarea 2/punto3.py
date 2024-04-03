print("Bienvenido usuario")
respuesta = input("este programa es de respuestas correctas escriba si para seguir")
if respuesta == "si":
    print("bien esta es la primera pregunta del juego")
    respuesta1 =input("¿Colon descubrio america?")
    if respuesta1 == "si":
        print("Felicidades pasaste la primera ronda")
        respuesta2 = input("La independica de mexico fue en 1810?")
        if respuesta2 == "si":
            print("Felicidades pasaste la segunda ronda")
            respuesta3 = input("The doors fue un grupo de rock americano")
            if respuesta3 == "si":
                print("Felicidades ganaste el juego")
            else:
                print("ya perdiste, gracias por intentar")
        else:
            print("ya perdiste, gracias por intentar")
    else:
        print("ya perdiste, gracias por intentar")
else: 
    print("Gracias en otra ocasion jugamos")