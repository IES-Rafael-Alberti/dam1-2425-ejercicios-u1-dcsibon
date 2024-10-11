#
# Ejercicio 13
# Escribir un programa que pida al usuario dos números enteros y muestre por pantalla los siguiente: 
# "la división de n entre m da un cociente c y un resto r", donde n y m son los números introducidos 
# por el usuario, y c y r son el cociente y el resto de la división entera respectivamente.
#

n = int(input("Introduzca un número: "))
m = int(input("Introduzca otro número: "))

c = n // m
r = n % m

print("la división de", n, "entre", m, "da un cociente", c, "y un resto", r)

#print("la división de {} entre {} da un cociente {} y un resto {}".format(n, m, c, r))
#print(f"la división de {n} entre {m} da un cociente {c} y un resto {r}")