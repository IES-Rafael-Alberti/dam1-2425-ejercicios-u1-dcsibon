import math

def es_primo(numero):
    """
    Si un número no es primo, tendrá un divisor entero que será menor o igual a su raíz cuadrada y mayor que 1.
    """
    if numero < 2:
        return False

    for i in range(2, int(math.sqrt(numero)) + 1):  # Usamos math.sqrt() para la raíz cuadrada
        if numero % i == 0:
            return False

    return True


def main():
    numero = int(input("Introduzca un número: "))
    print(f"El número {numero} {'SI es primo' if es_primo(numero) else 'NO es primo'}.")



if __name__ == "__main__":
    main()