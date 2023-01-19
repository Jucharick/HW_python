# игра в 'Крестики-нолики'

from random import randint as RI

maps = [1, 2, 3, 4, 5, 6, 7, 8, 9]
victories = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

def print_maps():
    print(maps[0], end=' ')
    print(maps[1], end=' ')
    print(maps[2]) # переходим на следующую строку

    print(maps[3], end=' ')
    print(maps[4], end=' ')
    print(maps[5])

    print(maps[6], end=' ')
    print(maps[7], end=' ')
    print(maps[8])


print_maps()

player_1 = 1
player_2 = 2

def draw_lot() -> int:
    lot = RI(1,2)
    print(f'Первый ход за игроком под № {lot}')
    return lot 

def check_victories():
    for i in victories:
        if maps[i[0]] == maps[i[1]] == maps[i[2]]:
            return True
    return False

def tic_tac_toe():
    lot = draw_lot()
    count = 0
    while True:
        if lot == player_1:
            print(f'ход игрока под № - {player_1}. Он ходит Х')
            symbol = 'X'
            step = int(input('Введи номер клетки - хода: '))
            while maps[step-1] == 'X' or maps[step-1] == 'O':
                print ('Клетка занята')
                step = int(input('Введи номер клетки - хода: '))
            maps[step-1] = symbol
            print_maps()
            if check_victories():
                print(f'Победил игрок № {player_1}')
                break
            lot = player_2

        else:
            print(f'ход игрока под № - {player_2}. Он ходит О')
            symbol = 'O'
            step = int(input('Введи номер клетки - хода: '))
            while maps[step-1] == 'X' or maps[step-1] == 'O':
                print ('Клетка занята')
                step = int(input('Введи номер клетки - хода: '))
            maps[step-1] = symbol
            print_maps()
            if check_victories():
                print(f'Победил игрок № {player_2}')
                break
            lot = player_1
        count +=1
        if count == 9:
            print(f'Ничья!')
            break

tic_tac_toe()