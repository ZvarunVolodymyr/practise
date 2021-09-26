import validation
from LinkedList import LinkedList


def cin():
    n = int(validation.input_validation('Введіть розмір масиву', validation.is_natural_number))
    list_ = LinkedList()
    list_.input(f'Введіть {n} елемента, кожен елемент в одному рядку', n, float, validation.is_float_number)
    return list_


list_ = cin()

# також можна записати так
# list_ = LinkedList()
# list_.input('Введіть масив', type=float, additional_condition=validation.is_float_number, input_size=True)
list_.get_answer_for_task()
print(list_)

