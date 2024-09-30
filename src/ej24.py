#
# Ejercicio 24
# Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla 
# el número de euros y el número de céntimos del precio introducido.
#


precio = float(input("Introduce el precio en euros (con dos decimales): "))

euros = int(precio)

centimos = int((precio - euros) * 100)

print(f"Euros: {euros}, Céntimos: {centimos}")