# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента 
# достаются сделавшему последний ход.

# a) Добавьте игру против бота (где бот берет рандомное количество конфет от 0 до 28)
# b) Подумайте как наделить бота 'интеллектом' (алгоритм, позволяющий выяснить какое количесвто конфет необходимо брать, чтобы гарантированно победить)

from random import randint as RI

# игрок против игрока

all_candies = (int(input('Введите общее количество конфет: ')))

player_1 = 1
player_2 = 2

def draw_lot() -> int:
    lot = RI(1,2)
    print(f'Первый ход за игроком под № {lot}')
    return lot 

def take_candy(candies):
    count = (int(input('Сколько вы возьмете конфет? За один ход можно забрать не более чем 28 конфет: ')))
    while count > 28 or 0 >= count:
        count = (int(input(f'Попробуйте еще раз (За один ход можно забрать конфет не более чем {candies if candies < 28 else 28} шт.): ')))
    while (candies - count) < 0:
        count = (int(input(f'Вы не можете взять больше конфет, чем {candies} шт. Попробуйте еще: ')))
    return count


def candy_game(candies):
    lot = draw_lot()
    count = candies
    while count > 0:
        if lot == player_1:
            print(f'ход игрока под № - {player_1}')
            count = count - take_candy(count)
            if count == 0:
                print(f'Победил игрок - {player_1}. Ему достались все конфеты в количестве {candies} шт.')
            print(f'На столе осталось {count} конфет')
            lot = player_2
        else:
            print(f'ход игрока под № - {player_2}')
            count = count - take_candy(count)
            if count == 0:
                print(f'Победил игрок - {player_2}. Ему достались все конфеты в количестве {candies} шт.')
            print(f'На столе осталось {count} конфет')
            lot = player_1

candy_game(all_candies)
            



# бот


# интеллект
