#
# Ejercicio 2
# Escribe un programa para pedirle al usuario las horas de trabajo y el precio por hora y calcule el importe total del servicio.
#

def calculo_salario(horas, coste_hora):
    return horas * coste_hora


def main():
    horas = int(input("Horas de trabajo: "))
    coste_hora = float(input("Coste por hora: "))

    print("Importe total: {}".format(calculo_salario(horas, coste_hora)))


if __name__ == "__main__":
    main()
