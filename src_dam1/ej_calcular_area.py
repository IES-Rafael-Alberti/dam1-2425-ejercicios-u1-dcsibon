import math

def tiene_mas_de_un_punto(valor: str):
    # Buscaamos la posición del primero punto
    pos_primer_punto = valor.find(".")

    # Si existe un punto, buscamos alguno más
    if pos_primer_punto >= 0 and valor.find(".", pos_primer_punto + 1) >= 0:
        return True
    else:
        return False


def contiene_digitos(valor: str):
    # En esta función ya sabemos que valor solo tiene un punto o ninguno.
    # Podemos eliminar el punto para que solo queden dígitos y simplificar la comprobación.
    valor = valor.replace(".", "")

    # Por tanto, si es un float la cadena resultante son solo dígitos
    return valor.isdigit()


def comprobar_numero_float(valor: str):
    # Eliminamos el signo menos de la primera posición si existe para las comprobaciones
    if valor[:1] == "-":
        valor = valor[1:]
    
    # Podemos unir las dos condiciones porque se lee muy fácil:
    # Retorna True si "no tiene más de un punto y contiene dígitos".
    return (not tiene_mas_de_un_punto(valor)) and contiene_digitos(valor)


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


def calcular_area(a, b, c):
    semiper = (a + b + c) / 2
    area = math.sqrt(semiper * (semiper - a) * (semiper - b) * (semiper - c))

    return area


def introduce_numero(msj: str):
    # Eliminamos los espacios el ppio y final de la cadena
    # También reemplazamos coma por punto para que aceptar float con ambos ("6.77" o "6,77")
    numero = input(msj).strip().replace(",", ".")

    # Mientras la comprobación de número float no sea correcta permanece en el bucle
    while comprobar_numero_float(numero) == False:
        print("**ERROR** Número inválido")
        numero = input(msj).strip()    
    
    return float(numero)


def main():
    print("Dame los tres lados del triángulo...")

    lado_a = introduce_numero("Lado 1: ")
    lado_b = introduce_numero("Lado 2: ")
    lado_c = introduce_numero("Lado 3: ")

    # Agregamos esta comprobación matemática para no usar try-except que ya veremos más adelante
    if comprobar_triangulo_valido(lado_a, lado_b, lado_c):
        area = calcular_area(lado_a, lado_b, lado_c)
        print("El área del triángulo con lados ({:.2f}, {:.2f}, {:.2f}) es {:.2f}.".format(lado_a, lado_b, lado_c, area))
    else:
        print("El triángulo con lados ({:.2f}, {:.2f}, {:.2f}) no es válido!".format(lado_a, lado_b, lado_c))


if __name__ == "__main__":
    main()