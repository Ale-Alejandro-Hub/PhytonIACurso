#Calculadora con menu

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply (a, b):
    return a * b

def divide(a, b):
    if b !=0:
        return a / b
    else:
        return"Las diviciones por Cero no estan permitidas" 
    

while True:
    print("\nMenu:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")
    
    eleccion = input("Ingresa tu Elección: ")
    
    if eleccion == "5":
        print("Saliendo del programa,")
        break
    
    num1 = int(input("Ingresa primer numero: "))
    num2 = int(input("Ingresa segundo numero: "))
    
    if eleccion == "1":
        print ("Resultado", add(num1, num2) )
    
    elif eleccion == "2":
        print ("Resultado", subtract(num1, num2) )
        
    elif eleccion == "3":
        print ("Resultado", multiply(num1, num2) )
        
    elif eleccion == "4":
        print ("Resultado", divide(num1, num2) )
    
    else:
        print("Eleccion no valida. Intentalo denuevo")
        