#
# Ejercicio 4
# Escribe un programa que le pida al usuario una temperatura en grados Celsius, la convierta a 
# grados Fahrenheit e imprima por pantalla la temperatura convertida.
#
# EXTRA1: Formatear la salida de los grados Farenheit a dos posiciones decimales
# EXTRA2: Mostrar en pantalla "La temperatura en grados Farenheit es 0.00ºF (0.00ºC)"
#

celsius = float(input("Introduzca la temperatura en grados Celsius: "))
farenheit = (celsius * 9 / 5) + 32

print("La temperatura en grados Farenheit es {:.2f}ºF ({:.2f}ºC)".format(farenheit, celsius))
