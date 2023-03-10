commands = ['Показ списка учеников',
            'Добавить нового студента (поля: имя, фамилия)',
            'Добавить предмет',
            'Добавить оценку ученику',
            'Редактировать данные ученика',
            'Удалить ученика',
            'Показ листа оценок конкретного ученика',
            'Показать весь журнал',
            'Выход из программы']




def menu():
    print('Главное меню:')
    for i, item in enumerate(commands, 1):
        print(f'\t{i}. {item}') # \t табуляция 
    while True:
        try: # try except пробует преобразовать input в int и если пользователь вводит букву или символ => ValueError: print('Введите корректное значение')
            request = int(input('Выберите пункт меню: '))
            if 0 < request < 10:
                return request
            else:
                print('Введите значение от 1 до 9')
        except ValueError:
            print('Введите корректное значение')

def show_students(student_list: list):
    if len(student_list) < 1:
        print('Список учеников пуст')
    else:
        print()
        for i, student in enumerate(student_list, 1):
            print(f'\t{i}. {student[0]:5} {student[1]:10} {student[2]:15}')
    print()

def create_student():
    id = input('Введите id: ')
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    return id, name, surname

def add_lesson():
    les = input('Введите название предмета: ')
    return les

def get_mark():
    name = input('Введите имя: ')
    less = input('Введите предмет: ')
    mark = input('Введите оценку: ')
    return name, less.lower(), mark

def select_student(message: str):
    student = input(message)
    return student

def delete_confirm(student: str):
    result = input(f'Вы действительно хотите удалить {student} (y/n)? ').lower()
    if result == 'y':
        return True
    elif result == 'n':
        print('Операция отменена')
        return False
    else:
        print('Вы ввели некорректное значение')

def change_student():
    print('Введите новые данные (если изменения не требуются нажмите Enter): ')
    id = input('Введите id: ')
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    return id, name, surname

def show_journal(journal):
    if len(journal) < 1:
            print('Список учеников пуст')
    else:
        print()
        for key, value in journal.items():
            print(f'\t{key} {value}')
    print()

def empty_request():
    print()
    print('Искомый контакт не найден')
    print()

def many_request():
    print()
    print('Найденных контактов больше 1. Введите более точные данные')
    print()

def end_prog():
    print()
    print('Работа в программе завершена')
    print()

def information(message):
    print(message)