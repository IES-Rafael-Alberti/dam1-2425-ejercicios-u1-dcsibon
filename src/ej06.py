#
# Ejercicio 6
# Escribe un programa que pida el importe final de un artículo y calcule e imprima por pantalla el IVA que se ha pagado y 
# el importe sin IVA (suponiendo que se ha aplicado un tipo de IVA del 10%).
#
# EXTRA: Para los Ejercicios 1.5 al 1.10, se deben usar tipos de datos float y mostrar los resultados con 2 posiciones decimales.
#


precio = float(input("Introduzca el importe final: "))
iva_aplicado = float(input("Introduzca el IVA aplicado: "))

precio_sin_iva = precio / (1 + iva_aplicado/100)
iva_calculado = precio - precio_sin_iva

print("Precio sin IVA: {:.2f}€.\nImporte del IVA: {:.2f}€".format(precio_sin_iva, iva_calculado))

