# Реализация кортежей. ХЗ только это придумал
students = [
    ("Иван", 20, 4.5),
    ("Мария", 22, 4.8),
    ("Петр", 21, 4.3),
    ("Анна", 19, 4.9),
    ("Сергей", 23, 4.7)
]


def get_top_student(students):
    top_student = max(students, key=lambda student: student[2])
    return top_student


top_student = get_top_student(students)
print("Студент с наивысшим средним баллом:")
print(f"Имя: {top_student[0]}, Возраст: {
      top_student[1]}, Средний балл: {top_student[2]}")
