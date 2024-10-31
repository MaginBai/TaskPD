# Массив от 1 до 10 возвести в квадрат и отсотритьровать по убыванию.
array = list(range(1, 11))

for i in range(len(array)):
    array[i] *= array[i]

array.sort(reverse=True)
print(array)
