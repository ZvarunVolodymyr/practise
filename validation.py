def is_str(n:str, value=None):
    return n

def is_float_number(n:str, value=None):
    try:
        return float(n)
    except ValueError:
        raise ValueError


def is_int_number(n:str, value=None):
    try:
        return int(n)
    except ValueError:
        raise ValueError


def is_natural_number(n:str, value=None):
    if not(is_int_number(n) and int(n) > 0):
        raise ValueError
    return int(n)


def is_menu(n:str, value=None):
    if n != '1' and n != '2' and n != 'exit':
        raise ValueError
    return n


def is_greater_then(n:str, value:[]):
    k = is_int_number(n)
    for i in value:
        if k <= i:
            raise ValueError
    return k


def is_valid_array(n: str, conditional: []):
    s = []
    if conditional[1] == -1:
        s = n.split(conditional[2])
    else:
        s = n.split(conditional[2])[:conditional[1]]
        if len(s) < conditional[1]:
            raise ValueError
    for i in range(len(s)):
        s[i].strip()
        s[i] = conditional[0](s[i])
    return s


def is_valid(n: str, additional_condition=is_str, *value_for_conditional):
    try:
        return additional_condition(n, value_for_conditional)
    except ValueError:
        return False


def input_validation(text="", additional_condition=is_str, *value_for_conditional):
    slesh_n = '\n'
    print(text, end=f'{slesh_n if text != "" else ""}')
    while True:
        try:
            return additional_condition(input().strip(), value_for_conditional)
        except ValueError:
            print('не правильний ввід, спробуйте йще раз')
        except KeyboardInterrupt:
            print('Програма завершила свою роботу')
            exit()


def array_input(text="", size=-1, additional_condition=is_str, split_symbol=' '):
    list_ = input_validation(text, is_valid_array, additional_condition, size, split_symbol)
    if size != -1:
        list_ = list_[:size]
    return list_
