#
# Ejercicio 5
# Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar y calcule e imprima por pantalla 
# el precio final del artículo.
#
# EXTRA: Para los Ejercicios 1.5 al 1.10, se deben usar tipos de datos float y mostrar los resultados con 2 posiciones decimales.
#

importe = float(input("Introduzca el importe: "))

iva = float(input("Introduzca el % de IVA a aplicar: "))

if (iva < 0 or iva > 100):
    iva = 21
    print("El porcentaje debe ser un valor entre 0 y 100... se aplicará el 21%")

print("El precio final del artículo con IVA ({:.2f}) es {:.2f}€.".format(iva, importe + (importe * (iva / 100))))
