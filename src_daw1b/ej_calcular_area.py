import math

def calcular_area(a: float, b: float, c: float) -> float:
    s = (a + b + c)/2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area


def comprobar_float(valor: str) -> bool:
    # Eliminamos la primera posición de la cadena si existe un signo -
    if valor.startswith("-"):
        valor = valor[1:]

    # Si existe un punto lo eliminamos también
    pos_punto = valor.find(".")
    if pos_punto >= 0:
        valor = valor[:pos_punto] + valor[pos_punto + 1:]

    # Por tanto, si es un float la cadena resultante son solo dígitos
    return valor.isdigit()


def introduce_numero(msj: str) -> float:
    # Eliminamos los espacios el ppio y final de la cadena
    # También reemplazamos coma por punto para que aceptar float con ambos ("6.77" o "6,77")
    valor = input(msj).strip().replace(",", ".")
    unificar_simbolos_decimales_seguidos(valor)

    # Mientras la comprobación de número float no sea correcta permanece en el bucle
    while not comprobar_float(valor):
        print("\n**ERROR** Número inválido!")
        valor = input(msj).strip().replace(",", ".")

    # Ya es seguro convertir a float y retornar el número sin temor a errores
    return float(valor)


def comprobar_triangulo_valido(a, b, c):
    """
    Nota: 
    
    El área de un triángulo no se puede calcular cuando los tres lados proporcionados 
    no forman un triángulo válido. Para que tres longitudes puedan formar un triángulo, 
    deben cumplir la desigualdad triangular, que establece que para cualquier triángulo:
    La suma de dos lados debe ser siempre mayor que el tercer lado.
    
    Condiciones para un triángulo válido:
        a + b > c
        a + c > b
        b + c > a
    """    
    return (a + b > c) and (a + c > b) and (b + c > a)


def unificar_simbolos_decimales_seguidos(valor: str) -> str:
    total_posibles_simbolos_seguidos = len(valor) - 1
    for i in range(total_posibles_simbolos_seguidos, 1, -1):
        print(i)


def main():
    print("Dame los tres lados del triángulo...")
    
    lado_a = introduce_numero("Lado 1: ")
    lado_b = introduce_numero("Lado 2: ")
    lado_c = introduce_numero("Lado 3: ")

    if comprobar_triangulo_valido(lado_a, lado_b, lado_c):
        area = calcular_area(lado_a, lado_b, lado_c)
        print("El área del triángulo con lados ({:.2f}, {:.2f}, {:.2f}) es {:.2f}.".format(lado_a, lado_b, lado_c, area))
    else:
        print("El triángulo con lados ({:.2f}, {:.2f}, {:.2f}) no es válido!".format(lado_a, lado_b, lado_c))



if __name__ == "__main__":
    main()
