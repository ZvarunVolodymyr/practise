from LinkedList import LinkedList
import os


def is_str(n):
    return n


def is_float_number(n):
    n = n.strip()
    try:
        return float(n)
    except ValueError:
        raise ValueError(n + ' не є дійсним числом')


def is_int_number(n):
    if type(n) == str:
        n = n.strip()
    try:
        return int(n)
    except ValueError:
        raise ValueError(n + ' не є цілим числом')


def is_natural_number(n):
    n = n.strip()
    if not (is_int_number(n) and int(n) > 0):
        raise ValueError(n + ' не є натуральним цілим числом')
    return int(n)


def is_menu(n, list_):
    n = n.strip()
    if not n in list_:
        raise ValueError(n + ' не є полем меню')
    return n


def is_greater_then(n, list_):
    k = is_int_number(n)
    for i in list_:
        if k <= i:
            raise ValueError(str(k) + ' не є більшим за ' + str(i))
    return k


def is_lower_then(n, list_):
    k = is_int_number(n)
    for i in list_:
        if k > i:
            raise ValueError(str(k) + ' не є меншим за ' + str(i))
    return k

def is_in_list(n, list_):
    n = is_natural_number(n)
    if not n in list_:
        raise ValueError(str(n) + ' немає в потрібному масиві')
    return n


def is_valid_array(list_, func, size, split_):
    s = LinkedList(map(func, filter(lambda x: x != '', list_.split(split_))))
    if size != -1:
        if len(s) != size:
            print(len(s))
            raise ValueError
    return s


def is_file(n):
    n = n.strip()
    if not os.path.isfile(n):
        raise ValueError(str(n) + ': файлу не існує, або програма його не бачить')
    return n


def is_valid(additional_condition=is_str, *value_for_conditional):
    try:
        return additional_condition(*value_for_conditional)
    except ValueError as error:
        raise ValueError(error)


def input_validation(additional_condition=is_str, *value_for_conditional, text=""):
    slesh_n = '\n'
    print(text, end=f'{slesh_n if text != "" else ""}')
    while True:
        try:
            a = [input()]
            a += value_for_conditional
            return additional_condition(*a)
        except ValueError as error:
            print(error)
            print('спробуйте йще раз')
        except KeyboardInterrupt:
            print('Програма завершила свою роботу')
            exit()


def was_error(message='ПОМИЛКА', file=''):
    message = str(message)
    message = '\n' + '*' * len(message) + '\n' + message + '\n' + '*' * len(message)
    print(message)
    if file != '':
        file = open(file, 'a')
        file.write('\n' + message + '\n')
        file.close()


def array_input(text="", size=-1, additional_condition=is_str, split_symbol=' '):
    list_ = input_validation(is_valid_array, additional_condition, size, split_symbol, text=text)
    return list_
