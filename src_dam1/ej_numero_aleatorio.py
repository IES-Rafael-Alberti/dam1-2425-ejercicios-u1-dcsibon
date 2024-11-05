import random


def dame_un_numero_aleatorio():
    return random.randint(min, max)


def main():
    min = int(input("Dame el mínimo: "))
    max = int(input("Dame el máximo: "))

    num_aleatorio = dame_un_numero_aleatorio(min, max)


if __name__ == "__main__":
    main()