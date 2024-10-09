
import math


def area_triangulo(a, b, c):
    # Semiperímetro
    s = (a + b + c) / 2

    # Fórmula de Herón
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area


def main():

    print("Introduce el valor de los tres lados del triángulo...")
    a, b, c = int(input("Lado 1: ")), int(input("Lado 2: ")), int(input("Lado 3: "))
    print(f"El área del triángulo es: {area_triangulo(a, b, c):.2f}")



if __name__ == "__main__":
    main()
