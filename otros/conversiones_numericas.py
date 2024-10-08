import os

SIMBOLOS = ("0", "1", "2", "3", "4", "5", 
            "6", "7", "8", "9", "A", "B", 
            "C", "D", "E", "F")

BASE_BINARIA = 2
BASE_OCTAL = 8
BASE_DECIMAL = 10
BASE_HEXADECIMAL = 16


def limpiar_pantalla():
    """
    Limpia la consola según el sistema operativo.
    
    En sistemas Windows utiliza el comando 'cls', en Linux o macOS utiliza 'clear'.
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def comprobar_entero(valor: str) -> bool:
    """
    Comprueba si una cadena de caracteres representa un número entero.

    Args:
        valor (str): La cadena de caracteres a comprobar.

    Returns:
        bool: True si es un número entero válido, False en caso contrario.
    """
    if valor == "-":
        return False
    return valor.isdigit() or (valor.startswith("-") and valor[1:].isdigit())


def es_hexadecimal(valor: str) -> bool:
    """
    Comprueba si una cadena de caracteres es un número en base hexadecimal.

    Args:
        valor (str): La cadena de caracteres a comprobar.

    Returns:
        bool: True si es hexadecimal, False en caso contrario.
    """
    if valor.startswith("-"):
        valor = valor[1:]

    for i in range(len(valor)):
        if valor_simbolo(valor[i]) == -1:
            return False
    return True


def es_decimal(valor: str) -> bool:
    """
    Comprueba si una cadena de caracteres es un número en base decimal.

    Args:
        valor (str): La cadena de caracteres a comprobar.

    Returns:
        bool: True si es decimal, False en caso contrario.
    """
    return comprobar_entero(valor)


def es_octal(valor: str) -> bool:
    """
    Comprueba si una cadena de caracteres es un número en base octal.

    Args:
        valor (str): La cadena de caracteres a comprobar.

    Returns:
        bool: True si es octal, False en caso contrario.
    """
    if valor.startswith("-"):
        valor = valor[1:]

    for i in range(len(valor)):
        valor_numerico = valor_simbolo(valor[i])
        if valor_numerico > 7 or valor_numerico == -1:
            return False
    return True


def es_binario(valor: str) -> bool:
    """
    Comprueba si una cadena de caracteres es un número en base binaria.

    Args:
        valor (str): La cadena de caracteres a comprobar.

    Returns:
        bool: True si es binario, False en caso contrario.
    """
    if valor.startswith("-"):
        valor = valor[1:]

    for i in range(len(valor)):
        valor_numerico = valor_simbolo(valor[i])
        if valor_numerico > 1 or valor_numerico == -1:
            return False
    return True


def comprobar_valor_base(valor: str, base) -> bool:
    """
    Comprueba si una cadena de caracteres es válida en una base dada.

    Args:
        valor (str): La cadena de caracteres a comprobar.
        base (int): La base numérica (2, 8, 10, 16).

    Returns:
        bool: True si el valor es válido en la base dada, False en caso contrario.
    """
    if valor == "" or valor == "-":
        return False
    elif base == BASE_BINARIA:
        return es_binario(valor)
    elif base == BASE_OCTAL:
        return es_octal(valor)
    elif base == BASE_DECIMAL:
        return es_decimal(valor)
    elif base == BASE_HEXADECIMAL:
        return es_hexadecimal(valor)
    else:
        return False


def dame_simbolo(valor: int) -> str:
    """
    Retorna el símbolo correspondiente a un valor en base hexadecimal.

    Args:
        valor (int): El valor entero entre 0 y 15.

    Returns:
        str: El símbolo correspondiente al valor.

    Raises:
        ValueError: Si el valor está fuera del rango permitido.
    """
    if valor not in range(len(SIMBOLOS)):
        raise ValueError(f"Valor {valor} fuera del rango hexadecimal permitido.")
    
    return SIMBOLOS[valor]


def valor_simbolo(posicion: str) -> int:
    """
    Retorna el valor numérico correspondiente a un símbolo.

    Args:
        posicion (str): El símbolo a convertir.

    Returns:
        int: El valor numérico correspondiente al símbolo, o -1 si no es válido.
    """
    try:
        resultado = SIMBOLOS.index(posicion)
    except ValueError:
        resultado = -1
    
    return resultado


def convertir_decimal_a_otra_base(valor: str, base: int) -> str:
    """
    Convierte un número decimal a una base dada.

    Args:
        valor (str): El número decimal en formato de cadena de caracteres.
        base (int): La base a la que se quiere convertir (2, 8, 16).

    Returns:
        str: El número convertido a la base dada en formato de cadena.
    """
    resultado = ""
    cociente = int(valor)

    try:
        while cociente >= base:
            resto = cociente % base
            cociente = cociente // base
            resultado += dame_simbolo(resto)

        resultado += str(dame_simbolo(cociente))
    except ValueError as e:
        print(f"**ERROR** en la conversión: {e}")
        return ""

    return resultado[::-1]


def convertir_a_base_decimal(valor: str, base: int) -> int:
    """
    Convierte un número en una base dada a base decimal.

    Args:
        valor (str): El número en formato de cadena de caracteres.
        base (int): La base de origen del número (2, 8, 16).

    Returns:
        int: El número convertido a decimal.
    """
    resultado = 0
    exponente = 0
    i = len(valor) - 1  # Empezamos desde la última posición de la cadena de caracteres valor

    while i >= 0:
        resultado += valor_simbolo(valor[i]) * base ** exponente
        exponente += 1  # Incrementamos el exponente de la base
        i -= 1  # Nos movemos hacia el siguiente carácter (de derecha a izquierda)

    return resultado


def convertir_numero_a_otra_base(valor: str, base1: int, base2: int) -> str:
    """
    Convierte un número de una base a otra.

    Args:
        valor (str): El número en formato de cadena de caracteres.
        base1 (int): La base de origen del número.
        base2 (int): La base a la que se desea convertir.

    Returns:
        str: El número convertido a la base destino.
    """
    if valor.startswith("-"):
        simbolo_primera_posicion = "-"
        valor = valor[1:]
    else:
        simbolo_primera_posicion = ""

    # Convertir a base decimal
    if base1 != 10:
        valor = str(convertir_a_base_decimal(valor, base1))

    if valor == "":
        simbolo_primera_posicion = ""
        valor = "0"

    if base2 != 10:
        # Convertir decimal al numero en otra base
        valor = convertir_decimal_a_otra_base(valor, base2)

    return simbolo_primera_posicion + valor


def introduce_base(msj: str, permitir_entrada_vacia: bool = False) -> int:
    """
    Solicita al usuario una base numérica válida (2, 8, 10 o 16).

    Args:
        msj (str): El mensaje a mostrar al usuario.
        permitir_entrada_vacia (bool): Si se permite una entrada vacía. (default: False)

    Returns:
        int: La base numérica seleccionada o None si la entrada está vacía.
    """
    while True:
        base = input(msj).strip()
        
        if permitir_entrada_vacia and base == "":
            return None
        
        if base not in ('2', '8', '10', '16'):
            print("**ERROR** no ha introducido una base correcta!\n")
        else:
            return int(base)


def introduce_numero(msj: str, base: int) -> str:
    """
    Solicita al usuario un número válido para la base dada.

    Args:
        msj (str): El mensaje a mostrar al usuario.
        base (int): La base numérica en la que debe estar el número.

    Returns:
        str: El número introducido por el usuario.
    """
    while True:
        valor = input(msj).strip()
        if not comprobar_valor_base(valor, base):
            print(f"**ERROR** el número '{valor}' no es válido para la base {dame_nombre_base(base)}!\n")
        else:
            return valor


def dame_nombre_base(base: int) -> str:
    """
    Retorna el nombre de la base numérica.

    Args:
        base (int): El valor numérico de la base (2, 8, 10, 16).

    Returns:
        str: El nombre descriptivo de la base (por ejemplo, 'binaria').
    """
    if base == BASE_BINARIA:
        return "binaria"
    elif base == BASE_OCTAL:
        return "octal"
    elif base == BASE_DECIMAL:
        return "decimal"
    elif base == BASE_HEXADECIMAL:
        return "hexadecimal"
    else:
        return "desconocida"


def desea_salir() -> bool:
    """
    Pregunta al usuario si desea salir del programa.

    Returns:
        bool: True si el usuario desea salir, False en caso contrario.
    """
    salir = input("\n¿Desea salir del programa? (S/N) ").upper()
    return salir in {'S', 'SI', 'Y', 'YES'}


def main():
    """
    Función principal que coordina la interacción con el usuario y la conversión de bases numéricas.
    """
    contador_conversiones = 0
    while True:
        limpiar_pantalla()
        base1 = introduce_base("\nIndica la base del número que vas a introducir (2, 8, 10 o 16): ", True)

        if base1 == None:
            if desea_salir():
                print(f"\nHas realizado {contador_conversiones} {'conversión' if contador_conversiones == 1 else 'conversiones'}.\n")
                return
            else:
                continue

        valor = introduce_numero("\nIntroduce el valor del número a convertir: ", base1)

        base2 = introduce_base("\nIndica la base de numeración a la que quieres convertir el número (2, 8, 10 o 16): ")
        
        print(f"\nEl número \"{valor}\" en base {dame_nombre_base(base1)} es el \"{convertir_numero_a_otra_base(valor, base1, base2)}\" en base {dame_nombre_base(base2)}.")
        contador_conversiones += 1
        input("\n\nPresione ENTER para continuar...")


if __name__ == "__main__":
    main()