# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


for x in range(2):
    for y in range(2):
        for z in range(2):
            print(not (x or y or z) == (not x and not y and not z))

print()
# вариант преподавателя
for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            expression = not (x or y or z) == (not x and not y and not z)
            print(f'{x}, {y}, {z},   =>  результат {expression}')