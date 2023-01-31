# python -m venv venv
# установить библиотеку pip install pytelegrambotapi
# обновить библиотеку pip3 install pytelegrambotapi --upgrade


import telebot
from telebot import types
import random

bot = telebot.TeleBot('')
print('Бот запущен')

max_count = 99 # по умолчанию, через команду /set можео изменить количество конфет в игре
total = 0
new_game = False
first_turn = 0

@bot.message_handler(commands=['start', 'старт'])
def mes_start(message: types.Message):
    name = message.from_user.first_name
    bot.send_message(message.chat.id, f'{name}, привет! Сыграем в конфеты? Для начала игры введи команду /new_game . '
                                      f'\nЧтобы изменить количество конфет в игре введи команду /set и укажи новое количесво конфет через пробел (по умолчанию количество = 99)'
                                      f'\nЧтобы узнать правила игры введи команду /help')

@bot.message_handler(commands=['help'])
def mes_help(message: types.Message):
    name = message.from_user.first_name
    bot.send_message(message.chat.id, f'{name}, Бог тебе поможет, жми /new_game ')

@bot.message_handler(commands=['new_game'])
def mes_new_game(message: types.Message):
    global new_game
    global max_count
    global total
    global first_turn
    new_game = True
    total = max_count
    first_turn = random.randint(0,1)
    if first_turn:
        bot.send_message(message.chat.id, f'Начнем игру! По жребию первым ходит {message.from_user.first_name}! Бери конфеты (от 1 до 28)')
    else: 
        bot.send_message(message.chat.id, f'Начнем игру! По жребию первым ходит Умный бот')
        bot_turn(message)

# /set 200 -> чтобы обратиться к 200 мы делаем split() и обращаемся к элементу с индексом [1]
@bot.message_handler(commands=['set'])
def mes_set(message: types.Message):
    global max_count
    global new_game
    name = message.from_user.first_name
    if len(message.text.split()) > 1:
        count = message.text.split()[1]
        if not new_game:
            if count.isdigit():
                max_count = int(count)
                bot.send_message(message.chat.id, f'Теперь конфет в игре будет {max_count}, жми /new_game ')
            else:
                bot.send_message(message.chat.id, f'{name}, напишите цифрами')
        else:
            bot.send_message(message.chat.id, f'{name}, нельзя менять правила во время игры')
    else:
        bot.send_message(message.chat.id, f'После команды /set нужно через пробел поставить новое количество конфет. Количество конфет не изменено, пробуй еще раз')

@bot.message_handler()
def mes_take_candy(message: types.Message):
    global total
    global new_game
    name = message.from_user.first_name
    count = message.text # обращаемся к полю текст
    if new_game:
        if count.isdigit() and 0 < int(count) < 29:
            total -= int(count)
            if total <= 0:
                bot.send_message(message.chat.id, f'Ура, {name} победил !!!')
                new_game = False
            else:
                bot.send_message(message.chat.id, f'{name} взяла {count} конфет. '
                                                  f'На столе осталось {total} конфет. ')
                bot_turn(message)
        else:
            bot.send_message(message.chat.id, f'{name}, надо указать ЧИСЛО от 1 до 28. Соблюдай правила и не тупи!')
        
def bot_turn(message):
    global total
    global new_game
    bot_take = 0
    if 0 < total < 29:
        bot_take = total
        total -= bot_take
        bot.send_message(message.chat.id, f'Умный бот взял {bot_take} конфет. '
                                          f'На столе осталось {total} конфет и Умный бот победил')
        new_game = False
    elif total%(28+1) == 0:
        bot_take = 28
        total -= bot_take
        bot.send_message(message.chat.id, f'Умный бот взял {bot_take} конфет. '
                                          f'На столе осталось {total} конфет. ')
    else:
        bot_take = total%(28+1)
        total -= bot_take
        bot.send_message(message.chat.id, f'Умный бот взял {bot_take} конфет. '
                                          f'На столе осталось {total} конфет. ')


bot.infinity_polling() # бот проверяет не пришли ли какие-то сообщения    



# #на столе лежит...
# import telebot
# import random

# bot = telebot.TeleBot("6185618554:AAGS8T5BvicTGRTkGKp3HGAq0HPYLnln8UM")

# flag = None
# sweets = 60
# max_sweet = 28

# @bot.message_handler(commands=["start"])
# def start(message):
#     global flag
#     bot.send_message(message.chat.id, f"Приветствую вас в игре!")
#     flag = random.choice(["user", "bot"])
#     bot.send_message(message.chat.id, f"Всего в игре {sweets} конфет")
#     if flag == "user":
#         bot.send_message(message.chat.id,f"Первым ходите вы")  # отправка сообщения (кому отправляем, что отправляем(str))
#     else:
#         bot.send_message(message.chat.id,f"Первым ходит бот")# отправка сообщения (кому отправляем, что отправляем(str))
#     controller(message)

# def controller(message):
#     global flag
#     if sweets > 0 :
#         if flag == "user":
#             bot.send_message(message.chat.id, f"Ваш ход введите кол-во конфет от 0 до {max_sweet}")
#             bot.register_next_step_handler(message,user_input)
#         else:
#             bot_input(message)
#     else:
#         flag = "user" if flag == "bot" else "bot"
#         bot.send_message(message.chat.id, f"Победил {flag}!")

# def bot_input(message):
#     global sweets, flag
#     if sweets <= max_sweet:
#         bot_turn = sweets
#     elif sweets % max_sweet == 0:
#         bot_turn = max_sweet - 1
#     else:
#         bot_turn = sweets % max_sweet - 1
#     sweets -= bot_turn
#     bot.send_message(message.chat.id, f"бот взял {bot_turn} конфет")
#     bot.send_message(message.chat.id, f"осталось {sweets}")
#     flag = "user" if flag == "bot" else "bot"
#     controller(message)