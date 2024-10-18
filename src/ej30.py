#
# Ejercicio 30
# Realiza un programa en Python que pida un número de inicio, un incremento y un total de la serie.
# - El incremento y el total deben ser mayores que cero. Si no es así, el programa debe finalizar con un error o obligar a 
#   que introduzcan un valor correcto para ambos (os lo dejo a vuestra elección, la primera opción es más fácil, aunque el 
#   mundo está lleno de valientes).
# - Por ejemplo, si introducen los valores 1, 1 y 10, el programa mostrará en consola exactamente lo siguiente: 
#   SERIE => 1-2..3..4..5..6..7..8..9-10
# 

inicio = int(input("dame el numero de inicio de la serie:"))
incremento = int(input("dame el numero de incremento de la serie:"))
total = int(input("dame el numero total de la serie:"))

if incremento < 0:
    while incremento < 0:
        incremento = int(input("dame un numero POSITIVO de incremento de la serie:"))

if total < 0:
    while total < 0:
        total = int(input("dame un numero POSITIVO de total de la serie:"))

serie = "SERIE => " + str(inicio) + "-"
cont = 1

while cont < total:
    inicio += incremento
    cont += 1
    if cont < (total-1):
        serie += str(inicio) + ".."
    else:
        if cont == total:
            serie += str(inicio)
        else:
            serie += str(inicio) + "-"

print(serie)


"""
# Otra forma... con un for o while y una lista

serie = []
fin = inicio + incremento * total

for i in range(inicio, inicio + incremento * total, incremento):
    serie.append(str(i))

num = inicio
while num <= fin:
    num += incremento
    serie.append(str(num))

# Mostrar la serie en el formato solicitado
print(f"SERIE => {'-'.join(serie[:1])}-{'..'.join(serie[1:-1])}-{'-'.join(serie[-1:])}")
"""