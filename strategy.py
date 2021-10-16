import array_generate
import validation
import menu_functions
from LinkedList import LinkedList


class strategy:
    list_ = None

    def __init__(self, obj):
        self.list_ = obj

    def func(self):
        pass


def generate_input(size):
    n = validation.is_natural_number(function='input', text='Введіть кількість елементів')
    a = validation.is_int_number(function='input', text='Введіть ліву межу генерації')
    b = validation.is_int_greater(a, function='input', text='Введіть праву межу генерації')
    k = validation.is_int_in_range(0, size, text='Ведіть позицію для вставки', function='input')
    n += 1
    return n, a, b, k


class generate_iterator(strategy):
    def func(self):
        n, a, b, k = generate_input(len(self.list_))
        self.list_.insert(k, *array_generate.iter_generate(n, a, b))
        return self.list_


class generate_generator(strategy):
    def func(self):
        n, a, b, k = generate_input(len(self.list_))
        self.list_.insert(k, *array_generate.generator_generate(n, a, b))
        return self.list_


class from_file(strategy):
    def func(self):
        file_name = validation.is_file(function='input', text='Введіть назву файла')
        file = open(file_name)
        new_list = validation.is_valid_array(file.readline(), validation.is_float_number, function='print',
                                             file=file_name)
        if new_list is None:
            return self.list_
        k = validation.is_int_in_range(0, len(self.list_), text='Ведіть позицію для вставки', function='input')
        self.list_.insert(k, *new_list)
