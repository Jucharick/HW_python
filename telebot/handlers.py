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
    new_game = True
    total = max_count
    first_turn = random.randint(0,1)
    if first_turn:
        bot.send_message(message.chat.id, f'Начнем игру! По жребию первым ходит {message.from_user.first_name}! Бери конфеты (от 1 до 28)')
    else: 
        bot.send_message(message.chat.id, f'Начнем игру! По жребию первым ходит Умный бот')
        bot.register_next_step_handler(message, bot_turn) # вызываем ход нашего Умного бота 

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
    count = message.text
    if new_game:
        if count.isdigit() and 0 < int(count) < 29:
            total -= int(count)
            if total <= 0:
                bot.send_message(message.chat.id, f'Ура, {name} победил !!!')
                new_game = False
            else:
                bot.send_message(message.chat.id, f'{name} взяла {count} конфет. '
                                                  f'На столе осталось {total} конфет. ')
                bot.register_next_step_handler(message, bot_turn) # вызываем ход нашего Умного бота
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