

def es_mayor(num1, num2):
    """
    Comprueba cual es el número mayor y lo retorna o 0 si son iguales

    Args:
        num1 (int): Primer número entero a comprobar.
        num2 (int): Segundo número entero a comprobar.

    Returns:
        int: Número mayor o 0 si son iguales.
    """
    if num1 == num2:
        return 0
    else:
        return max(num1, num2)
    

def introduce_entero(msj: str) -> int:
    """
    Solicita la introducción de un entero mostrando un mensaje.

    Args:
        msj (str): Mensaje a mostrar en el input().

    Returns:
        int: Número entero convertido desde la entrada del usuario.
    """
    while True:
        valor = input(msj).strip()
        if valor.isdigit() or (valor.startswith("-") and valor[1:].isdigit()):
            return int(valor)
        else:
            print(f"**ERROR** \'{valor}\' no es un número entero válido!")


def main():
    num1 = introduce_entero("Introduzca un número: ")
    num2 = introduce_entero("Introduzca otro número: ")
    numero_mayor = es_mayor(num1, num2)
    print("Los números son iguales " if numero_mayor == 0 else f"El número mayor es el {numero_mayor}")


if __name__ == "__main__":
    main()