# Ejercicio 2
# Escribe un programa para pedirle al usuario las horas de trabajo y el precio por hora y calcule el importe total del servicio.

def es_float(cadena):
    """Comprueba si la cadena es un número flotante válido"""
    
    partes = cadena.split('.')
    # Un número float puede tener solo una parte decimal y ambas partes deben ser dígitos
    
    if len(partes) == 1:
        # No hay punto decimal, debería ser un entero
        return partes[0].isdigit()
    elif len(partes) == 2:
        # Hay punto decimal, verificar ambas partes
        return (partes[0].isdigit() or partes[0] == '') and partes[1].isdigit()
    else:
        return False


def main():
    horas = input("Horas de trabajo: ")
    while not horas.isdigit():
        print("Por favor, introduce un número entero válido para las horas.")
        horas = input("Horas de trabajo: ")

    horas = int(horas)

    coste_hora = input("Coste por hora: ")
    while not es_float(coste_hora):
        print("Por favor, introduce un número válido para el coste por hora.")
        coste_hora = input("Coste por hora: ")

    coste_hora = float(coste_hora)

    # Calcular el salario
    salario = horas * coste_hora
    print("Importe total: {}".format(salario))


if __name__ == "__main__":
    main()