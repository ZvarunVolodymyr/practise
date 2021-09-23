from random import choices


class OperationCounter:
    comparison = 0
    addition = 0

    def plus_comparison(self, a: int):
        self.comparison += a

    def plus_addition(self, a: int):
        self.addition += a


class ArrayWithOperations:
    operation = OperationCounter
    array = []

    def __init__(self, operation_counter, array):
        self.operation = operation_counter
        self.array = array


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


def input_validation(text="", additional_condition=None, *value_for_conditional):
    slesh_n = '\n'
    print(text, end=f'{slesh_n if text != "" else ""}')
    while True:
        try:
            n = input()
            n = n.strip()
            if not is_valid(n, additional_condition, value_for_conditional):
                int('error')
            return n
        except ValueError:
            print('не правильний ввід, спробуйте йще раз')
        except KeyboardInterrupt:
            print('Програма завершила свою роботу')
            exit()


def cin_array(n: int):
    print(f'Введіть масив з {n} чисел(кожне число в новому рялку)')
    list_ = []
    for i in range(n):
        list_.append(float(input_validation('', is_float_number)))
    return list_


def generate_array(sz: int, left: int, right: int):
    list_ = choices(range(left, right), k=sz)
    return list_


def cin():
    n = input_validation('Ведіть(без лапок):\n'
                                        '"1" - ввести масив для сортування\n'
                                        '"2" - згенерувати масив для сортування\n'
                                        '"exit" - вихід з програми',
                         is_menu)
    if n == 'exit':
        print('програма завершила свою роботу')
        exit()
    n = int(n)
    m = int(input_validation('Введіть ціле число - розмір масиву', is_natural_number))
    k = input_validation('Введіть порядок сортування(без лапок): \n"1" - по зростанню\n"2" - по спаданню', is_menu)
    if k == 'exit':
        print('програма завершила свою роботу')
        exit()
    k = int(k)
    if n == 1:
        return [k, cin_array(m)]
    if n == 2:
        left = int(input_validation('Введіть ліву межу генерації(ціле число)', is_int_number))
        right = int(input_validation('Введіть праву межу генерації(ціле число)', is_greater_then, left))
        list_ = generate_array(m, left, right)
        print('Згенерований масив :', list_)
        return [k, list_]


def comparator_erasing(a, b):
    return a > b


def comparator_falling(a, b):
    return a < b


def merge(list_1, list_2, sort_type, operation_counter:OperationCounter):
    new_list = []
    left_pointer = 0
    right_pointer = 0

    comparator = None
    if sort_type == 1:
        comparator = comparator_erasing
    else:
        comparator = comparator_falling

    if not comparator(list_1[len(list_1) - 1], list_2[0]):
        operation_counter.plus_comparison(1) # operation count
        operation_counter.plus_addition(1) # operation count
        return ArrayWithOperations(operation_counter, list_1 + list_2)

    if not comparator(list_2[len(list_2) - 1], list_1[0]):
        operation_counter.plus_comparison(1) # operation count
        operation_counter.plus_addition(1) # operation count
        return ArrayWithOperations(operation_counter, list_2 + list_1)

    while left_pointer < len(list_1) or right_pointer < len(list_2):
        operation_counter.plus_comparison(1 + (left_pointer >= len(list_1))) # operation count
        if left_pointer == len(list_1) or right_pointer != len(list_2) and comparator(list_1[left_pointer],
                                                                                      list_2[right_pointer]):
            new_list.append(list_2[right_pointer])
            operation_counter.plus_comparison(1 + 2 * (left_pointer != len(list_1))) # operation count
            right_pointer += 1
            continue
        operation_counter.plus_comparison(2 + (right_pointer == len(list_2))) # operation count
        new_list.append(list_1[left_pointer])
        left_pointer += 1

    operation_counter.plus_addition(len(new_list)) # operation count
    return ArrayWithOperations(operation_counter, new_list)


def merge_sort(sort_type: int, array: []):
    sz = len(array)
    if sz == 1:
        return ArrayWithOperations(OperationCounter(), array)
    operation_counter = OperationCounter()
    list_1 = merge_sort(sort_type, array[:sz // 2])
    list_2 = merge_sort(sort_type, array[sz // 2:])
    operation_counter.plus_comparison(list_1.operation.comparison + list_2.operation.comparison)
    operation_counter.plus_addition(list_1.operation.addition + list_2.operation.addition)
    return merge(list_1.array, list_2.array, sort_type, operation_counter)


while True:
    input_value = cin()
    sorted_array = merge_sort(input_value[0], input_value[1])
    print(f'\nПосортований масив - {sorted_array.array}\nКількість оперцій додавання - {sorted_array.operation.addition}'
          f'\nКількість оперцій порівняння - {sorted_array.operation.comparison}')
    print('\n\n__________________________________________\n')
