""" 
Mi programa consta de dos funciones. Una es medir con estrellas la satisfaccion de los usuario de una tienda de videojuegos
por medio de una encuesta. Otra es saber si el usuario quiere dejar una queja para poder mejorar el servicio.
"""
#importar
from time import sleep
#diccionarios
diccionario = {
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
def promedio (p_1, p_2, p_3, p_4, p_5):
    prom = (p_1 + p_2 + p_3 + p_4 + p_5)/5
    return prom
#Código
res1 = "si"
while res1 == "si":
    sleep (0.5)
    print ("¿Quiere responder nuestra encuesta de satisfaccion?")
    sleep (0.5)
    res1 = input("Introduzca su respuesta: |si| - |no| ==> ")
    if res1 == "no":
        sleep (0.5)
        print ("Gracias por su tiempo")
    else:
        sleep (0.5)
        print ("¿Le gustaría poner una queja?")
        sleep (0.5)
        res2 = input("Introduzca su respuesta: |si| - |no| ==> ")
        if res2 == "si":
            sleep (0.5)
            print ("¿Sobre que se quisiera quejar?")
            sleep (0.5)
            res3 = input ("|servicio| - |productos| - |establecimiento| - |empleados| - |precios| ==> ")
            if res3 == "servicio":
                sleep (0.5)
                print (diccionario["Quejas"][1])
                sleep (0.5)
                resQ = input("Escriba su respuesta: ")
                print (f"Su respuesta fue: {resQ}")
            elif res3 == "productos":
                sleep (0.5)
                print (diccionario["Quejas"][2])
                sleep (0.5)
                resQ = input("Escriba su respuesta: ")
                print (f"Su respuesta fue: {resQ}")
            elif res3 == "establecimiento":
                sleep (0.5)
                print (diccionario["Quejas"][3])
                sleep (0.5)
                resQ = input("Escriba su respuesta: ")
                print (f"Su respuesta fue: {resQ}")
            elif res3 == "empleados":
                sleep (0.5)
                print (diccionario["Quejas"][4])
                sleep (0.5)
                resQ = input("Escriba su respuesta: ")
                print (f"Su respuesta fue: {resQ}")
            elif res3 == "precios":
                sleep (0.5)
                print (diccionario["Quejas"][5])
                sleep (0.5)
                res_q = input("Escriba su respuesta: ")
                print (f"Su respuesta fue: {res_q}")
        else:
            sleep (0.5)
            print ("Califique las siguientes preguntas usando numeros:")
            sleep (0.5)
            print (diccionario["Preguntas"][1])
            res_1 = int(input())
            sleep (0.5)
            print (diccionario["Preguntas"][2])
            res_2 = int(input())
            sleep (0.5)
            print (diccionario["Preguntas"][3])
            res_3 = int(input())
            sleep (0.5)
            print (diccionario["Preguntas"][4])
            res_4 = int(input())
            sleep (0.5)
            print (diccionario["Preguntas"][5])
            res_5 = int(input())
            sleep (0.5)
            print ("Su promedio fue:")
            sleep (0.5)
            print (promedio(res_1,res_2,res_3,res_4,res_5))