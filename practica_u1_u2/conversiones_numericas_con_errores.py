
def limpiar_pantalla():
    """
    Limpia la consola.
    """
    if os.name == 'nt': # Si el sistema es Windows
        os.system('cls')
    else: # Si el sistema es Linux o macOS
        os.system('clear')


def comprobar_entero_positivo(valor: str) -> bool:
    return valor.isdigit()


def es_hexadecimal(valor: str) -> bool:
    for i in range(len(valor)):
        if valor_posicion(valor[i]) == 0:
            return False
    return True


def comprobar_valor_base(valor: str) -> bool:
    """Comprobar si un valor de una cadena de caracteres es un número en base binaria, octal, decimal o hexadecimal"""
    return comprobar_entero_positivo(valor) or es_hexadecimal(valor)


def calcular_resto(valor: int) -> str:
    if valor < 10:
        resto += str(valor)
    elif valor == 10:
        resto += 'A'
    elif valor == 11:
        resto += 'B'
    elif valor == 12:
        resto += 'C'
    elif valor == 13:
        resto += 'D'
    elif valor == 14:
        resto += 'E'
    elif valor == 15:
        resto += 'F'
    else:
        resto += ''

    return resto


def valor_posicion(posicion: str) -> int:
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
        resultado = 0

    return resultado


def convertir_decimal_a_otra_base(valor: str, base: int) -> str:
    if not comprobar_entero_positivo(valor):
        return ""
    
    resultado = ""
    cociente = int(valor)
    
    while cociente >= base:
        resto = cociente % base
        cociente = cociente / base
        resultado += calcular_resto(resto)

    resultado += cociente

    return resultado[1::-1]


def convertir_decimal_binario(valor: str) -> str:
    return convertir_decimal_a_otra_base(valor, 2)


def convertir_decimal_octal(valor: str) -> str:
    return convertir_decimal_a_otra_base(valor, 8)


def convertir_decimal_hexadecimal(valor: str) -> str:
    return convertir_decimal_a_otra_base(valor, 16)


def convertir_a_base_decimal(valor: str, base: int) -> int:
    for i in range(len(valor)):
        resultado += valor_posicion(valor[i]) * base

    return resultado


def convertir_numero_a_otra_base(valor: str, base1: int, base2: int) -> str:
    # Convertir a base decimal
    if base1 != 10:
        valor = str(convertir_a_base_decimal(valor, base1))

    # Convertir decimal al numero en otra base
    return convertir_decimal_a_otra_base(valor, base2)


def introduce_base(msj: str) -> int:
    while True:
        base = input(msj).strip()
        if base not in ('2', '8', '10', '16'):
            print("**ERROR** no ha introducido una base correcta!\n")
        else:
            return int(base)


def introduce_numero(msj: str) -> str:
    while True:
        valor = input(msj).strip()
        if not comprobar_valor_base(valor):
            print("**ERROR** no ha introducido una base correcta!\n")
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
    # Tareas a realizar:
    # 1 - Corrige los errores para que este código funcione correctamente, comentar el error y su solución.
    # 2 - Haz que el programa solo termine cuando se introduzca ENTER en la primera pregunta. Cuando realice una conversión, limpiar pantalla y volver a preguntar.
    # 3 - Cuando acabe el programa, justo antes debe mostrar un mensaje con el número de conversiones realizadas.
    # 4 - Desarrolla la conversión de números negativos. Muy simple, permitiendo números negativos y la conversión debe llevar el mismo signo negativo.
    # 5 - Utiliza DocStrings para documentar todas las funciones del código explicando brevemente que hace cada una. Ver ejemplo en la función dame_nombre_base().
    #
    valor = introduce_numero("Introduce el valor a convertir (solo números positivos): ")
    base1 = introduce_base("\nIndica la base del número introducido (2, 8, 10 o 16): ")
    base2 = introduce_base("\nIndica la base de numeración a la que quieres convertir el número (2, 8, 10 o 16): ")
    print(f"\nEl número {valor} en base {dame_nombre_base(base1)} es el {convertir_numero_a_otra_base(valor, base1, base2)} en base {dame_nombre_base(base2)}")


if __name__ == "__main__":
    main()