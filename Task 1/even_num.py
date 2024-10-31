# Нахождение четных чисел до заданного числа
max_limit = int(input("Up to what number to look for even numbers: "))
for v in range(1, max_limit):
    if v % 2 == 0:
        print(v)
