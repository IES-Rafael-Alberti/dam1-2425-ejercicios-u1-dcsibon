import random


def numero_aleatorio(min_val, max_val):
    return random.randint(min_val, max_val)


def main():
    min_val, max_val = int(input("Límite inferior: ")), int(input("Límite superior: "))
    print(f"Un número aleatorio entre {min_val} y {max_val} es el {numero_aleatorio(min_val, max_val)}.")



if __name__ == "__main__":
    main()
