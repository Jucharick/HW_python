# 1. Показ списка учеников
# 2. Добавить нового студента (поля: имя, фамилия)
# 3. Добавить предмет
# 4. Добавить оценку ученику
# 5. Редактировать данные ученика
# 6. Удалить ученика
# 7. Показ листа оценок конкретного ученика
# 8. Выход из программы

# main_journal = {'Name_1': {'math': [4, 5, 4], 'phisic': [5,3,5]}, 'Name_2': {'math': [4, 5, 4], 'phisic': [5,3,5]}}

main_journal = {}
path_journal = 'school/journal.txt'

students_book = []
path = 'school/data.txt'

lesson_book = []
path_les = 'school/lesson.txt'


def get_students_book():
    global students_book
    return students_book

def get_lesson_book():
    global lesson_book
    return lesson_book

def create_main_journal():
    global main_journal
    global students_book
    global lesson_book
    for name in students_book:
        student = ' '.join(name)
        main_journal[student] = {}
        for lesson in lesson_book:
            main_journal[student][lesson] = []

def get_main_journal():
    global main_journal
    return main_journal

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
    global lesson_book
    global main_journal
    students_book.append(new_student)
    student = ' '.join(new_student)
    main_journal[student] = {}
    for les in lesson_book:
        main_journal[student][les] = []

def open_file_les():
    global path_les
    global lesson_book
    with open(path_les, 'r', encoding='utf-8') as data: # преобразую в utf-8, иначе ошибка (кириллица)
        file = data.readlines()
    for les in file:
        lesson_book.append(les.strip())

def save_file_les():
    global path_les
    global lesson_book
    with open(path_les, 'w', encoding='utf-8') as data: # преобразую в utf-8, иначе ошибка (кириллица)
        data.writelines('\n'.join(lesson_book))

def close_file_les():
    global lesson_book
    lesson_book = []

def add_les(les: str):
    global students_book
    global lesson_book
    global main_journal
    lesson_book.append(les.lower())
    for name in students_book:
        student = ' '.join(name)
        main_journal[student] = {}
        for lesson in lesson_book:
            main_journal[student][lesson] = []

def search_contact(find: str) -> list:
    global students_book
    result = []
    for student in students_book:
        for field in student:
            if find in field:
                result.append(student)
                break
    return result
    
def add_mark(name: str, less: str, mark: str):
    global students_book
    global lesson_book
    global main_journal
    main_journal[name][less].append(mark)

def save_journal():
    global main_journal
    main_journal = {"r":{"m":[2,3,4]},"t":{"m":[5]}}
    # with open("school1/journal.txt", 'w', encoding='utf-8') as data: # преобразую в utf-8, иначе ошибка (кириллица)
    # for keyOUT, valueOUT in main_journal.items():
    #     student_string = ""
    #     student_string += str(keyOUT)+" "
    # for keyIN,valueIN in valueOUT.items():
    #     student_string += str(keyIN)+" "+" ".join(map(str,valueIN))
    #     data.writelines(student_string+"\n")

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

def get_student_journal(find_cont: str):
    global main_journal
    result = []
    for key, values in main_journal.items():
        if find_cont in key:
            result.append(main_journal.get(key, values))
            break
    if len(result) > 1: # если в список по поиску для удаления добавились больше 1 строки, то мы не можем удалить
        return False
    elif result == []:
        return result
    else:
        return result

def show_student_journal(student):
    global main_journal
    return main_journal[student]