#
# Ejercicio 2
# Escribe un programa para pedirle al usuario las horas de trabajo y el precio por hora y calcule el importe total del servicio.
#

horas = int(input("Horas de trabajo: "))
coste_hora = float(input("Coste por hora: "))
salario = horas * coste_hora

print("Importe total: {}".format(salario))

#print("Importe total: " + str(horas * coste_hora))
