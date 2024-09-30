#
# Ejercicio 28
# Realiza un programa en Python que lea dos números enteros, muestre cuál es el menor de los dos y cuántos números existen entre ellos dos.
# El segundo número no puede ser igual, si es así, debe mostrar el error: "Los números no pueden ser iguales".
# Si los números son diferentes, por ejemplo, 5 y 12, debe mostrar la frase: "El número menor es el 5 y entre ellos existen 7 números enteros".
#


num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

if num1 == num2:
    print("Los números no pueden ser iguales.")
else:
    menor = min(num1, num2)
    mayor = max(num1, num2)
    diferencia = mayor - menor - 1
    print(f"El número menor es el {menor} y entre ellos existen {diferencia} números enteros.")