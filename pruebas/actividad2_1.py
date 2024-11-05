"""

Actividad 1: Escribe un programa que lea repetidamente números hasta que el usuario introduzca “fin”. Una vez se haya introducido “fin”, muestra por pantalla el total, la cantidad de números y la media de esos números. Si el usuario introduce cualquier otra cosa que no sea un número, (mas adelante veremos como detectar los fallos usando try y except)

Introduzca un número: 4
Introduzca un número: 5
Introduzca un número: dato erróneo
Entrada inválida
Introduzca un número: 7
Introduzca un número: fin
16 3 5.33333333333

"""

def comprobar_numero(cadena: str) -> bool:
    """   
    Comprueba si la cadena de caracteress es un número entero opositivo.
    """
    if cadena.startswith("-"):
        cadena = cadena[1:]
    return cadena.isdigit()


def main():

    cantidad = 0
    suma = 0
    media = 0
    salir = False
    
    while not salir:
        entrada = input("Introduzca un número: ")
        
        if entrada.lower() == "fin":
            # fin
            salir = True
        elif not comprobar_numero(entrada):
            print("Entrada inválidad!")
        else:
            num = int(entrada)
            cantidad += 1
            suma += num

    if cantidad != 0:
        media = suma / cantidad
    
    print("{} {} {}".format(suma, cantidad, media))

if __name__ == "__main__":
    main()