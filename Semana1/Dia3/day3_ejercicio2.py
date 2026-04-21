# #importar modulos de operaciones_matematicas.py basicas

import operaciones_matematicas as op
num1 = 10
num2 = 5

print ("suma:", op.sumar(num1,num2))
print ("resta:", op.restar(num1,num2))
print ("multiplicar:",op.multiplicar(num1,num2))
print ("dividir:", op.dividir(num1,num2))


#ejercicio crear modulo para operaciones con cadenas,incluyendo funciones para invertir cadena contar las vocales, y verificar palindromos, importar en un script y probar funciones
def invertir_cadena(cadena):
    return cadena[::-1]

def contar_vocales(cadena):
    vocales = "aeiouAEIOU"
    contador = 0
    for char in cadena:
        if char in vocales:
            contador += 1
    return contador

def es_palindromo(cadena):
    cadena = cadena.replace(" ", "").lower()
    return cadena == cadena[::-1]
#Estas lineas estan comentadas para evitar que se ejecuten al importar el modulo, pero se pueden descomentar para probar las funciones directamente en este script
# print(invertir_cadena("Hola Mundo"))
# print(contar_vocales("aeiouAEIOU"))
# print(es_palindromo("Anita lava la tina"))


#ejercicio Crear para verificar si el numero es par o impar llamar la dentro de otra funcion
# def es_par(num):
#     return num % 2 == 0

# def es_impar(num):
#     return num %2 !=0

# def verificar_paridad(num):
#     if es_par(num):
#         print(f"{num} es un numero par")
#     elif es_impar(num):
#         print( f"{num} es un numero impar")
#     else:
#         print("Error: no es un numero Valido")

# verificar_paridad(10)
# verificar_paridad(7)


