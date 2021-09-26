
def is_float_number(n:str, value=None):
    try:
        k = float(n)
    except ValueError:
        return False
    return True


def is_int_number(n:str, value=None):
    try:
        k = int(n)
    except ValueError:
        return False
    return True


def is_natural_number(n:str, value=None):
    return is_int_number(n, None) and int(n) > 0


def is_menu(n:str, value=None):
    return n == '1' or n == '2' or n == 'exit'


def is_greater_then(n:str, value:[]):
    if not is_int_number(n):
        return False
    k = float(n)
    for i in value:
        if k <= i:
            return False
    return True


def is_valid_array(n: str, conditional: []):
    if conditional[0] is None:
        return True
    s = []
    if conditional[1] == -1:
        s = n.split(conditional[2])
    else:
        s = n.split(conditional[2])[:conditional[1]]
        if len(s) < conditional[1]:
            return False
    for i in s:
        if not conditional[0](i):
            return False
    return True


def is_valid(n: str, additional_condition=None, value_for_conditional=None):
    if additional_condition is None:
        return True
    return additional_condition(n, value_for_conditional)


def input_validation(text="", additional_condition=None, *value_for_conditional):
    slesh_n = '\n'
    print(text, end=f'{slesh_n if text != "" else ""}')
    while True:
        try:
            n = input()
            n = n.strip()
            if not is_valid(n, additional_condition, value_for_conditional):
                int('error')
            return n
        except ValueError:
            print('не правильний ввід, спробуйте йще раз')
        except KeyboardInterrupt:
            print('Програма завершила свою роботу')
            exit()


def array_input(text="", size=-1, additional_condition=None, type=str, split_symbol=' '):
    func = lambda x: type(x.strip())
    list_ = input_validation(text, is_valid_array, additional_condition, size, split_symbol).split(split_symbol)
    if size != -1:
        list_ = list_[:size]
    list_ = list(map(func, list_))
    return list_
