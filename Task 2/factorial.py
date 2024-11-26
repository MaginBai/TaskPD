def factorial(n):
    def recursive_factorial(x):
        if x == 0 or x == 1:
            return 1
        else:
            return x * recursive_factorial(x - 1)
    if n < 0:
        raise ValueError("Факториал не определен для отрицательных чисел.")
    return recursive_factorial(n)


print(factorial(5))
