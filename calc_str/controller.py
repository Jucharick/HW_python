import view
import model

def start():
    get_str = view.get_expression()
    get_list = model.convert_expression(get_str)
    orig_example = get_list.copy()
    while len(get_list) > 1:
        model.calculate(get_list, '*', '/')
        model.calculate(get_list, '+', '-')
    view.output(orig_example, get_list)