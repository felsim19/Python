monedas = 0
oportunidad = 0
castigos = []
armas = []
oportunidad1 = 0

def nivel1():
    global monedas , armas , castigos
    preguntasCorrectas = 0
    PreguntasIncorrectas = 0
    pregunta1= str(input("1.cuanto es 2+2? \nA.2\nB.1\nC.3\nD.4\n"))
    if(pregunta1 == "d"):
        print("Felicidades esa es la respuesta correcta")
        preguntasCorrectas += 1
    else:
        print("esa respuesta es incorrecta")
        PreguntasIncorrectas += 1
    pregunta2= str(input("2.cuanto es 1+1? \nA.2\nB.1\nC.3\nD.4\n"))
    if(pregunta2 == "a"):
        print("Felicidades esa es la respuesta correcta")
        preguntasCorrectas += 1
    else:
        print("esa respuesta es incorrecta")
        PreguntasIncorrectas += 1
    pregunta3= str(input("3.cuanto es 2+1? \nA.2\nB.1\nC.3\nD.4\n"))
    if(pregunta3 == "c"):
        print("Felicidades esa es la respuesta correcta")
        preguntasCorrectas += 1
    else:
        print("esa respuesta es incorrecta")
        PreguntasIncorrectas += 1
    pregunta4= str(input("4.cuanto es 1-1? \nA.2\nB.0\nC.3\nD.4\n"))
    if(pregunta4 == "b"):
        print("Felicidades esa es la respuesta correcta")
        preguntasCorrectas += 1
    else:
        print("esa respuesta es incorrecta")
        PreguntasIncorrectas += 1
    pregunta5= str(input("5.cuanto es 2+3? \nA.2\nB.5\nC.3\nD.4\n"))
    if(pregunta5 == "b"):
        print("Felicidades esa es la respuesta correcta")
        preguntasCorrectas += 1
    else:
        print("esa respuesta es incorrecta")
        PreguntasIncorrectas += 1
    
    if(preguntasCorrectas <= 1):
        print("sera sentenciado por el señor oscuro por responder una bien")
        return False
    else:
        print("Felicidades ha sido recompensado con la espada de zeus")
        objeto = "Espada de zeus"
        armas.append(objeto)
        monedas += 10000
        aciertos = preguntasCorrectas*1000
        monedas += aciertos
        if(PreguntasIncorrectas == 3):
            print("Usted recibira un castigo por responder 3 mal")
            castigo = "envenendo por serpiente"
            castigos.append(castigo)
        print("Las preguntas correctas que respondio bien fueron " + str(preguntasCorrectas))
        print("Las preguntas incorrectas que respondio fueron " + str(PreguntasIncorrectas))
        print("su cantidad de monedas "+ str(monedas))
        print("sus armas son " + str(armas))
        print("Sus castigos son " + str(castigos))
        return True

def nivel2():
    global monedas , armas , castigos
    preguntasCorrectas = 0
    PreguntasIncorrectas = 0
    pregunta1= str(input("1.cuanto es 3+3? \nA.5\nB.6\nC.7\nD.8\n"))
    if(pregunta1 == "b"):
        print("Felicidades esa es la respuesta correcta")
        preguntasCorrectas += 1
    else:
        print("esa respuesta es incorrecta")
        PreguntasIncorrectas += 1
    pregunta2= str(input("2.cuanto es 3+4? \nA.5\nB.6\nC.7\nD.8\n"))
    if(pregunta2 == "c"):
        print("Felicidades esa es la respuesta correcta")
        preguntasCorrectas += 1
    else:
        print("esa respuesta es incorrecta")
        PreguntasIncorrectas += 1
    pregunta3= str(input("3.cuanto es 3+5? \nA.5\nB.6\nC.7\nD.8\n"))
    if(pregunta3 == "d"):
        print("Felicidades esa es la respuesta correcta")
        preguntasCorrectas += 1
    else:
        print("esa respuesta es incorrecta")
        PreguntasIncorrectas += 1
    pregunta4= str(input("4.cuanto es 5-1? \nA.2\nB.0\nC.3\nD.4\n"))
    if(pregunta4 == "d"):
        print("Felicidades esa es la respuesta correcta")
        preguntasCorrectas += 1
    else:
        print("esa respuesta es incorrecta")
        PreguntasIncorrectas += 1
    pregunta5= str(input("5.cuanto es 6+3? \nA.9\nB.10\nC.11\nD.12\n"))
    if(pregunta5 == "a"):
        print("Felicidades esa es la respuesta correcta")
        preguntasCorrectas += 1
    else:
        print("esa respuesta es incorrecta")
        PreguntasIncorrectas += 1
    
    if(preguntasCorrectas <= 2):
        print("sera sentenciado por el señor oscuro por responder solo dos bien")
        return False
    else:
        print("Felicidades ha sido recompensado con el Sable dorado")
        objeto = "Sable dorado"
        armas.append(objeto)
        monedas += 100000
        aciertos = preguntasCorrectas*20000
        monedas += aciertos
        if(PreguntasIncorrectas == 2):
            print("Usted recibira un castigo por responder 2 mal")
            castigo = "lentitud en los movimientos"
            castigos.append(castigo)
        print("Las preguntas correctas que respondio bien fueron " + str(preguntasCorrectas))
        print("Las preguntas incorrectas que respondio fueron " + str(PreguntasIncorrectas))
        print("su cantidad de monedas "+ str(monedas))
        print("sus armas son " + str(armas))
        print("Sus castigos son " + str(castigos))
        return True

def nivel3():
    global monedas , armas , castigos , oportunidad
    preguntasCorrectas = 0
    PreguntasIncorrectas = 0
    aciertos = 0
    pregunta1= str(input("1.cuanto es 7+8? \nA.15\nB.16\nC.17\nD.18\n"))
    print("Esta respuesta vale 3000")
    if(pregunta1 == "a"):
        print("Felicidades esa es la respuesta correcta")
        preguntasCorrectas += 1
        aciertos += 3000
    else:
        print("esa respuesta es incorrecta")
        PreguntasIncorrectas += 1
    pregunta2= str(input("2.cuanto es 13+14? \nA.25\nB.26\nC.27\nD.28\n"))
    print("Esta respuesta vale 2000")
    if(pregunta2 == "c"):
        print("Felicidades esa es la respuesta correcta")
        preguntasCorrectas += 1
        aciertos += 2000
    else:
        print("esa respuesta es incorrecta")
        PreguntasIncorrectas += 1
    pregunta3= str(input("3.cuanto es 13+15? \nA.25\nB.26\nC.27\nD.28\n"))
    print("Esta respuesta vale 3000")
    if(pregunta3 == "d"):
        print("Felicidades esa es la respuesta correcta")
        preguntasCorrectas += 1
        aciertos += 3000
    else:
        print("esa respuesta es incorrecta")
        PreguntasIncorrectas += 1
    pregunta4= str(input("4.cuanto es 15-11? \nA.2\nB.0\nC.3\nD.4\n"))
    print("Esta respuesta vale 6000")
    if(pregunta4 == "d"):
        print("Felicidades esa es la respuesta correcta")
        preguntasCorrectas += 1
        aciertos += 6000
    else:
        print("esa respuesta es incorrecta")
        PreguntasIncorrectas += 1
    pregunta5= str(input("5.cuanto es 16+13? \nA.29\nB.10\nC.21\nD.32\n"))
    print("Esta respuesta vale 4000")
    if(pregunta5 == "a"):
        print("Felicidades esa es la respuesta correcta")
        preguntasCorrectas += 1
        aciertos += 4000
    else:
        print("esa respuesta es incorrecta")
        PreguntasIncorrectas += 1
    
    if(aciertos >= 10000):
        if (oportunidad == 0):
            print("Felicidades ha obtenido el arco de zafiro y 1000000 de monedas de oro")
            monedas += 1000000
            objeto = "arco zafiro"
            armas.append(objeto)
            print("y por completarlo en el primer inteto te dare el poder de la super fuerza y el escudo dorado")
            objeto1 = "Super fuerza"
            objeto2 = "escudo dorado"
            armas.append(objeto1)
            armas.append(objeto2)
            print("Las preguntas correctas que respondio bien fueron " + str(preguntasCorrectas))
            print("Las preguntas incorrectas que respondio fueron " + str(PreguntasIncorrectas))
            print("su cantidad de monedas "+ str(monedas))
            print("sus armas son " + str(armas))
            print("Sus castigos son " + str(castigos))
            return True
        else:
            print("Usted respondio todo bien pero ya que uso la segunda oportunidad solo se le dara 500000 y tendra un castigo")
            monedas += 500000
            castigo = "enfermedad de fuego"
            castigos.append(castigo)
            print("Las preguntas correctas que respondio bien fueron " + str(preguntasCorrectas))
            print("Las preguntas incorrectas que respondio fueron " + str(PreguntasIncorrectas))
            print("su cantidad de monedas "+ str(monedas))
            print("sus armas son " + str(armas))
            print("Sus castigos son " + str(castigos))
            return True
    elif(aciertos >= 6000):
        oportunidad += 1
        print("Tus monedas son" + str(monedas))
        print("tienes que pagar 20000 por una segunda oprtunidad")
        monedas -= 200000
        print("las monedas que quedarons son" + str(monedas))
        nivel3()
    elif(aciertos == 2000):
        print("Tienes que regresar al nivel uno con un castigo")
        castigo = "enfermedad de hielo"
        castigos.append(castigo)
        print("Sus castigos son " + str(castigos))
        nivel1()
        nivel2()
        nivel3()
    elif(aciertos == 0):
        print("Sera sentenciado a vivir en un mundo desconocido para siempre")
        return False

def nivel4():
    global monedas , armas , castigos , oportunidad1
    preguntasCorrectas = 0
    PreguntasIncorrectas = 0
    pregunta1= str(input("1.cuanto es 8+9? \nA.15\nB.16\nC.17\nD.18\n"))
    if(pregunta1 == "c"):
        print("Felicidades esa es la respuesta correcta")
        preguntasCorrectas += 1
    else:
        print("esa respuesta es incorrecta")
        PreguntasIncorrectas += 1
    pregunta2= str(input("2.cuanto es 17+16? \nA.25\nB.26\nC.33\nD.28\n"))
    if(pregunta2 == "c"):
        print("Felicidades esa es la respuesta correcta")
        preguntasCorrectas += 1
    else:
        print("esa respuesta es incorrecta")
        PreguntasIncorrectas += 1
    if(preguntasCorrectas >= 2):
        monedas += 10000000
        objeto = "La armadura con todo los super poderes legendarios"
        armas.append(objeto)
        print("felicidades usted a derrotado al señor oscuro y salavado el mundo de sus poderes oscuros")
        print("Las preguntas correctas que respondio bien fueron " + str(preguntasCorrectas))
        print("Las preguntas incorrectas que respondio fueron " + str(PreguntasIncorrectas))
        print("su cantidad de monedas "+ str(monedas))
        print("sus armas son " + str(armas))
        print("Sus castigos son " + str(castigos))
        return False
    
    if(preguntasCorrectas == 1):
        print("Tus monedas son" + str(monedas))
        print("tienes dos opciones 1.regresar al nivel uno o  2.pagar $1200000 de monedas para un segundo intento")
        opcion1 = int(input("eliga la opcion"))
        if (opcion1 == 1):
            nivel1()
            nivel2()
            nivel3()
            nivel4()
            monedas -= monedas
        elif(opcion1 == 2):
            if(monedas >= 1200000 and oportunidad1 == 0):
                print("Usted va a pagar 1200000 de monedas")
                monedas -= 1200000
                oportunidad1 += 1
                nivel4()
            else:
                print("Usted tiene saldo insuciente")
                return False
        else:
            print("Usted a perdido las dos respuestas")
            return False
            
while(True):
    if nivel1() == False:
        break
    if nivel2() == False:
        break
    if nivel3() == False:
        break
    if nivel4() == False:
        break


