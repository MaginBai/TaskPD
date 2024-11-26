# функция, принимающая лямбда-выражение как параметр, и вызывающая лямбда-выражение внутри себя
def execute_lambda(lambda_func, value):
    return lambda_func(value)


def my_lambda(x): return x * 2


result = execute_lambda(my_lambda, 5)
print(result)
