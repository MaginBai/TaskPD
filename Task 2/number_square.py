def outer_function(number):
    def inner_function(n):
        return n ** 2

    result = inner_function(number)
    return result


number = 5
squared_value = outer_function(number)
print(f"Квадрат числа {number} равен {squared_value}.")
