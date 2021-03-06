import functools

import strategy
import validation
from LinkedList import LinkedList
import array_generate


def exit_(value):
    print('програма завершила свою роботу')
    exit()


def back_(value):
    return None


def get_answer(list_):

    s_1 = 'Відповідь для масиву ' + str(list_) + ':'
    s_2 = str(list_.get_answer_for_task())
    mx = max(len(s_1), len(s_2))
    print('*' * mx)
    print(s_1 + '\n' + s_2)
    print('*' * mx)


def write(list_):
    list_.set_strategy(strategy.from_file)


def remove_from_list(list_):
    k_pos = validation.is_int_in_range(0, len(list_) - 1, text='Ведіть позицію: ', function='input')
    list_.remove(k_pos)


def remove_in_range(list_):
    a = validation.is_int_in_range(0, len(list_) - 1, text='Введіть ліву межу до видялення', function='input')
    b = validation.is_int_in_range(a + 1, len(list_), text='Введіть праву межу до видялення', function='input')
    list_.remove(a, b)


def update(list_):
    list_.execute_strategy()


def generator(list_):
    list_.set_strategy(strategy.generate_generator)


def iterator(list_):
    list_.set_strategy(strategy.generate_iterator)


def print_list(list_):
    print(list_)
