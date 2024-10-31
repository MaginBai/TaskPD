# Функции с переменым числом аргументов

def get_maps(**arg):
    return arg


def sum_array(*array):
    return sum(array)


print(sum_array(1, 23, 4, 52, 12))
print(get_maps(name='Arthur', age=23, sex='Male'))
