#
# Ejercicio 29
# Realiza un programa en Python que solicite un nombre y una edad.
# Si el nombre está vacío, debes utilizar el valor "Desconocido". La edad debe pedirse hasta que introduzca una edad comprendida entre 0 y 125 años.
# El programa mostrará la siguiente frase: "Te llamas Pepito y tienes 20 años, te quedan aún 105 años por cumplir".
#


nombre = input("Introduce tu nombre: ")
if nombre == "":
    nombre = "Desconocido"

edad = int(input("Introduce tu edad: "))

while edad < 0 or edad > 125:
    print("Edad no válida, debe ser entre 0 y 125.")
    edad = int(input("Introduce tu edad: "))

años_restantes = 125 - edad

print(f"Te llamas {nombre} y tienes {edad} años, te quedan aún {años_restantes} años por cumplir.")