
def fibonacci(hasta):
    num1 = 0  # Primer número de Fibonacci
    num2 = 1  # Segundo número de Fibonacci

    serie = "0 1"
    suma = 0

    while suma <= hasta:
        suma = num1 + num2
        num1 = num2
        num2 = suma
        if suma <= hasta:
            serie += " " + str(suma)

    return serie


def main():
    num_fin = int(input("Introduzca el número final de la serie Fibonacci: "))
    print(fibonacci(num_fin))



if __name__ == "__main__":
    main()