from aiogram import types
from loader import dp
import random

max_count = 221 # по умолчанию, через команду /set можео изменить количество конфет в игре
total = 0
new_game = False # флаг
duel = [] # список id - мой (кто вызвал на поединок) и оппонента
first_turn = 0
current = 0

@dp.message_handler(commands=['start', 'старт'])
async def mes_start(message: types.Message):
    name = message.from_user.first_name
    await message.answer(f'{name}, привет! Сыграем в конфеты? Для начала игры введи команду /new_game . '
                         f'\nЕсли хочешь сыграть в поединок -> введи команду /duel и укажи id оппонента через пробел. '
                         f'\nЧтобы изменить количество конфет в игре введи команду /set и укажи новое количесво конфет через пробел (по умолчанию количество = 221)'
                         f'\nЧтобы узнать правила игры введи команду /help')
    print(message.from_user.id) # приходит id того, кто отправил комманду /start

@dp.message_handler(commands=['help'])
async def mes_help(message: types.Message):
    await message.answer(f'Бог поможет, бери конфеты (от 1 до 28)')

@dp.message_handler(commands=['new_game'])
async def mes_new_game(message: types.Message):
    global new_game
    global max_count
    global total
    new_game = True
    total = max_count
    first_turn = random.randint(0,1)
    if first_turn:
        await message.answer(f'Начнем игру! По жребию первым ходит {message.from_user.first_name}! Бери конфеты (от 1 до 28)')
    else: 
        await message.answer(f'Начнем игру! По жребию первым ходит Умный бот')
        await bot_turn(message) # вызываем ход нашего Умного бота

@dp.message_handler(commands=['duel'])
async def mes_duel(message: types.Message):
    global new_game
    global max_count
    global total
    global duel
    global first_turn
    global current
    player = int(message.from_user.id)
    duel.append(player) # мой id (кто вызвал на поединок)
    opponent = int(message.text.split()[1]) # добавляем split()[1] правую часть команды /duel id
    duel.append(opponent) # id оппонента
    total = max_count
    first_turn = random.randint(0,1)
    if first_turn:
        await dp.bot.send_message(duel[0], f'Первый ход за тобой! Бери конфеты (от 1 до 28)')
        await dp.bot.send_message(duel[1], f'Первый ход за твоим противником. Жди своего хода.')
    else: 
        await dp.bot.send_message(duel[1], f'Первый ход за тобой! Бери конфеты (от 1 до 28)')
        await dp.bot.send_message(duel[0], f'Первый ход за твоим противником. Жди своего хода.')
    current = duel[0] if first_turn ==1 else duel[1]
    new_game = True

# /set 200 -> чтобы обратиться к 200 мы делаем split() и обращаемся к элементу с индексом [1]
@dp.message_handler(commands=['set'])
async def mes_set(message: types.Message):
    global max_count
    global new_game
    name = message.from_user.first_name
    count = message.text.split()[1]
    if not new_game:
        if count.isdigit():
            max_count = int(count)
            await message.answer(f'Теперь конфет в игре будет {max_count}')
        else:
            await message.answer(f'{name}, напишите цифрами')
    else:
        await message.answer(f'{name}, нельзя менять правила во время игры')

@dp.message_handler() # жадный handler, ловит все ходы 
async def mes_take_candy(message: types.Message):
    global new_game
    global max_count
    global total
    global duel
    global first_turn
    global current
    name = message.from_user.first_name
    count = message.text
    if len(duel) == 0:
        if new_game:
            if count.isdigit() and 0 < int(count) < 29:
                total -= int(count)
                if total <= 0:
                    await message.answer(f'Ура, {name} победил !!!')
                    new_game = False
                else:
                    await message.answer(f'{name} взяла {count} конфет. '
                                        f'На столе осталось {total} конфет. ')
                    await bot_turn(message) # вызываем ход нашего Умного бота
            else:
                await message.answer(f'{name}, надо указать ЧИСЛО от 1 до 28. Соблюдай правила и не тупи!')
    else:
        if current == message.from_user.id:
            name = message.from_user.first_name
            count = message.text
            if new_game:
                if count.isdigit() and 0 < int(count) < 29:
                    total -= int(count)
                    if total <= 0:
                        await message.answer(f'Ура, {name} победил !!!')
                        await dp.bot.send_message(opponent_id(), f'К сожалению ты проиграл, твой оппонент оказался умнее. Думай! прежде чем сделать ход')
                        new_game = False
                    else:
                        await message.answer(f'{name} взяла {count} конфет. '
                                            f'На столе осталось {total} конфет. ')
                        await dp.bot.send_message(opponent_id(), f'Теперь твой ход, бери конфеты. На столе осталось {total} конфет. ')
                        switch_players() # вызываем ход второго игрока
                else:
                    await message.answer(f'{name}, надо указать ЧИСЛО от 1 до 28. Соблюдай правила и не тупи!')

def switch_players():
    global duel
    global current
    if current == duel[0]: # меняем id - ход игроков
        current = duel[1]
    else:
        current = duel[0]

def opponent_id():
    global duel
    global current
    if current == duel[0]: # меняем id - ход игроков
        return duel[1] # не присваивает как switch_players(), а возвращает противоположное значение (для отправки сообщения другому игроку)
    else:
        return duel[0] # не присваивает как switch_players(), а возвращает противоположное значение (для отправки сообщения другому игроку)

async def bot_turn(message: types.Message):
    global total
    global new_game
    bot_take = 0
    if 0 < total < 29:
        bot_take = total
        total -= bot_take
        await message.answer(f'Умный бот взял {bot_take} конфет. '
                             f'На столе осталось {total} конфет и Умный бот победил')
        new_game = False
    elif total%(28+1) == 0:
        bot_take = 28
        total -= bot_take
        await message.answer(f'Умный бот взял {bot_take} конфет. '
                            f'На столе осталось {total} конфет. ')
    else:
        bot_take = total%(28+1)
        total -= bot_take
        await message.answer(f'Умный бот взял {bot_take} конфет. '
                            f'На столе осталось {total} конфет. ')
        