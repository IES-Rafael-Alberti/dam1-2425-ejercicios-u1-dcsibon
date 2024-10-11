#
# Ejercicio 20
# Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, 
# y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono 
# con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
#


telefono = input("Introduce un número de teléfono en el formato +34-XXXXXXXXX-XX: ")

numero_sin_prefijo_ni_extension = telefono[4:-3]

# Otra forma:

# Encontrar las posiciones de los guiones
pos_guion_1 = telefono.find("-")
pos_guion_2 = telefono.rfind("-")

# Extraer el número sin prefijo ni extensión
numero_sin_prefijo_ni_extension = telefono[pos_guion_1 + 1:pos_guion_2]

print("Número sin prefijo y extensión:", numero_sin_prefijo_ni_extension)