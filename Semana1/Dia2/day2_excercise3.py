#Encontrar el numero mas grande en una lista

numeros = [10, 754, 827585]

mayor = numeros[0]

for num in numeros:
    if num > mayor:
        mayor = num

print("El número mayor es:", mayor)


# mayor = numeros[0] → empezamos suponiendo que el primero es el mayor
# for num in numeros → recorremos toda la lista
# if num > mayor → comparamos
# mayor = num → actualizamos


numeros = [10, 754, 827585]

menor = numeros[0]

for num in numeros:
    if num < menor:
        menor = num

print("El número menor es:", menor)

#Aqui realice lo mismo la diferencia es que declare lo que queria realizar, es decir
#Buscar el el menor es por eso que declare "menor" asi como arriba queria buscar
#"mayor" y la declare