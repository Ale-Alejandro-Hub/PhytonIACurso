#Ejercicio crear funcion para calcular factoriales
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
def print_factorial(n):
    resultado =  factorial(n)
    print(f"El factorial de {n} es: {resultado}")
    
print_factorial(7)

#Ejetcicio 2 construir un modulo de python con funciones matematicas basicas para usarlo en otro script