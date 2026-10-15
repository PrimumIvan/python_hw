import math


def square(i):
    return math.ceil(i*i)


num_items = float(input("Введите сторону квадрата: "))
print(f"Округлённая площадь: {square(num_items)}")