

def es_mayor(num1, num2):
    if num1 == num2:
        return 0
    else:
        return max(num1, num2)
    

def main():
    num1 = input("Introduzca un número: ")
    num2 = input("Introduzca otro número: ")
    print(es_mayor(num1, num2))


if __name__ == "__main__":
    main()