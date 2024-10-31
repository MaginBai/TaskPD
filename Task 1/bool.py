# Реализация с булевыми операциям XOR, также отображение пересечения, не пересечения в множествах
def xor(a: bool, b: bool) -> bool:
    return (a and not b) or (not a and b)


print(xor(True, False))
print(xor(False, False))
print(xor(False, True))
print(xor(True, True))

set_one = {1, 2, 3, 4}
set_two = {3, 4, 5, 6}
print(set_one & set_two)
print(set_one ^ set_two)
