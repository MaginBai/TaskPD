# реализцаия цикл в цикле. В данном случае таблица умножения
for i in range(1, 9):
    for j in range(1, 9):
        print(f"{i} x {j} = {i*j}", end='\t')
    print()
