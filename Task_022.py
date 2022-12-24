# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10


num = int(input('Введите число: '))
num_2 = num

# список
res = []
print(f'{num}  => ', end = ' ')
while int(num) > 0:
    res.insert(0, (int(num % 2))) # insert() - добавляет элемент на указанный индекс (в данном случае на индекс 0)
    num = num / 2
for i in res:
    print(i, end = '')
print()

# строка
my_str = ''
print(f'{num_2} ', end = ' ')
while int(num_2) > 0:
    my_str = str(num_2 % 2) + my_str # добавляю в начало строки my_str
    num_2 = num_2 // 2
print(f'=>  {my_str}')