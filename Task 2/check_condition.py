def check_condition(func, value):
    return func(value)


def is_even(n):
    return n % 2 == 0


number = 4
result = check_condition(is_even, number)
print(f"Число {number} четное? {result}")
