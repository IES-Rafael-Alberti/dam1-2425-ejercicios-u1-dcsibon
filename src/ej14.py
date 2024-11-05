#
# Ejercicio 14
# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa 
# de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en 
# cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y 
# muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.
#


peso_payaso = 112
peso_muneca = 75

num_payasos = int(input("Introduce el número de payasos vendidos: "))
num_muniecas = int(input("Introduce el número de muñecas vendidas: "))

peso_total = (peso_payaso * num_payasos) + (peso_muneca * num_muniecas)

print("El peso total del paquete es: {:.2f} kg".format(peso_total/1000))