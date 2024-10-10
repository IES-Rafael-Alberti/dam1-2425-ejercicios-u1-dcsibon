#
# Ejercicio 7
# Escribe un programa que solicite tres números al usuario y calcule e imprima por pantalla su suma.
#
# EXTRA: Para los Ejercicios 1.5 al 1.10, se deben usar tipos de datos float y mostrar los resultados con 2 posiciones decimales.
#


num1 = float(input("Dame un número: "))
num2 = float(input("Dame otro: "))
num3 = float(input("Dame un tercer número: "))

print("La suma de los 3 números es {:.2f}€.".format(num1 + num2 + num3))

