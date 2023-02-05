# python -m venv venv
# установить библиотеку pip install pytelegrambotapi
# обновить библиотеку pip3 install pytelegrambotapi --upgrade


import telebot
from telebot import types
import random

bot = telebot.TeleBot('')
print('Бот запущен')

flag = 0
cal_list = []
orig_example = []
operation = {'+': lambda x, y: x+y,
                     '-': lambda x, y: x-y,
                     '*': lambda x, y: x*y,
                     '/': lambda x, y: x/y,
                     '//': lambda x, y: x//y,
                     '%': lambda x, y: x%y}

@bot.message_handler(commands=['start', 'старт'])
def mes_start(message: types.Message):
    name = message.from_user.first_name
    bot.send_message(message.chat.id, f'{name}, привет! Посчитаем?'
                                      f'\nДля комплексных чисел жми /complex'
                                      f'\nДля ряциональных чисел жми /int')

@bot.message_handler(commands=['complex'])
def cal_complex(message: types.Message):
    global flag
    global cal_list
    global orig_example
    flag = 1
    bot.send_message(message.chat.id, f'Введите выражение с комплексными числами (используйте i)')

@bot.message_handler(commands=['int'])
def calc_int(message: types.Message):
    global flag
    global cal_list
    global orig_example
    flag = 0
    bot.send_message(message.chat.id, f'Введите выражение с рациональными числами')

def calculate(operation_1, operation_2):
    global cal_list
    i = 0
    while operation_1 in cal_list or operation_2 in cal_list:
        if cal_list[i] in [operation_1, operation_2]:
            cal_list[i - 1] = operation.get(cal_list[i])(int(cal_list[i - 1]), int(cal_list[i + 1]))
            cal_list.pop(i)
            cal_list.pop(i)
        else:
            i+=1

def calculate_complex(operation_1, operation_2):
    global cal_list
    i = 0
    while operation_1 in cal_list or operation_2 in cal_list:
        if cal_list[i] in [operation_1, operation_2]:
            cal_list[i - 1] = operation.get(cal_list[i])(complex(cal_list[i - 1]), complex(cal_list[i + 1]))
            cal_list.pop(i)
            cal_list.pop(i)
        else:
            i+=1

def save_log(message: types.Message):
    path = 'telebot_calc/log.txt'
    data = open(path, 'w', encoding='utf-8') # преобразую в utf-8, иначе ошибка (кириллица)
    data.writelines(f'{message.from_user.first_name}   {message.text}')
    data.close()

@bot.message_handler()
def calc (message: types.Message):
    global flag
    global cal_list
    global orig_example
    calc_str = message.text
    nums = calc_str.replace('+', ' + ') \
                   .replace('-', ' - ') \
                   .replace('*', ' * ') \
                   .replace('/', ' / ') \
                   .replace('i', 'j') \
                   .split()
    for i in range(len(nums)-1):
        if nums[0] == '-':
            nums[1] = '-' + nums[1]
            nums.pop(0)
        if nums[i]=='/':
            if nums[i+1]=='/':
                nums[i] = '//'
                del(nums[i+1])
    for el in nums:
        if 'j' in el:
            cal_list.append(complex(el))
        elif el.isdigit():
            cal_list.append(int(el))
        else:
            cal_list.append(el)
    if flag:
        if '//' in cal_list or '%' in cal_list:
            bot.send_message(message.chat.id,f'Ошибка. С комплексными числами нельзя проводить операции // or %. '
                                            f'\nДля комплексных чисел жми /complex'
                                            f'\nДля ряциональных чисел жми /int')
            cal_list = []
        else:
            while len(cal_list) > 1:
                calculate_complex('*', '/')
                calculate_complex('+', '-')  
            bot.send_message(message.chat.id,f'{cal_list[0]}')    
    else:
        # for фиксирует длину списка один раз и после del не проверяет длину списка снова (а она у нас уменьшается)
        # while при каждой итерации проверяет длину списка
        while len(cal_list) > 1:
            calculate('//', '%')
            calculate('*', '/')
            calculate('+', '-')
        bot.send_message(message.chat.id,f'{cal_list[0]}')
    save_log(message)
    cal_list = []

            
bot.infinity_polling() # бот проверяет не пришли ли какие-то сообщения    


