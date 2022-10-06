""" 
Mi programa consta de dos funciones. Una es medir con estrellas la satisfaccion de los usuario de una tienda de videojuegos
por medio de una encuesta. Otra es saber si el usuario quiere dejar una queja para poder mejorar el servicio.
"""
#importar
from time import sleep
#diccionarios
Diccionario = {
    "Preguntas" : {
        1:"¿Cómo calificaría la atención de los empleados?",
        2:"¿Cómo calificaría la calidad de nuestros productos?",
        3:"¿Cómo calificaría los precios de los productos?",
        4:"¿Cómo calificaría nuestros servicios?",
        5:"¿Cómo calificaría la condición del establecimiento?"
    },
    "Quejas" : {
        1:"¿Qué es lo que no le gusto de nuestro servicio?",
        2:"¿Qué es lo que no le gusto de nuestros productos?",
        3:"¿Qué es lo que no le gusto de nuestro establecimiento?",
        4:"¿Qué es lo que no le gusto de nuestros empleados?",
        5:"¿Qué es lo que no le gusto de nuestros precios?"
    }
    }
#Funciones
def promedio (P_1, P_2, P_3, P_4, P_5):
    prom = (P_1 + P_2 + P_3 + P_4 + P_5)/5
    return prom
#Código
Res1 = "si"
while Res1 == "si":
    sleep (0.5)
    print ("¿Quiere responder nuestra encuesta de satisfaccion?")
    sleep (0.5)
    Res1 = input("Introduzca su respuesta: |si| - |no| ==> ")
    if Res1 == "no":
        sleep (0.5)
        print ("Gracias por su tiempo")
    else:
        sleep (0.5)
        print ("¿Le gustaría poner una queja?")
        sleep (0.5)
        Res2 = input("Introduzca su respuesta: |si| - |no| ==> ")
        if Res2 == "si":
            sleep (0.5)
            print ("¿Sobre que se quisiera quejar?")
            sleep (0.5)
            Res3 = input ("|servicio| - |productos| - |establecimiento| - |empleados| - |precios| ==> ")
            if Res3 == "servicio":
                sleep (0.5)
                print (Diccionario["Quejas"][1])
                sleep (0.5)
                resQ = input("Escriba su respuesta: ")
                print (f"Su respuesta fue: {resQ}")
            elif Res3 == "productos":
                sleep (0.5)
                print (Diccionario["Quejas"][2])
                sleep (0.5)
                resQ = input("Escriba su respuesta: ")
                print (f"Su respuesta fue: {resQ}")
            elif Res3 == "establecimiento":
                sleep (0.5)
                print (Diccionario["Quejas"][3])
                sleep (0.5)
                resQ = input("Escriba su respuesta: ")
                print (f"Su respuesta fue: {resQ}")
            elif Res3 == "empleados":
                sleep (0.5)
                print (Diccionario["Quejas"][4])
                sleep (0.5)
                resQ = input("Escriba su respuesta: ")
                print (f"Su respuesta fue: {resQ}")
            elif Res3 == "precios":
                sleep (0.5)
                print (Diccionario["Quejas"][5])
                sleep (0.5)
                resQ = input("Escriba su respuesta: ")
                print (f"Su respuesta fue: {resQ}")
        else:
            sleep (0.5)
            print ("Califique las siguientes preguntas usando numeros:")
            sleep (0.5)
            print (Diccionario["Preguntas"][1])
            res_1 = int(input())
            sleep (0.5)
            print (Diccionario["Preguntas"][2])
            res_2 = int(input())
            sleep (0.5)
            print (Diccionario["Preguntas"][3])
            res_3 = int(input())
            sleep (0.5)
            print (Diccionario["Preguntas"][4])
            res_4 = int(input())
            sleep (0.5)
            print (Diccionario["Preguntas"][5])
            res_5 = int(input())
            sleep (0.5)
            print ("Su promedio fue:")
            sleep (0.5)
            print (promedio(res_1,res_2,res_3,res_4,res_5))