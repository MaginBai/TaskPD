def apply_function_to_list(func, lst):
    return [func(x) for x in lst]


def square(x):
    return x ** 2


numbers = [1, 2, 3, 4, 5]
squared_numbers = apply_function_to_list(square, numbers)
print(squared_numbers)
