#
# Ejercicio 8
# Escribir el programa del ejercicio 1.7 usando solamente dos variables diferentes.
#
# EXTRA: Para los Ejercicios 1.5 al 1.10, se deben usar tipos de datos float y mostrar los resultados con 2 posiciones decimales.
#


num = float(input("Dame un número: "))
suma = num
num = float(input("Dame otro: "))
suma += num
num = float(input("Dame un tercer número: "))
suma += num

print("La suma de los 3 números es {:.2f}€.".format(suma))
