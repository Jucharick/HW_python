commands = ['Показ списка учеников',
            'Добаить нового студента (поля: имя, фамилия)',
            'Добаить предмет',
            'Добаить оценку ученику',
            'Редактировать данные ученика',
            'Удалить ученика',
            'Показ листа оценок конкретного ученика',
            'Выход из программы']

def menu():
    print('Главное меню:')
    for i, item in enumerate(commands, 1):
        print(f'\t{i}. {item}') # \t табуляция 
    while True:
        try: # try except пробует преобразовать input в int и если пользователь вводит букву или символ => ValueError: print('Введите корректное значение')
            request = int(input('Выберите пункт меню: '))
            if 0 < request < 9:
                return request
            else:
                print('Введите значение от 1 до 8')
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

def select_student(message: str):
    student = input(message)
    return student

def delete_confirm(student: str):
    result = input(f'Вы действительно хотите удалить {student} (y/n)? ').lower()
    if result == 'y':
        return True
    else:
        return False

def change_student():
    print('Введите новые данные (если изменения не требуются нажмите Enter): ')
    id = input('Введите id: ')
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    return id, name, surname

def empty_request():
    print()
    print('Искомый контакт не найден')
    print()

def many_request():
    print()
    print('Найденных контактов больше 1. Введите более точные данные')
    print()

# def get_student():
#     input('Введите имя ')
#     input('Введите фамилию ')

# def get_journal():
#     input('Введите предмет ')
#     input('Введите оценку ')






def end_prog():
    print()
    print('Работа в программе завершена')
    print()

def information(message):
    print(message)