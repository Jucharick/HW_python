def get_expression():
    in_str = input('Введите арифметическое выражение (используйте операции +, -, /, *): ')
    return in_str

def output(orig_example, my_list):
    print(f'{" ".join(orig_example)} = {my_list[0]}')