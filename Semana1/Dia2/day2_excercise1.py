#Encuentra el numero primo
#un numero primo solo es dividible por 1 y por si mismo
#Usar un bucle para numeros divisibles entre 2 y la raiz cuadrada del numero dado, y romper el bucle si se encuentra un divisor

num = int(input("Ingresa un numero "))

if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} no es primo")
            break
    else:
        print(f"{num} es primo")
else:
    print(f"{num} no es un numero primo")