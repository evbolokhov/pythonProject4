if __name__ == "__main__":
    a = int(input("Введите сторону A "))
    b = int(input("Введите сторону B "))
    c = int(input("Введите сторону C "))
    if (a * a == b * b + c * c) or (b * b == a * a + c * c) or (c * c == a * a + b * b):
        print("Прямоугольный")
    else:
        print("Не прямоугольный")
