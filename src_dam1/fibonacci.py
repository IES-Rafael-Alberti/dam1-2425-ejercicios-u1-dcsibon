# 0 1 1 2 3 5 8 13 21 34 ...


def fibonacci(maximo: int) -> str:
    if maximo < 1:
        return "0"

    num1 = 0
    num2 = 1
    serie = "0 1"

    while (num2 <= maximo):
        resultado = num1 + num2

        if resultado <= maximo:
            serie += " " + str(resultado)

        num1 = num2
        num2 = resultado

    return serie


def main():
    numero = int(input("Introduzca el máximo: "))
    print("La serie es " + fibonacci(numero))


if __name__ == "__main__":
    main()