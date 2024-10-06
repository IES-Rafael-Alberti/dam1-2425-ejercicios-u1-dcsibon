import os


def limpiar_pantalla():
    # Si el sistema es Windows
    if os.name == 'nt':
        os.system('cls')
    # Si el sistema es Linux o macOS
    else:
        os.system('clear')


def comprobar_entero(valor: str) -> bool:
    """
    Comprueba si una cadena de caracteres es un número entero.
    """
    return valor.isdigit() or (valor.startswith("-") and valor[1:].isdigit())


def comprobar_entero_positivo(valor: str) -> bool:
    """
    Comprueba si una cadena de caracteres es un número entero positivo.
    """
    return valor.isdigit()


def es_hexadecimal(valor: str) -> bool:
    """
    Comprueba si una cadena de caracteres es un número en base hexadecimal.
    """
    if valor.startswith("-"):
        valor = valor[1:]
    for i in range(len(valor)):
        if valor_posicion(valor[i]) == -1:
            return False
    return True


def es_decimal(valor: str) -> bool:
    """
    Comprueba si una cadena de caracteres es un número en base decimal.
    """
    return comprobar_entero(valor)


def es_octal(valor: str) -> bool:
    """
    Comprueba si una cadena de caracteres es un número en base octal.
    """
    if valor.startswith("-"):
        valor = valor[1:]

    for i in range(len(valor)):
        valor_numerico = valor_posicion(valor[i])
        if valor_numerico > 7 or valor_numerico == -1:
            return False
    return True


def es_binario(valor: str) -> bool:
    """
    Comprueba si una cadena de caracteres es un número en base binaria.
    """
    if valor.startswith("-"):
        valor = valor[1:]

    for i in range(len(valor)):
        valor_numerico = valor_posicion(valor[i])
        if valor_numerico > 1 or valor_numerico == -1:
            return False
    return True


def comprobar_valor_base(valor: str, base) -> bool:
    """
    Comprueba si una cadena de caracteres es un número en base binaria, octal, decimal o hexadecimal.
    """
    if base == 2:
        return es_binario(valor)
    elif base == 8:
        return es_octal(valor)
    elif base == 10:
        return es_decimal(valor)
    else:
        return es_hexadecimal(valor)


def calcular_resto(valor: int) -> str:
    """
    Retorna una cadena de caracteres de una sola posición con el dígito de su posición.
    """
    if valor < 10:
        resto = str(valor)
    elif valor == 10:
        resto = 'A'
    elif valor == 11:
        resto = 'B'
    elif valor == 12:
        resto = 'C'
    elif valor == 13:
        resto = 'D'
    elif valor == 14:
        resto = 'E'
    elif valor == 15:
        resto = 'F'
    else:
        resto = ''

    return resto


def valor_posicion(posicion: str) -> int:
    """
    Retorna un número entero con el valor decimal de una posición de un número de cualquier base.
    """
    if posicion.isdigit():
        resultado = int(posicion)
    elif posicion == 'A':
        resultado = 10
    elif posicion == 'B':
        resultado = 11
    elif posicion == 'C':
        resultado = 12
    elif posicion == 'D':
        resultado = 13
    elif posicion == 'E':
        resultado = 14
    elif posicion == 'F':
        resultado = 15
    else:
        resultado = -1

    return resultado


def convertir_decimal_a_otra_base(valor: str, base: int) -> str:
    """
    Convierte un número decimal a un número con una base concreta.
    """
    if not comprobar_entero_positivo(valor):
        return ""
    
    resultado = ""
    cociente = int(valor)
    
    while cociente >= base:
        resto = cociente % base
        cociente = cociente // base
        resultado += calcular_resto(resto)

    resultado += str(cociente)

    return resultado[::-1]


def convertir_decimal_binario(valor: str) -> str:
    """
    Convierte un número decimal a un número con base binaria.
    """
    return convertir_decimal_a_otra_base(valor, 2)


def convertir_decimal_octal(valor: str) -> str:
    """
    Convierte un número decimal a un número con base octal.
    """
    return convertir_decimal_a_otra_base(valor, 8)


def convertir_decimal_hexadecimal(valor: str) -> str:
    """
    Convierte un número decimal a un número con base hexadecimal.
    """
    return convertir_decimal_a_otra_base(valor, 16)


def convertir_a_base_decimal(valor: str, base: int) -> int:
    """
    Convierte un número de una base concreta a un número con base decimal.
    """
    resultado = 0
    for i in range(len(valor)):
        resultado += valor_posicion(valor[i]) * base

    return resultado


def convertir_numero_a_otra_base(valor: str, base1: int, base2: int) -> str:
    """
    Convierte un número de una base a otra.
    """
    # Convertir a base decimal
    if base1 != 10:
        valor = str(convertir_a_base_decimal(valor, base1))

    # Convertir decimal al numero en otra base
    return convertir_decimal_a_otra_base(valor, base2)


def introduce_base(msj: str) -> int:
    """
    Pide la base de un número hasta que introduzca una base correcta.
    """
    while True:
        base = input(msj).strip()
        if base not in ('2', '8', '10', '16'):
            print("**ERROR** no ha introducido una base correcta!\n")
        else:
            return int(base)


def introduce_numero(msj: str, base: int) -> str:
    """
    Pide un número hasta que el número introducido sea correcto.
    """
    while True:
        valor = input(msj).strip()
        if not comprobar_valor_base(valor, base):
            print(f"**ERROR** no ha introducido un número correcto para la base {dame_nombre_base(base)}!\n")
        else:
            return valor


def dame_nombre_base(base: int) -> str:
    """
    Retorna el nombre de la base en una cadena de caracteres.
    
    Args:
        base (int): número de dígitos del sistema de numeración (2, 8, 10 o 16).

    Returns:
        str: el nombre que recibe la base (por ejemplo: 2 => binaria)
    
    """
    if base == 2:
        return "binaria"
    elif base == 8:
        return "octal"
    elif base == 10:
        return "decimal"
    else:
        return "hexadecimal"


def main():
    #
    # DCS: Pendiente...
    # Ver cómo convertir los números negativos o sino no permitir que lo introduzcan...
    #
    limpiar_pantalla()
    base1 = introduce_base("\nIndica la base del número que vas a introducir (2, 8, 10 o 16): ")
    valor = introduce_numero("Introduce el valor del número a convertir (solo positivos): ", base1)
    base2 = introduce_base("\nIndica la base de numeración a la que quieres convertir el número (2, 8, 10 o 16): ")
    print(f"\nEl número {valor} en base {dame_nombre_base(base1)} es el {convertir_numero_a_otra_base(valor, base1, base2)} en base {dame_nombre_base(base2)}")


if __name__ == "__main__":
    main()