# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи


num = int(input('Введите число k: '))
res = []
list_1 = [0, 1]
for i in range(2, num+1):
    list_1.append(list_1[i-2] + list_1[i-1])
list_2 = [1, 0]
for i in range(2, num+1):
    list_2.insert(0, list_2[i-len(list_2)+1] - list_2[i-i])
negafibonacci = list_2 + list_1
negafibonacci.remove(0)
print(negafibonacci)
