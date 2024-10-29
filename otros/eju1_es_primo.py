import math

def es_primo_basico(numero):
    """
    Si un número no es primo, tendrá un divisor entero que será menor o igual a su raíz cuadrada y mayor que 1.
    """
    if numero < 2:
        return False
    
    cont_divisores = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            cont_divisores += 1

    if cont_divisores > 2:
        return False
    else:
        return True

def es_primo_basico2(numero):
    """
    Si un número no es primo, tendrá un divisor entero que será menor o igual a su raíz cuadrada y mayor que 1.
    """
    if numero < 2:
        return False
    
    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True

def es_primo_optimizado1(numero):
    """
    Si un número no es primo, tendrá un divisor entero que será menor o igual a su raíz cuadrada y mayor que 1.
    """

    if numero < 2:
        return False

    for i in range(2, int(math.sqrt(numero)) + 1):  # Usamos math.sqrt() para la raíz cuadrada
        if numero % i == 0:
            return False

    return True

def es_primo_optimizado(numero):
    """Comprueba si un número es primo.

    Args:
        numero (int): Número a comprobar.

    Returns:
        bool: True si el número es primo, False en caso contrario.
    """
    if numero <= 1:
        return False
    if numero == 2:  # 2 es el único número par que es primo
        return True
    if numero % 2 == 0:  # Todos los números pares mayores que 2 no son primos
        return False

    # Solo revisamos los números impares hasta la raíz cuadrada del número para mayor eficiencia
    # Los números pares no son números primos ninguno, ya lo hemos comprobado en el "if" anterior
    for i in range(3, int(math.sqrt(numero)) + 1, 2):
        if numero % i == 0:
            return False

    return True


def main():
    numero = int(input("Introduzca un número: "))
    print(f"El número {numero} {'SI es primo' if es_primo(numero) else 'NO es primo'}.")



if __name__ == "__main__":
    main()
