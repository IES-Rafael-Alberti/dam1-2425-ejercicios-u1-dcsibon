#
# Ejercicio 3
# Suponiendo que se han ejecutado las siguientes sentencias de asignación: 
# ancho = 17
# alto = 12.0
# Para cada una de las expresiones siguientes, intenta adivinar el valor de la expresión y su tipo sin ejecutarlas en el intérprete:
# 1. ancho / 2
# 2. ancho // 2
# 3. alto / 3
# 4. 1 + 2 * 5
#
# EXTRA: Analizar las nuevas expresiones:
# 1. ancho / alto
# 2. ancho // 2
# 3. ancho / 2
# 4. ancho * 2
# 5. ancho * alto
# 6. (5 + 1) * 3
# 7. (5 + 1) / 3
# Después mostrar resultado y tipo por pantalla de cada expresión para comprobar si habéis acertado.
# La salida esperada es:
# ancho / alto = 1.4166666666666667 y es de tipo <class 'float'>
#

ancho = 17

alto = 12.0

res = ancho / alto
print("ancho / alto = " + str(res) + " y es de tipo " + str(type(res)))

res = ancho // 2
print("ancho // 2 = " + str(res) + " y es de tipo " + str(type(res)))

res = ancho / 2
print("ancho / 2 = " + str(res) + " y es de tipo " + str(type(res)))

res = ancho * 2
print("ancho * 2 = " + str(res) + " y es de tipo " + str(type(res)))

res = ancho * alto
print("ancho * alto = " + str(res) + " y es de tipo " + str(type(res)))

res = (5 + 1) * 3
print("(5 + 1) * 3 = " + str(res) + " y es de tipo " + str(type(res)))

res = (5 + 1) / 3
print("(5 + 1) / 3 = " + str(res) + " y es de tipo " + str(type(res)))
