def sum_of_squares(numbers):
    def square(x):
        return x * x

    return sum(square(num) for num in numbers)


print(sum_of_squares([1, 2, 3, 4]))
