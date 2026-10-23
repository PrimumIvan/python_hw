n = int(input("Введите год"))

def is_year_leap(year):
  return year % 4 == 0


result = is_year_leap(n)
print("Год", n, ":", result)
