#
# Ejercicio 25
# Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, 
# el día, el mes y el año. 
# Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.
#


fecha = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")

#dia, mes, ano = fecha.split('/')

pos1 = fecha.find('/')
pos2 = fecha.find('/', pos1 + 1)

dia = fecha[:pos1]
mes = fecha[pos1 + 1:pos2]
ano = fecha[pos2 + 1:]

print(f"Día: {dia}, Mes: {mes}, Año: {ano}")

