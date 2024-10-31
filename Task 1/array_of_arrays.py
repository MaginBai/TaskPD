# Массив массивов. В даном случае матрица.

import random

rows = int(input("Input rows: "))
cols = int(input("Input cols: "))

matix = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(random.randint(1, 100))
    matix.append(row)

for row in matix:
    print(row)
