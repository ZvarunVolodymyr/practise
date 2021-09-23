
def is_float_number(n:str, value = None):
    try:
        k = float(n)
    except ValueError:
        return False
    return True


def is_int_number(n:str, value = None):
    try:
        k = int(n)
    except ValueError:
        return False
    return True


def is_natural_number(n:str, value = None):
    return is_int_number(n, None) and int(n) > 0


def is_menu(n:str, value = None):
    return n == '1' or n == '2' or n == 'exit'


def is_greater_then(n:str, value:[]):
    if not is_int_number(n):
        return False
    k = float(n)
    for i in value:
        if k <= i:
            return False
    return True


def is_valid(n: str, additional_condition=None, value_for_conditional=None):
    if additional_condition is None:
        return True
    return additional_condition(n, value_for_conditional)


def input_validation(text="", additional_condition=None, *value_for_conditional, is_strip = True):
    slesh_n = '\n'
    print(text, end=f'{slesh_n if text != "" else ""}')
    while True:
        try:
            n = input()
            if is_strip:
                n = n.strip()
            if not is_valid(n, additional_condition, value_for_conditional):
                int('error')
            return n
        except ValueError:
            print('не правильний ввід, спробуйте йще раз')
        except KeyboardInterrupt:
            print('Програма завершила свою роботу')
            exit()