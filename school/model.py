# 1. Показ списка учеников
# 2. Добаить нового студента (поля: имя, фамилия)
# 3. Добавить предмет
# 4. Добаить оценку ученику
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
    open_file()
    open_file_les()
    students_book.append(new_student)
    student = ' '.join(new_student)
    main_journal[student] = {}
    print(main_journal)
    for les in lesson_book:
        main_journal[student][les] = []
    print(main_journal)
    save_file()
    close_file()
    close_file_les()

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
    open_file()
    open_file_les()
    if les not in lesson_book:
        lesson_book.append(les)
        for name in students_book:
            student = ' '.join(name)
            main_journal[student] = {}
            for lesson in lesson_book:
                main_journal[student][lesson] = []
    print(main_journal)
    save_file_les()
    close_file()
    close_file_les()

def search_contact(find: str) -> list:
    global students_book
    open_file()
    result = []
    for student in students_book:
        for field in student:
            if find in field:
                result.append(student)
                break
    close_file()
    return result
    
def add_mark(name: str, less: str, mark: str):
    global students_book
    global lesson_book
    global main_journal
    open_file()
    open_file_les()
    for stud in students_book:
            student = ' '.join(stud)
            main_journal[student] = {}
            for lesson in lesson_book:
                main_journal[student][lesson] = []
    main_journal[name][less].append(mark)
    print(main_journal)
    close_file()
    close_file_les()

def save_journal():
    global main_journal
    for key, value in main_journal.items():
        with open(path_journal, 'w', encoding='utf-8') as data: # преобразую в utf-8, иначе ошибка (кириллица)
            data.writelines(' '.join(main_journal.get(key)))

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

