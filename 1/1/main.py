if __name__ == "__main__":
    A = int(input("Введите целое число "))
    b = A % 2 == 0
    c = A % 3 == 0
    if b or c:
        print("Условие выполняется")
    else:
        print("Условие не выполняется")
