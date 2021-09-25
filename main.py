import validation
from LinkedList import LinkedList


def cin():
    n = int(validation.input_validation('Введіть розмір масиву', validation.is_natural_number))
    list_ = LinkedList()
    list_.input(n, f'Введіть {n} елемента, кожен елемент в одному рядку', float, validation.is_float_number)
    return list_


list_ = cin()
list_.get_answer_for_task()
print(list_)

