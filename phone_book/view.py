commands = ['Открыть файл',
            'Сохранить файл',
            'Показать все контакты',
            'Создать контакт',
            'Удалить контакт',
            'Изменить контакт',
            'Найти контак',
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


def show_contacts(phone_list: list):
    if len(phone_list) < 1:
        print('Телефонная книга пуста или не открыта')
    else:
        print()
        for i, contact in enumerate(phone_list, 1):
            print(f'\t{i}. {contact[0]:30} {contact[1]:13} {contact[2]}')
    print()
        
def create_contact():
    name = input('Введите ФИО: ')
    phone = input('Введите номер телефона: ')
    comment = input('Укажите комментарий: ')
    return name, phone, comment

def select_contact(message: str):
    cont = input(message)
    return cont

def change_contact():
    print('Введите новые данные (если изменения не требуются нажмите Enter): ')
    name = input('Введите ФИО: ')
    phone = input('Введите номер телефона: ')
    comment = input('Укажите комментарий: ')
    return name, phone, comment

def delete_confirm(contact: str):
    result = input(f'Вы действительно хотите удалить {contact} (y/n)? ').lower()
    if result == 'y':
        return True
    else:
        return False

def find_contact():
    find = input('Введите искомый элемент: ')
    return find

def end_prog():
    print()
    print('Работа в программе завершена')
    print()

def empty_request():
    print()
    print('Искомый контакт не найден')
    print()

def many_request():
    print()
    print('Найденных контактов больше 1. Введите более точные данные')
    print()

def information(message):
    print(message)