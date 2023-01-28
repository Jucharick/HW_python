def convert_expression(my_srt) -> list:
    my_srt= my_srt.replace(' ', '').replace('+', ' + ').replace('-', ' - ').replace('/', ' / ').replace('*', ' * ')
    if my_srt[1] == ('-'):
        my_srt = '-' + my_srt[3:]
    my_list = my_srt.split()
    return my_list

def calculate(my_list, operation_1, operation_2):
    operation = {'+': lambda x, y: x+y,
             '-': lambda x, y: x-y,
             '*': lambda x, y: x*y,
             '/': lambda x, y: x/y,}
    i = 0
    while operation_1 in my_list or operation_2 in my_list:
        if my_list[i] in [operation_1, operation_2]:
            my_list[i - 1] = operation.get(my_list[i])(int(my_list[i - 1]), int(my_list[i + 1]))
            my_list.pop(i)
            my_list.pop(i)
        else:
            i+=1
    return my_list

