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
    return list_


def add_to_list(list_):
    k_pos = validation.input_validation(validation.is_lower_then, [len(list_)], text='Ведіть позицію: ')
    list_.insert(k_pos, validation.input_validation(validation.is_float_number, text='Ведіть значення '))
    return list_


def remove_from_list(list_):
    k_pos = validation.input_validation(validation.is_lower_then, [len(list_) - 1], text='Ведіть позицію: ')
    list_.remove(k_pos)
    return list_


def write_menu(list_):
    list_ = LinkedList()
    m = validation.input_validation(validation.is_natural_number, text='Введіть ціле число - розмір масиву')
    list_.input(f'Введіть {m} елемента, кожен елемент в одному рядку', m, validation.is_float_number)
    return list_


def generate(func):
    def decorator(list_):
        m = validation.input_validation(validation.is_natural_number, text='Введіть ціле число - розмір масиву')
        left = validation.input_validation(validation.is_int_number, text='Введіть ліву межу генерації(ціле число)')
        right = validation.input_validation(validation.is_greater_then, [left],
                                            text='Введіть праву межу генерації(ціле число)')
        return func(m, left, right)
    return decorator


@generate
def generator(m, left, right):
    list_ = LinkedList(array_generate.generator_generate(m, left, right))
    return list_


@generate
def iterator(m, left, right):
    list_ = array_generate.iter_generate(m, left, right)
    return list_