# лямбда-выражение с параметрами
strings = ["apple", "banana", "kiwi", "cherry", "blueberry"]

sorted_strings = sorted(strings, key=lambda x: len(x))

print(sorted_strings)
