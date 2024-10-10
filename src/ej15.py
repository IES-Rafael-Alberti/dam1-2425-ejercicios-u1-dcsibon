#
# Ejercicio 15
# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, 
# que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience 
# leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular 
# y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.
#
# Calcula el interés: capital * (1 + interes)
#


capital = float(input("Introduce la cantidad de dinero depositada: "))

interes = 4/100
capital_anio_1 = capital * (1 + interes)
capital_anio_2 = capital_anio_1 * (1 + interes)
capital_anio_3 = capital_anio_2 * (1 + interes)

print("Ahorros primer año:", round(capital_anio_1, 2))
print("Ahorros segundo año:", round(capital_anio_2, 2))
print("Ahorros tercer año:", round(capital_anio_3, 2))