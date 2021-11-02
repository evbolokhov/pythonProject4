if __name__ == "__main__":
    A = int(input("Введите целое число A "))
    B = int(input("Введите целое число B "))
    c = A % 2 == 0
    d = B % 2 == 0
    if (c or d) and not (c and d):
        print("Условие выполняется")
    else:
        print("Условие не выполняется")
