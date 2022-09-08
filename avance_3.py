""" 
Mi programa consta de dos funciones. Una es medir con estrellas la satisfaccion de los usuario de una tienda de videojuegos
por medio de una encuesta. Otra es saber si el usuario quiere dejar una queja para poder mejorar el servicio.
"""
# Importar
import time
# Funciones
def pedir_estrellas():
    print ("Califique las siguientes preguntas con 1 a 5 estrellas.")
    time.sleep (1)
    print ("¿Cómo calificaría la atención de los empleados?")
    estrellas_1 = int(input())
    time.sleep (0.5)
    print ("¿Cómo calificaría la calidad de nuestros productos?")
    estrellas_2 = int (input())
    time.sleep (0.5)
    print ("¿Cómo calificaría los precios de los productos?")
    estrellas_3 = int (input())
    time.sleep (0.5)
    print ("¿Cómo calificaría las medidas sanitarias del establecimiento?")
    estrellas_4 = int (input())
    time.sleep (0.5)
    print ("¿Cómo calificaría la condición del establecimiento?")
    estrellas_5 = int (input())
    time.sleep (0.5)
    print ("Gracias por su preferencia.")
    global promedio_E
    promedio_E = ((estrellas_1 + estrellas_2 + estrellas_3 + estrellas_4 + estrellas_5)/5)
    print (f"Su promedio de estrellas es: {promedio_E}")
def pedir_quejas():
    global opcion_quejas
    print ("¿Qué es lo que no le gusto de nuestro servicio?")
    time.sleep (1)
    print ("1. Los empleados.")
    time.sleep (0.5)
    print ("2. Estado del establecimiento.")
    time.sleep (0.5)
    print ("3. Calidad de nuestros productos.")
    time.sleep (1)
    opcion_quejas = input ("Seleccione su opcion colocando un numero: ")
    print ("Gracias por su preferencia. Mejoraremos el servicio.")
#Código
print ("1.Calificar el servicio 2.Poner una queja")
time.sleep (0.5)
opcion_menu = int(input("Seleccione que opcion quiere escoger: "))

if (opcion_menu == 1):
    pedir_estrellas ()
elif (opcion_menu == 2):
    pedir_quejas ()