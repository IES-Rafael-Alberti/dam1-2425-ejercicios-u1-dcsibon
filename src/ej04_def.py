#
# Ejercicio 4
# Escribe un programa que le pida al usuario una temperatura en grados Celsius, la convierta a 
# grados Fahrenheit e imprima por pantalla la temperatura convertida.
#
# EXTRA1: Formatear la salida de los grados Farenheit a dos posiciones decimales
# EXTRA2: Mostrar en pantalla "La temperatura en grados Farenheit es 0.00ºF (0.00ºC)"
#


def grados_celsius():
    farenheit = float(input("Introduzca la temperatura en grados Farenheit: "))
    celsius = (farenheit - 32) * (5 / 9)
    return "{:.2f}ºC ({:.2f}ºF)".format(celsius, farenheit)


def main():
    print("La temperatura en grados Celsius es " + grados_celsius())


if __name__ == "__main__":
    main()

