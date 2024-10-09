
def divisores(numero):
    resultado = ""
    for i in range(1, numero + 1):
        if numero % i == 0:
            resultado += str(i) + " "
    
    return resultado.strip()


def main():
    numero = int(input("Introduzca un número: "))
    divisores_numero = divisores(numero)
    print(f"Los divisores de {numero} son: {divisores_numero}")



if __name__ == "__main__":
    main()
