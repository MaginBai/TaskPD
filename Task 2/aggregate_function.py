def aggregate(func, lst):
    result = lst[0]
    for item in lst[1:]:
        result = func(result, item)
    return result


def add(x, y):
    return x + y


numbers = [1, 2, 3, 4]
total = aggregate(add, numbers)
print(f"Сумма чисел: {total}")
