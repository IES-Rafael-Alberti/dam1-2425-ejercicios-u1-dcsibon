#
# Ejercicio 17
# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla 
# en líneas distintas el nombre del usuario tantas veces como el número introducido.
#


nombre = input("Introduce tu nombre: ")
veces = int(input("Introduce un número: "))

print((nombre + '\n') * veces)