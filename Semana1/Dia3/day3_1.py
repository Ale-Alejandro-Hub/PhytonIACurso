#Funciones, Alcance de Variables y Modulos
import math #Importamos el modulo math para usar sus funciones matematicas
print(math.sqrt(16))

import math as m #Importamos el modulo math con un alias m para usar sus funciones matematicas esto es por si el nombre del modulo es muy largo o para evitar conflictos con otros modulos
print(m.sqrt(16))

from math import sqrt #Importamos solo la funcion sqrt del modulo math
print(sqrt(16))






# #Alcance Local

# def greet():
#     mensaje = "Hola desde la función"
#     print(mensaje)
    
# greet()

# #Alcance Global creamos la variable, fuera de la función, por lo tanto es global

# saludo ="HOLA"

# def di_hola():
#     print(saludo + " Desde la función")
    
# di_hola()
# print(saludo + " Desde Fuera de la función")

#Funcion con parametros y valor de retorno

# def sumar_numeros(a,b):
#     #c= a + b
#     return a + b

# resultado = sumar_numeros(5,10)
# print("La suma es:", resultado)

#Importar y usar Modulos


