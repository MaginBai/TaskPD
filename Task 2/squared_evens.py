
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


squared_evens = list(
    map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))

print(squared_evens)
