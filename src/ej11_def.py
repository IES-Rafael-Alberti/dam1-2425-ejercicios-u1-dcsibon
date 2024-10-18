#
# Ejercicio 11
# Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla 
# la suma de todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada 
# de la siguiente forma: suma = n (n+1)/2
#

def suma_numeros(num):
    suma = int(num * (num + 1) / 2)
    return "La suma de los números del 1 al " + str(num) + " es " + str(suma) + "."


def main():
    num = int(input("Dame un número: "))
    print(suma_numeros(num))


if __name__ == "__main__":
    main()