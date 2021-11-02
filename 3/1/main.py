if __name__ == "__main__":
    a = int(input("Введите сумму вклада "))
    if a < 5000:
        b = a * 1.2
    else:
        b = a * 1.22
    print("Сумма выплаты ", b)
