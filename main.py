import validation
from LinkedList import LinkedList


def main_function(n, elements_list: LinkedList):
    max_ = elements_list.max_element()
    min_ = elements_list.min_element()

    coefficient = 0
    if elements_list[0] >= 0:
        coefficient = min_ * min_
    else:
        coefficient = max_ * max_

    for i in range(n):
        elements_list[i] *= coefficient

    return elements_list


def cin():
    n = int(validation.input_validation('Введіть розмір масиву', validation.is_natural_number))
    list_ = LinkedList()
    list_.input(n, f'Введіть {n} елемента, кожен елемент в одному рядку', float, validation.is_float_number)
    return list_


list_ = cin()
list_ = main_function(len(list_), list_)
print(list_)

