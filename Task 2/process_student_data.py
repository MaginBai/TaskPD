# функция с несколькими параметрами, у которых задан тип
def prossec_student_data(name: str, age: int, grades: list[float], is_full_time: bool = True):
    if age < 18 and age > 100:
        raise Exception("Возраст должен быть  от 18 до 100")
    el_sum = 0
    for el in grades:
        el_sum += el
        average_grade = el_sum/len(grades)

    return {'name': name, 'age': age, 'average_grade': average_grade, 'status': 'Full-time' if is_full_time else "Distance"}


student = prossec_student_data("Artem", 19, [5, 4, 2, 5, 3], False)
print(student)
