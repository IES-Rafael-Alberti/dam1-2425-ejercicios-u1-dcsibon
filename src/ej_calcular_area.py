import math

def tiene_mas_de_un_punto(valor: str):
    pos_primer_punto = valor.find(".")
    if pos_primer_punto >= 0 and valor.find(".", pos_primer_punto + 1):
        return True
    else:
        return False


def contiene_solo_digitos_y_un_punto(valor: str):
    for i in range(len(valor)): # 0..len(valor) - 1
        if not (valor[i].isdigit() or valor[i] == "."):
            return False
    return True


def comprobar_numero_float(valor: str):
    if valor[:1] == "-":
        valor = valor[1:]
        if len(valor) == 0:
            return False

    if tiene_mas_de_un_punto(valor):
        return False
    
    return contiene_solo_digitos_y_un_punto(valor)



def calcular_area(lado_a, lado_b, lado_c):
    try:
        semiperimetro = (lado_a + lado_b + lado_c) / 2
        area = math.sqrt(semiperimetro * (semiperimetro - lado_a) * (semiperimetro - lado_b) * (semiperimetro - lado_c))
    except ValueError:
        print("**ERROR** Cálculo de área imposible con estos valores.")
        return None

    return area


def introduce_numero(msj: str):
    numero = input(msj).strip()
    while comprobar_numero_float(numero) == False:
        print("**ERROR** Número inválido")
        numero = input(msj).strip()    
    
    return float(numero)


def main():
    print("Dame los tres lados del triángulo...")

    lado_a = introduce_numero("Lado 1: ")
    lado_b = introduce_numero("Lado 2: ")
    lado_c = introduce_numero("Lado 3: ")

    area = calcular_area(lado_a, lado_b, lado_c)

    if area is not None:
        print("El área del triángulo es {:.2f}".format(area))


if __name__ == "__main__":
    main()