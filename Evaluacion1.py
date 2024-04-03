puntajeInicial = 0
monedasOro = 0 
vidas = 5
poderes = []
preguntasCorrectas = 0
preguntasIncorrectas = 0
reincio10 = 0

def veintepregunta():
    global puntajeInicial, vidas, poderes, preguntasCorrectas, preguntasIncorrectas,monedasOro,reincio10
    pregunta1= str(input("1.cuanto es 2+2? \nA.2\nB.1\nC.3\nD.4\n"))
    if(pregunta1 == "d"):
        print("Felicidades esa es la respuesta correcta")
        puntajeInicial += 30
        poder = "volar"
        poderes.append(poder)
        preguntasCorrectas += 1
        print(f"Usted lleva {preguntasCorrectas} respuestas correctas")
        print(f"Por contestar esta pregunta bien le doy 30 puntaje")
        print(f"por contestar esta pregunta bien recibe {poder}")
        print(f"Sus puntaje es {puntajeInicial}")
        print(f"Sus vidas son {vidas}")
        print(f"Sus poderes son {poderes}")
    else:
        print("esa respuesta es incorrecta")
        vidas -= 1
        preguntasIncorrectas += 1
        if preguntasIncorrectas == 1:
            preguntasCorrectas -= preguntasCorrectas
            preguntasIncorrectas -= preguntasIncorrectas
        print(f"Sus puntaje es {puntajeInicial}")
        print(f"Sus vidas son {vidas}")
        print(f"Sus poderes es {poderes}")
    pregunta2= str(input("2.cuanto es 3+2? \nA.2\nB.5\nC.3\nD.4\n"))
    if(pregunta2 == "b"):
        print("Felicidades esa es la respuesta correcta")
        puntajeInicial += 30
        poder = "lanzar fuego"
        poderes.append(poder)
        preguntasCorrectas += 1
        print(f"Usted lleva {preguntasCorrectas} respuestas correctas")
        print(f"Por contestar esta pregunta bien le doy 30 puntaje")
        print(f"por contestar esta pregunta bien recibe {poder}")
        print(f"Sus puntaje es {puntajeInicial}")
        print(f"Sus vidas son {vidas}")
        print(f"Sus poderes son {poderes}")
    else:
        print("esa respuesta es incorrecta")
        vidas -= 1
        preguntasIncorrectas += 1
        if preguntasIncorrectas == 1:
            preguntasCorrectas -= preguntasCorrectas
            preguntasIncorrectas -= preguntasIncorrectas
        print(f"Sus puntaje es {puntajeInicial}")
        print(f"Sus vidas son {vidas}")
        print(f"Sus poderes es {poderes}")
    pregunta3= str(input("3.cuanto es 1+2? \nA.2\nB.1\nC.3\nD.4\n"))
    if(pregunta3 == "c"):
        print("Felicidades esa es la respuesta correcta")
        puntajeInicial += 30
        poder = "lanzar hielo"
        poderes.append(poder)
        preguntasCorrectas += 1
        print(f"Usted lleva {preguntasCorrectas} respuestas correctas")
        print(f"Por contestar esta pregunta bien le doy 30 puntaje")
        print(f"por contestar esta pregunta bien recibe {poder}")
        print(f"Sus puntaje es {puntajeInicial}")
        print(f"Sus vidas son {vidas}")
        print(f"Sus poderes son {poderes}")
    else:
        print("esa respuesta es incorrecta")
        vidas -= 1
        preguntasIncorrectas += 1
        if preguntasIncorrectas == 1:
            preguntasCorrectas -= preguntasCorrectas
            preguntasIncorrectas -= preguntasIncorrectas        
        print(f"Sus puntaje es {puntajeInicial}")
        print(f"Sus vidas son {vidas}")
        print(f"Sus poderes es {poderes}")
    pregunta4= str(input("4.cuanto es 1+1? \nA.2\nB.1\nC.3\nD.4\n"))
    if(pregunta4 == "a"):
        print("Felicidades esa es la respuesta correcta")
        puntajeInicial += 30
        poder = "superfuerza"
        poderes.append(poder)
        preguntasCorrectas += 1
        print(f"Usted lleva {preguntasCorrectas} respuestas correctas")
        print(f"Por contestar esta pregunta bien le doy 30 puntaje")
        print(f"por contestar esta pregunta bien recibe {poder}")
        print(f"Sus puntaje es {puntajeInicial}")
        print(f"Sus vidas son {vidas}")
        print(f"Sus poderes son {poderes}")
    else:
        print("esa respuesta es incorrecta")
        vidas -= 1
        preguntasIncorrectas += 1
        if preguntasIncorrectas == 1:
            preguntasCorrectas -= preguntasCorrectas
            preguntasIncorrectas -= preguntasIncorrectas        
        print(f"Sus puntaje es {puntajeInicial}")
        print(f"Sus vidas son {vidas}")
        print(f"Sus poderes es {poderes}")
    pregunta5= str(input("5.cuanto es 6+2? \nA.2\nB.1\nC.3\nD.8\n"))
    if(pregunta5 == "d"):
        print("Felicidades esa es la respuesta correcta")
        puntajeInicial += 30
        poder = "convertirse en cosas"
        poderes.append(poder)
        preguntasCorrectas += 1
        print(f"Usted lleva {preguntasCorrectas} respuestas correctas")
        print(f"Por contestar esta pregunta bien le doy 30 puntaje")
        print(f"por contestar esta pregunta bien recibe {poder}")
        print(f"Sus puntaje es {puntajeInicial}")
        print(f"Sus vidas son {vidas}")
        print(f"Sus poderes son {poderes}")
    else:
        print("esa respuesta es incorrecta")
        vidas -= 1
        preguntasIncorrectas += 1
        if preguntasIncorrectas == 1:
            preguntasCorrectas -= preguntasCorrectas
            preguntasIncorrectas -= preguntasIncorrectas         
        print(f"Sus puntaje es {puntajeInicial}")
        print(f"Sus vidas son {vidas}")
        print(f"Sus poderes es {poderes}")
        if (vidas == 0):
            return False
    pregunta6= str(input("6.cuanto es 6+6? \nA.12\nB.11\nC.13\nD.18\n"))
    if(pregunta6 == "a"):
        print("Felicidades esa es la respuesta correcta")
        puntajeInicial += 30
        poder = "telequinesis"
        poderes.append(poder)
        preguntasCorrectas += 1
        print(f"Usted lleva {preguntasCorrectas} respuestas correctas")
        print(f"Por contestar esta pregunta bien le doy 30 puntaje")
        print(f"por contestar esta pregunta bien recibe {poder}")
        print(f"Sus puntaje es {puntajeInicial}")
        print(f"Sus vidas son {vidas}")
        print(f"Sus poderes son {poderes}")
    else:
        print("esa respuesta es incorrecta")
        vidas -= 1
        preguntasIncorrectas += 1
        if preguntasIncorrectas == 1:
            preguntasCorrectas -= preguntasCorrectas
            preguntasIncorrectas -= preguntasIncorrectas         
        print(f"Sus puntaje es {puntajeInicial}")
        print(f"Sus vidas son {vidas}")
        print(f"Sus poderes es {poderes}")
        if (vidas == 0):
            return False
    pregunta7= str(input("7.cuanto es 16+2? \nA.12\nB.11\nC.13\nD.18\n"))
    if(pregunta7 == "d"):
        print("Felicidades esa es la respuesta correcta")
        puntajeInicial += 30
        poder = "ojos laser"
        poderes.append(poder)
        preguntasCorrectas += 1
        print(f"Usted lleva {preguntasCorrectas} respuestas correctas")
        print(f"Por contestar esta pregunta bien le doy 30 puntaje")
        print(f"por contestar esta pregunta bien recibe {poder}")
        print(f"Sus puntaje es {puntajeInicial}")
        print(f"Sus vidas son {vidas}")
        print(f"Sus poderes son {poderes}")
    else:
        print("esa respuesta es incorrecta")
        vidas -= 1
        preguntasIncorrectas += 1
        if preguntasIncorrectas == 1:
            preguntasCorrectas -= preguntasCorrectas
            preguntasIncorrectas -= preguntasIncorrectas          
        print(f"Sus puntaje es {puntajeInicial}")
        print(f"Sus vidas son {vidas}")
        print(f"Sus poderes es {poderes}")
        if (vidas == 0):
            return False
    pregunta8= str(input("8.cuanto es 16+12? \nA.22\nB.21\nC.23\nD.28\n"))
    if(pregunta8 == "d"):
        print("Felicidades esa es la respuesta correcta")
        puntajeInicial += 30
        poder = "garras de adamantiun"
        poderes.append(poder)
        preguntasCorrectas += 1
        print(f"Usted lleva {preguntasCorrectas} respuestas correctas")
        print(f"Por contestar esta pregunta bien le doy 30 puntaje")
        print(f"por contestar esta pregunta bien recibe {poder}")
        print(f"Sus puntaje es {puntajeInicial}")
        print(f"Sus vidas son {vidas}")
        print(f"Sus poderes son {poderes}")
    else:
        print("esa respuesta es incorrecta")
        vidas -= 1
        preguntasIncorrectas += 1
        if preguntasIncorrectas == 1:
            preguntasCorrectas -= preguntasCorrectas
            preguntasIncorrectas -= preguntasIncorrectas          
        print(f"Sus puntaje es {puntajeInicial}")
        print(f"Sus vidas son {vidas}")
        print(f"Sus poderes son {poderes}")
        if (vidas == 0):
            return False
    pregunta9= str(input("9.cuanto es 6+3? \nA.2\nB.9\nC.3\nD.8\n"))
    if(pregunta9 == "b"):
        print("Felicidades esa es la respuesta correcta")
        puntajeInicial += 30
        poder = "cambiar el clima"
        poderes.append(poder)
        preguntasCorrectas += 1
        print(f"Usted lleva {preguntasCorrectas} respuestas correctas")
        print(f"Por contestar esta pregunta bien le doy 30 puntaje")
        print(f"por contestar esta pregunta bien recibe {poder}")
        print(f"Sus puntaje es {puntajeInicial}")
        print(f"Sus vidas son {vidas}")
        print(f"Sus poderes son {poderes}")
    else:
        print("esa respuesta es incorrecta")
        vidas -= 1
        preguntasIncorrectas += 1
        if preguntasIncorrectas == 1:
            preguntasCorrectas -= preguntasCorrectas
            preguntasIncorrectas -= preguntasIncorrectas        
        print(f"Sus puntaje es {puntajeInicial}")
        print(f"Sus vidas son {vidas}")
        print(f"Sus poderes es {poderes}")
        if (vidas == 0):
            return False
    pregunta10= str(input("10.cuanto es 6+2? \nA.2\nB.1\nC.3\nD.8\n"))
    if(pregunta10 == "d"):
        print("Felicidades esa es la respuesta correcta")
        puntajeInicial += 30
        poder = "convertirse en bestia"
        poderes.append(poder)
        preguntasCorrectas += 1
        print(f"Usted lleva {preguntasCorrectas} respuestas correctas")
        if (preguntasCorrectas == 10):
            print("por cada 10 preguntas respondida de forma correcta le doy 1000 monedas de oro")
            monedasOro += 1000
            preguntasCorrectas -= preguntasCorrectas
        print(f"Por contestar esta pregunta bien le doy 30 puntaje")
        print(f"por contestar esta pregunta bien recibe {poder}")
        print(f"Sus puntaje es {puntajeInicial}")
        print(f"Sus vidas son {vidas}")
        print(f"Sus poderes son {poderes}")
    else:
        print("esa respuesta es incorrecta")
        vidas -= 1
        preguntasIncorrectas += 1
        if preguntasIncorrectas == 1:
            preguntasCorrectas -= preguntasCorrectas
            preguntasIncorrectas -= preguntasIncorrectas   
        print(f"Sus puntaje es {puntajeInicial}")
        print(f"Sus vidas son {vidas}")
        print(f"Sus poderes es {poderes}")
        if (vidas == 0):
            return False
    
    if(puntajeInicial <= 180):
        print("Usted tiene menos de 180 puntos por lo tanto tiene que reiniciar el juego con las mismas vidas que tiene")
        if(reincio10 == 0):
            print(f"Sus puntaje es {puntajeInicial}")
            print(f"Sus vidas son {vidas}")
            print(f"Sus poderes son {poderes}")
            reincio10 += 1
            veintepregunta() 
            return False
        else:
            return False
    pregunta11= str(input("11.cuanto es 9+2? \nA.12\nB.11\nC.13\nD.18\n"))
    if(pregunta11 == "b"):
        print("Felicidades esa es la respuesta correcta")
        puntajeInicial += 50
        poder = "magia"
        poderes.append(poder)
        preguntasCorrectas += 1
        print(f"Usted lleva {preguntasCorrectas} respuestas correctas")
        if (preguntasCorrectas == 10):
            print("por cada 10 preguntas respondida de forma correcta le doy 1000 monedas de oro")
            monedasOro += 1000
            preguntasCorrectas -= preguntasCorrectas
        print(f"Por contestar esta pregunta bien le doy 50 puntaje")
        print(f"por contestar esta pregunta bien recibe {poder}")
        print(f"Sus puntaje es {puntajeInicial}")
        print(f"Sus vidas son {vidas}")
        print(f"Sus poderes son {poderes}")
    else:
        print("esa respuesta es incorrecta")
        vidas -= 1
        preguntasIncorrectas += 1
        if preguntasIncorrectas == 1:
            preguntasCorrectas -= preguntasCorrectas
            preguntasIncorrectas -= preguntasIncorrectas
        print(f"Sus puntaje es {puntajeInicial}")
        print(f"Sus vidas son {vidas}")
        print(f"Sus poderes es {poderes}")
        if (vidas == 0):
            return False
    pregunta12= str(input("12.cuanto es 9+12? \nA.22\nB.21\nC.23\nD.18\n"))
    if(pregunta12 == "b"):
        print("Felicidades esa es la respuesta correcta")
        puntajeInicial += 50
        poder = "ser elastico"
        poderes.append(poder)
        preguntasCorrectas += 1
        print(f"Usted lleva {preguntasCorrectas} respuestas correctas")
        if (preguntasCorrectas == 10):
            print("por cada 10 preguntas respondida de forma correcta le doy 1000 monedas de oro")
            monedasOro += 1000
            preguntasCorrectas -= preguntasCorrectas
        print(f"Por contestar esta pregunta bien le doy 50 puntaje")
        print(f"por contestar esta pregunta bien recibe {poder}")
        print(f"Sus puntaje es {puntajeInicial}")
        print(f"Sus vidas son {vidas}")
        print(f"Sus poderes son {poderes}")
    else:
        print("esa respuesta es incorrecta")
        vidas -= 1
        preguntasIncorrectas += 1
        if preguntasIncorrectas == 1:
            preguntasCorrectas -= preguntasCorrectas
            preguntasIncorrectas -= preguntasIncorrectas
        print(f"Sus puntaje es {puntajeInicial}")
        print(f"Sus vidas son {vidas}")
        print(f"Sus poderes es {poderes}")
        if (vidas == 0):
            return False
    if(puntajeInicial >= 400):
        print("Felicidades ha ganado una vida")
        vidas += 1
        print(f"Su vidas son {vidas}")
    pregunta13= str(input("13.cuanto es 26+12? \nA.38\nB.21\nC.23\nD.28\n"))
    if(pregunta13 == "a"):
        print("Felicidades esa es la respuesta correcta")
        puntajeInicial += 50
        poder = "controlar el metal"
        poderes.append(poder)
        preguntasCorrectas += 1
        print(f"Usted lleva {preguntasCorrectas} respuestas correctas")
        if (preguntasCorrectas == 10):
            print("por cada 10 preguntas respondida de forma correcta le doy 1000 monedas de oro")
            monedasOro += 1000
            preguntasCorrectas -= preguntasCorrectas
        print(f"Por contestar esta pregunta bien le doy 50 puntaje")
        print(f"por contestar esta pregunta bien recibe {poder}")
        print(f"Sus puntaje es {puntajeInicial}")
        print(f"Sus vidas son {vidas}")
        print(f"Sus poderes son {poderes}")
    else:
        print("esa respuesta es incorrecta")
        vidas -= 1
        preguntasIncorrectas += 1
        if preguntasIncorrectas == 1:
            preguntasCorrectas -= preguntasCorrectas
            preguntasIncorrectas -= preguntasIncorrectas
        print(f"Sus puntaje es {puntajeInicial}")
        print(f"Sus vidas son {vidas}")
        print(f"Sus poderes es {poderes}")
        if (vidas == 0):
            return False
    pregunta14= str(input("14.cuanto es 16-3? \nA.2\nB.9\nC.13\nD.8\n"))
    if(pregunta14 == "c"):
        print("Felicidades esa es la respuesta correcta")
        puntajeInicial += 50
        poder = "immortalidad"
        poderes.append(poder)
        preguntasCorrectas += 1
        print(f"Usted lleva {preguntasCorrectas} respuestas correctas")
        if (preguntasCorrectas == 10):
            print("por cada 10 preguntas respondida de forma correcta le doy 1000 monedas de oro")
            monedasOro += 1000
            preguntasCorrectas -= preguntasCorrectas
        print(f"Por contestar esta pregunta bien le doy 50 puntaje")
        print(f"por contestar esta pregunta bien recibe {poder}")
        print(f"Sus puntaje es {puntajeInicial}")
        print(f"Sus vidas son {vidas}")
        print(f"Sus poderes es {poderes}")
    else:
        print("esa respuesta es incorrecta")
        vidas -= 1
        preguntasIncorrectas += 1
        if preguntasIncorrectas == 1:
            preguntasCorrectas -= preguntasCorrectas
            preguntasIncorrectas -= preguntasIncorrectas
        print(f"Sus puntaje es {puntajeInicial}")
        print(f"Sus vidas son {vidas}")
        print(f"Sus poderes es {poderes}")
        if (vidas == 0):
            return False
    pregunta15= str(input("15.cuanto es 16-2? \nA.12\nB.14\nC.13\nD.18\n"))
    if(pregunta15 == "b"):
        print("Felicidades esa es la respuesta correcta")
        puntajeInicial += 50
        poder = "supervelocidad"
        poderes.append(poder)
        preguntasCorrectas += 1
        print(f"Usted lleva {preguntasCorrectas} respuestas correctas")
        if (preguntasCorrectas == 10):
            print("por cada 10 preguntas respondida de forma correcta le doy 1000 monedas de oro")
            monedasOro += 1000
            preguntasCorrectas -= preguntasCorrectas
        print(f"Por contestar esta pregunta bien le doy 50 puntaje")
        print(f"por contestar esta pregunta bien recibe {poder}")
        print(f"Sus puntaje es {puntajeInicial}")
        print(f"Sus vidas son {vidas}")
        print(f"Sus poderes es {poderes}")
    else:
        print("esa respuesta es incorrecta")
        vidas -= 1
        preguntasIncorrectas += 1
        if preguntasIncorrectas == 1:
            preguntasCorrectas -= preguntasCorrectas
            preguntasIncorrectas -= preguntasIncorrectas
        print(f"Sus puntaje es {puntajeInicial}")
        print(f"Sus vidas son {vidas}")
        print(f"Sus poderes es {poderes}")
        if (vidas == 0):
            return False
    pregunta16= str(input("16.cuanto es 9-2? \nA.7\nB.11\nC.13\nD.18\n"))
    if(pregunta16 == "a"):
        print("Felicidades esa es la respuesta correcta")
        puntajeInicial += 50
        poder = "invisibilidad"
        poderes.append(poder)
        preguntasCorrectas += 1
        print(f"Usted lleva {preguntasCorrectas} respuestas correctas")
        if (preguntasCorrectas == 10):
            print("por cada 10 preguntas respondida de forma correcta le doy 1000 monedas de oro")
            monedasOro += 1000
            preguntasCorrectas -= preguntasCorrectas
        print(f"Por contestar esta pregunta bien le doy 50 puntaje")
        print(f"por contestar esta pregunta bien recibe {poder}")
        print(f"Sus puntaje es {puntajeInicial}")
        print(f"Sus vidas son {vidas}")
        print(f"Sus poderes son {poderes}")
    else:
        print("esa respuesta es incorrecta")
        vidas -= 1
        preguntasIncorrectas += 1
        if preguntasIncorrectas == 1:
            preguntasCorrectas -= preguntasCorrectas
            preguntasIncorrectas -= preguntasIncorrectas
        print(f"Sus puntaje es {puntajeInicial}")
        print(f"Sus vidas son {vidas}")
        print(f"Sus poderes son {poderes}")
        if (vidas == 0):
            return False
    pregunta17= str(input("17.cuanto es 9-12? \nA.22\nB.21\nC.3\nD.18\n"))
    if(pregunta17 == "c"):
        print("Felicidades esa es la respuesta correcta")
        puntajeInicial += 50
        poder = "lanzar telarañas"
        poderes.append(poder)
        preguntasCorrectas += 1
        print(f"Usted lleva {preguntasCorrectas} respuestas correctas")
        if (preguntasCorrectas == 10):
            print("por cada 10 preguntas respondida de forma correcta le doy 1000 monedas de oro")
            monedasOro += 1000
            preguntasCorrectas -= preguntasCorrectas
        print(f"Por contestar esta pregunta bien le doy 50 puntaje")
        print(f"por contestar esta pregunta bien recibe {poder}")
        print(f"Sus puntaje es {puntajeInicial}")
        print(f"Sus vidas son {vidas}")
        print(f"Sus poderes son {poderes}")
    else:
        print("esa respuesta es incorrecta")
        vidas -= 1
        preguntasIncorrectas += 1
        if preguntasIncorrectas == 1:
            preguntasCorrectas -= preguntasCorrectas
            preguntasIncorrectas -= preguntasIncorrectas
        print(f"Sus puntaje es {puntajeInicial}")
        print(f"Sus vidas son {vidas}")
        print(f"Sus poderes son {poderes}")
        if (vidas == 0):
            return False
    pregunta18= str(input("18.cuanto es 9+2? \nA.7\nB.11\nC.13\nD.18\n"))
    if(pregunta18 == "b"):
        print("Felicidades esa es la respuesta correcta")
        puntajeInicial += 50
        poder = "super inteligencia"
        poderes.append(poder)
        preguntasCorrectas += 1
        print(f"Usted lleva {preguntasCorrectas} respuestas correctas")
        if (preguntasCorrectas == 10):
            print("por cada 10 preguntas respondida de forma correcta le doy 1000 monedas de oro")
            monedasOro += 1000
            preguntasCorrectas -= preguntasCorrectas
        print(f"Por contestar esta pregunta bien le doy 50 puntaje")
        print(f"por contestar esta pregunta bien recibe {poder}")
        print(f"Sus puntaje es {puntajeInicial}")
        print(f"Sus vidas son {vidas}")
        print(f"Sus poderes son {poderes}")
    else:
        print("esa respuesta es incorrecta")
        vidas -= 1
        preguntasIncorrectas += 1
        if preguntasIncorrectas == 1:
            preguntasCorrectas -= preguntasCorrectas
            preguntasIncorrectas -= preguntasIncorrectas
        print(f"Sus puntaje es {puntajeInicial}")
        print(f"Sus vidas son {vidas}")
        print(f"Sus poderes son {poderes}")
        if (vidas == 0):
            return False
    pregunta19= str(input("19.cuanto es 9+9? \nA.7\nB.11\nC.13\nD.18\n"))
    if(pregunta19 == "d"):
        print("Felicidades esa es la respuesta correcta")
        puntajeInicial += 50
        poder = "supertraje"
        poderes.append(poder)
        preguntasCorrectas += 1
        print(f"Usted lleva {preguntasCorrectas} respuestas correctas")
        if (preguntasCorrectas == 10):
            print("por cada 10 preguntas respondida de forma correcta le doy 1000 monedas de oro")
            monedasOro += 1000
            preguntasCorrectas -= preguntasCorrectas
        print(f"Por contestar esta pregunta bien le doy 50 puntaje")
        print(f"por contestar esta pregunta bien recibe {poder}")
        print(f"Sus puntaje es {puntajeInicial}")
        print(f"Sus vidas son {vidas}")
        print(f"Sus poderes son {poderes}")
    else:
        print("esa respuesta es incorrecta")
        vidas -= 1
        preguntasIncorrectas += 1
        if preguntasIncorrectas == 1:
            preguntasCorrectas -= preguntasCorrectas
            preguntasIncorrectas -= preguntasIncorrectas
        print(f"Sus puntaje es {puntajeInicial}")
        print(f"Sus vidas son {vidas}")
        print(f"Sus poderes son {poderes}")
        if (vidas == 0):
            return False
    pregunta20= str(input("20.cuanto es 9+12? \nA.22\nB.21\nC.3\nD.18\n"))
    if(pregunta20 == "b"):
        print("Felicidades esa es la respuesta correcta")
        puntajeInicial += 50
        poder = "trepar paredes"
        poderes.append(poder)
        preguntasCorrectas += 1
        print(f"Usted lleva {preguntasCorrectas} respuestas correctas")
        if (preguntasCorrectas == 10):
            print("por cada 10 preguntas respondida de forma correcta le doy 1000 monedas de oro")
            monedasOro += 1000
            preguntasCorrectas -= preguntasCorrectas
        print(f"Por contestar esta pregunta bien le doy 50 puntaje")
        print(f"por contestar esta pregunta bien recibe {poder}")
        print(f"Su puntaje es {puntajeInicial}")
        print(f"Su vidas son {vidas}")
        print(f"Su poderes es {poderes}")
        if(puntajeInicial >= 800 and vidas == 6):
            print("ha terminado perfecto")
            print("Felicidades consigio el premio maximo")
            print(f"Sus puntaje es {puntajeInicial}")
            print(f"Sus vidas son {vidas}")
            print(f"Sus poderes es {poderes}")
            print(f"Sus monedas de oro son {monedasOro}")
            return False
        else:
            if(puntajeInicial > 600):
                print("ha terminado el juego")
                print("Felicidades cesto es lo que ha consegido")
                print(f"Sus puntaje es {puntajeInicial}")
                print(f"Sus vidas son {vidas}")
                print(f"Sus poderes es {poderes}")
                print(f"Sus monedas de oro son {monedasOro}")
                return False
            elif(puntajeInicial < 600):
                print("Desea volver a inciar la aventura no obtendra el puntaje absoluto")
                print("Si eligue si volveras a inciar si no se le restaran 10 poderes ")
                opcion1 = str(input("puede eleguir si o no"))
                if(opcion1 == "si"):
                    print("Volvera a inciar el juego y le otorgare una vida")
                    vidas += 1
                    print(f"Sus vidas son {vidas}")
                    veintepregunta()
                elif(opcion1 == "no"):
                    for i in range(0, 10):
                        poderes.pop()
                    print(f"Su puntaje es {puntajeInicial}")
                    print(f"Su vidas son {vidas}")
                    print(f"Su poderes es {poderes}")
                    print(f"Sus monedas de oro son {monedasOro}")
                    return False

    else:
        print("esa respuesta es incorrecta")
        vidas -= 1
        preguntasIncorrectas += 1
        if preguntasIncorrectas == 1:
            preguntasCorrectas -= preguntasCorrectas
            preguntasIncorrectas -= preguntasIncorrectas
        print(f"Su puntaje es {puntajeInicial}")
        print(f"Su vidas son {vidas}")
        print(f"Su poderes es {poderes}")
        if (vidas == 0):
            return False
        if(puntajeInicial > 600):
            print("ha terminado el juego")
            print("Felicidades cesto es lo que ha consegido")
            print(f"Sus puntaje es {puntajeInicial}")
            print(f"Sus vidas son {vidas}")
            print(f"Sus poderes es {poderes}")
            print(f"Sus monedas de oro son {monedasOro}")
            return False
        elif(puntajeInicial < 600):
            print("Desea volver a inciar la aventura no obtendra el puntaje absoluto")
            print("Si eligue si volvera a inciat si no se le restaran 10 poderes ")
            opcion1 = str(input("puede eleguir si o no"))
            if(opcion1 == "si"):
                print("Volvera a inciar el juego y le otorgare una vida")
                vidas += 1
                print(f"Sus vidas son {vidas}")
                veintepregunta()
            elif(opcion1 == "no"):
                for i in range(0, 10):
                    poderes.pop()
                print(f"Su puntaje es {puntajeInicial}")
                print(f"Su vidas son {vidas}")
                print(f"Su poderes es {poderes}")
                print(f"Sus monedas de oro son {monedasOro}")
                return False
   
        
veintepregunta()