# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.


num = int(input('Введите целое число: '))
#numbers = list(range(-1*num, num+1))
numbers = [i for i in range(-num, num+1)] # альтернативная запись создания списка
print(numbers)


data = open('file.txt', 'w') # открытие на запись
for  line in range(2):
    data.writelines(f"{int(input('Введите позию элемента: '))} \n")
data.close()

data = open('file.txt', 'r') # открытие на чтение
positions = []
for line in data:
    positions.append(int(line))
data.close()

mult = 1
for i in range(len(positions)):
    index = positions[i]
    print(f'Число с индексом {index} = {numbers[index]}')
    mult = mult * numbers[index]
print(f'произведение элементов на указанных позициях => {mult}')
