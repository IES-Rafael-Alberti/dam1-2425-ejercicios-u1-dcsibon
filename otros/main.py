def suma(n1, n2):
    return n1 + n2

def main():
    num1 = int(input("Dame un número: "))
    num2 = int(input("Dame otro número: "))
    print(f"La suma de {num1} + {num2} es {suma(num1, num2)}")

if __name__ == "__main__":
    main()