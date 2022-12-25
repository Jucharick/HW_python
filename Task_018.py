# Реализуйте алгоритм перемешивания списка.

# SHUFFLE
import random

number = int(input('Введите число элементов: '))
my_list = []

for i in range(number):
    my_list.append(i)
print(my_list)
random.shuffle(my_list)
print(my_list)


# через замену местами 
from random import randint

num = int(input('Введите число элементов: '))
my_list1 = []
for i in range(num):
    my_list1.append(i)
print(my_list1)
for i in range(num):
    new_i = randint(0, num - 1) # при использовании этого метода есть вероятность что элементы заменятся сами на себя
    temp = my_list1[i]
    my_list1[i] = my_list1[new_i]
    my_list1[new_i] = temp
print(my_list1)

# вариант преподавателя
import datetime

def random_int(num):
    rand = datetime.datetime.now().microsecond/10**6  # datetime.datetime.now().microsecond вернет микросекунды;  делим на миллион, потому что нам надо получить дробь
    return int(num*rand)

list_num = [i for i in range(number+1)] # создаем список от 0 до введенного number
print(list_num)

for i in range((len(list_num)-1), -1, -1): # идем до -1 потому что range не включает последний элемент
    j = random_int(i+1)
    list_num[i], list_num[j] = list_num[j], list_num[i] # замена местами элементов как в C# через temp

print(list_num)

