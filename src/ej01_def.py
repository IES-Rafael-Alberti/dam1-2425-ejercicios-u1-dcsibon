#
# Ejercicio 1
# Escribe un programa que pida el nombre del usuario para luego darle la bienvenida.
#

import os

def saludo(nombre):
    nombre = nombre.strip()
    if not nombre:
        return "No has introducido un nombre."
    return "Hola, " + nombre.title() + "."

    #return "Hola, " + nombre.capitalize() + "."
    #return "Hola, " + nombre[0:1].upper() + nombre[1:].lower() + "."


def capitalizar(frase):
    return frase[0:1].upper() + frase[1:].lower()

def titular_v1(frase):
    palabra = ""
    frase_titular = ""

    for letra in frase:
        if letra == " ":
            frase_titular += palabra[0:1].upper() + palabra[1:].lower() + " "
            palabra = ""
        else:
            palabra += letra

    if len(palabra) > 0:
        frase_titular += palabra[0:1].upper() + palabra[1:].lower()

    return frase_titular


def titular_v2(frase):
    lista_palabras = frase.split()
    frase_titular = ""

    for palabra in lista_palabras:
        frase_titular += palabra[0:1].upper() + palabra[1:].lower() + " "

    return frase_titular


def titular_v3(frase):
    lista_palabras = frase.split()

    for i in range(len(lista_palabras)):
        lista_palabras[i] = lista_palabras[i][0:1].upper() + lista_palabras[i][1:].lower() + " "

    return " ".join(lista_palabras)


def limpiar_pantalla():
    if os.name == 'nt':  # 'nt' es Windows
        os.system('cls')
    else:
        os.system('clear')


def main():
    print(saludo(input("Escribe tu nombre: ")))


if __name__ == "__main__":
    main()

# str.capitalize(): Convierte solo la primera letra de la cadena a mayúsculas y el resto a minúsculas.
# str.title(): Convierte la primera letra de cada palabra en mayúscula y el resto en minúsculas.

# Los que van más avanzados => Crear la función capitalizar() y titular() simulando el comportamiento de capitalize() y title()
# 1. titular_v1() => Solo con un bucle.
# 2. titular_v2() => Usando una lista (investiga la función split()).
# 3. titular_v3() => Con una lista, modificando los elementos de la lista y usando join().