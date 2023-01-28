# 1. Показ списка учеников
# 2. Добаить нового студента (поля: имя, фамилия)
# 3. Добаить предмет
# 4. Добаить оценку ученику
# 5. Редактировать данные ученика
# 6. Удалить ученика
# 7. Показ листа оценок конкретного ученика
# 8. Выход из программы


students_book = []
path = 'school/data.txt'

def get_students_book():
    global students_book
    return students_book

def open_file():
    global path
    global students_book
    with open(path, 'r', encoding='utf-8') as data: # преобразую в utf-8, иначе ошибка (кириллица)
        file = data.readlines()
    for student in file:
        students_book.append(student.strip().split(','))
    return file

def close_file():
    global students_book
    students_book = []


def save_file():
    global path
    global students_book
    pb_str = []
    for student in students_book:
        pb_str.append(','.join(student))
    with open(path, 'w', encoding='utf-8') as data: # преобразую в utf-8, иначе ошибка (кириллица)
        data.write('\n'.join(pb_str))
    
def add_new_student(new_student: list):
    global students_book
    students_book.append(new_student)

def get_student(find_cont: str):
    global students_book
    result = []
    for i, student in enumerate(students_book):
        for field in student:
            if find_cont in field:
                result.append((student, i)) # возвращается кортеж - студент и его индекс
                break
    if len(result) > 1: # если в список по поиску для удаления добавились больше 1 строки, то мы не можем удалить
        return False
    elif result == []:
        return result
    else:
        return result[0]

def del_student(student: list):
    global students_book
    students_book.remove(student)

def change_student(index: int, new: list):
    global students_book
    for i in range(len(new)):
        if new[i] != '':
            students_book[index][i] = new [i]
        else:
            students_book[index][i]



# def get_students(find_cont: str):
#     global students_book
#     result = []
#     for i, students in enumerate(students_book):
#         for field in students:
#             if find_cont in field:
#                 result.append((students, i)) # возвращается кортеж - сам студент и его индекс
#                 break
#     if len(result) > 1: # если в список по поиску для удаления добавились больше 1 строки, то мы не можем удалить
#         return False
#     elif result == []:
#         return result
#     else:
#         return result[i]