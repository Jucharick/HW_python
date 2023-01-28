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



def get_student():
    input('Введите имя ')
    input('Введите фамилию ')

def get_journal():
    input('Введите предмет ')
    input('Введите оценку ')






def end_prog():
    print()
    print('Работа в программе завершена')
    print()