def find_max(*args):
    sum = 0
    for el in args:
        sum += el
    return sum


print(find_max(3, 2, 6, 7, 4, 8, 3, 2.5))
