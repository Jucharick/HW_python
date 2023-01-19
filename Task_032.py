# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента 
# достаются сделавшему последний ход.

# a) Добавьте игру против бота (где бот берет рандомное количество конфет от 0 до 28)
# b) Подумайте как наделить бота 'интеллектом' (алгоритм, позволяющий выяснить какое количесвто конфет необходимо брать, чтобы гарантированно победить)

from random import randint as RI



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


# игрок против игрока

# def candy_game(candies):
#     lot = draw_lot()
#     count = candies
#     while count > 0:
#         if lot == player_1:
#             print(f'ход игрока под № - {player_1}')
#             count = count - take_candy(count)
#             if count == 0:
#                 print(f'Победил игрок - {player_1}. Ему достались все конфеты в колличестве {candies} шт.')
#             print(f'На столе осталось {count} конфет')
#             lot = player_2
#         else:
#             print(f'ход игрока под № - {player_2}')
#             count = count - take_candy(count)
#             if count == 0:
#                 print(f'Победил игрок - {player_2}. Ему достались все конфеты в колличестве {candies} шт.')
#             print(f'На столе осталось {count} конфет')
#             lot = player_1
            

# бот

# def candy_game(candies):
#     lot = draw_lot()
#     count = candies
#     while count > 0:
#         if lot == player_1:
#             count_bot = RI(1,29)
#             while count_bot > count:
#                 count_bot = RI(1,29)
#             print(f'ход Глупого робота. Он взяд {count_bot} шт.')
#             count = count - count_bot
#             if count == 0:
#                 print(f'Победил Глупый робот. Ему достались все конфеты в колличестве {candies} шт.')
#             print(f'На столе осталось {count} конфет')
#             lot = player_2
#         else:
#             print(f'ход Человека')
#             count = count - take_candy(count)
#             if count == 0:
#                 print(f'Победил Человек. Ему достались все конфеты в колличестве {candies} шт.')
#             print(f'На столе осталось {count} конфет')
#             lot = player_1


# интеллект

def candy_game(candies):
    lot = draw_lot()
    max_sweet = 28
    count = candies
    while count > 0:
        if lot == player_1:
            if count <= max_sweet:
                count_bot = count
            elif count % max_sweet == 0: # count % max_sweet если четное, то должен взять столько, чтоб в полследнем ходе противника осталось 28+1 конфета 
                count_bot = max_sweet - 1
            else:
                count_bot = count % max_sweet - 1
            print(f'ход "Умного" робота. Он взяд {count_bot} шт.')
        # exit()
            count = count - count_bot
            if count == 0:
                print(f'Победил "Умный" робот. Ему достались все конфеты в колличестве {candies} шт.')
            print(f'На столе осталось {count} конфет')
            lot = player_2
        else:
            print(f'ход Человека')
            count = count - take_candy(count)
            if count == 0:
                print(f'Победил Человек. Ему достались все конфеты в колличестве {candies} шт.')
            print(f'На столе осталось {count} конфет')
            lot = player_1


candy_game(all_candies)