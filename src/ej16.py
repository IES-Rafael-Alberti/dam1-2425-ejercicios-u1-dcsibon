#
# Ejercicio 16
# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. 
# Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el 
# programa debe mostrar el precio habitual de una barra de pan (establecido en el programa como una constante), 
# el descuento que se le hace por no ser fresca y el coste final total de todas las barras no frescas.
#


PRECIO_BARRA = 3.49

descuento = 6/100
barras_no_frescas = int(input("Introduce el número de barras no frescas vendidas: "))
precio_descuento = PRECIO_BARRA * descuento
precio_total = barras_no_frescas * PRECIO_BARRA * (1 - descuento)

print(f"Precio habitual: {PRECIO_BARRA}€")
print("Descuento por barra: {:.2f}€".format(precio_descuento))
print(f"Coste final total: {round(precio_total, 2)}€")