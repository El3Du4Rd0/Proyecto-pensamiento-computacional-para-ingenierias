""" 
Mi programa consta de dos funciones. Una es medir con estrellas la satisfaccion de los usuario de una tienda de videojuegos
por medio de una encuesta. Otra es saber si el usuario quiere dejar una queja para poder mejorar el servicio.
"""
#importar
from time import sleep
#diccionarios
Dicc_Preguntas = {
    "primera":"¿Cómo calificaría la atención de los empleados?",
    "segunda":"¿Cómo calificaría la calidad de nuestros productos?",
    "tercera":"¿Cómo calificaría los precios de los productos?",
    "cuarta":"¿Cómo calificaría nuestros servicios?",
    "quinta":"¿Cómo calificaría la condición del establecimiento?"
}
Dicc_Quejas = {
    "primera":"¿Qué es lo que no le gusto de nuestro servicio?",
    "segunda":"¿Qué es lo que no le gusto de nuestros productos?",
    "tercera":"¿Qué es lo que no le gusto de nuestro establecimiento?",
    "cuarta":"¿Qué es lo que no le gusto de nuestros empleados?",
    "quinta":"¿Qué es lo que no le gusto de nuestros precios?"
}
#Funciones
def promedio (P_1, P_2, P_3, P_4, P_5):
    prom = (P_1 + P_2 + P_3 + P_4 + P_5)/5
    return prom
#Código
Res1 = "si"
while Res1 == "si":
    print ("¿Quiere responder nuestra encuesta de satisfaccion?")
    Res1 = input("Introduzca su respuesta: |si| - |no| ==> ")
    if Res1 == "no":
        print ("Gracias por su tiempo")
    else:
        print ("¿Le gustaría poner una queja?")
        Res2 = input("Introduzca su respuesta: |si| - |no| ==> ")
        if Res2 == "si":
            print ("¿Sobre que se quisiera quejar?")
            Res3 = input ("|servicio| - |productos| - |establecimiento| - |empleados| - |precios| ==> ")
            if Res3 == "servicio":
                print (Dicc_Quejas["primera"])
                resQ = input()
            elif Res3 == "productos":
                print (Dicc_Quejas["segunda"])
                resQ = input()
            elif Res3 == "establecimiento":
                print (Dicc_Quejas["tercera"])
                resQ = input()
            elif Res3 == "empleados":
                print (Dicc_Quejas["cuarta"])
                resQ = input()
            elif Res3 == "precios":
                print (Dicc_Quejas["quinta"])
                resQ = input()
        else:
            print ("Califique las siguientes preguntas:")
            print (Dicc_Preguntas["primera"])
            res_1 = int(input())
            print (Dicc_Preguntas["segunda"])
            res_2 = int(input())
            print (Dicc_Preguntas["tercera"])
            res_3 = int(input())
            print (Dicc_Preguntas["cuarta"])
            res_4 = int(input())
            print (Dicc_Preguntas["quinta"])
            res_5 = int(input())
            print ("Su promedio fue:")
            print (promedio(res_1,res_2,res_3,res_4,res_5))