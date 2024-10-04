
def comprobar_entero(valor: str) -> bool:
    return valor.isdigit() or (valor.startswith("-") and valor[1:].isdigit())


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
        resto = ''

    return resto


def valor_posicion(posicion: str) -> str:
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
    if not comprobar_entero(valor):
        return ""
    
    valor_decimal = int(valor)
    resultado = ""
    cociente = valor_decimal
    
    while cociente >= base:
        cociente = valor_decimal // base
        resultado += calcular_resto(valor_decimal % base)

    resultado += cociente

    return resultado[::-1]


def convertir_decimal_binario(valor: str) -> str:
    return convertir_decimal_a_otra_base(valor, 2)


def convertir_decimal_octal(valor: str) -> str:
    return convertir_decimal_a_otra_base(valor, 8)


def convertir_decimal_hexadecimal(valor: str) -> str:
    return convertir_decimal_a_otra_base(valor, 16)


def convertir_a_base_decimal(valor: str, base: int) -> int:
    resultado = 0
    for i in range(len(valor)):
        resultado += valor_posicion(valor[i]) * base

    return resultado


def convertir_numero_a_otra_base(valor: str, base1: int, base2: int) -> str:
    # Convertir a base decimal
    if base1 != 10:
        valor = str(convertir_a_base_decimal(valor, base1))

    # Convertir decimal al numero en otra base
    return convertir_decimal_a_otra_base(valor, base2)


def main():
    valor = input("Introduce el valor a convertir: ")
    print(convertir_decimal_binario(valor))


if __name__ == "__main__":
    main()