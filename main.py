import validation
from LinkedList import LinkedList


def cin():
    n = validation.input_validation('Ведіть(без лапок):\n'
                                    '"1" - ввести масив\n'
                                    '"2" - згенерувати масив\n'
                                    '"exit" - вихід з програми',
                                    validation.is_menu)
    if n == 'exit':
        print('програма завершила свою роботу')
        exit()
    m = validation.input_validation('Введіть ціле число - розмір масиву', validation.is_natural_number)
    if n == '1':
        list_ = LinkedList()
        list_.input(f'Введіть {m} елемента, кожен елемент в одному рядку', m, validation.is_float_number)
        # також можна записати так
        # list_ = LinkedList()
        # list_.input('Введіть масив', type=float, additional_condition=validation.is_float_number, input_size=True)
        return list_
    if n == '2':
        left = validation.input_validation('Введіть ліву межу генерації(ціле число)', validation.is_int_number)
        right = validation.input_validation('Введіть праву межу генерації(ціле число)', validation.is_greater_then, left)
        list_ = LinkedList()
        list_.generate(m, left, right)
        print('Згенерований масив :', list_)
        return list_


while True:
    list_ = cin()
    list_.get_answer_for_task()
    print(list_)

