from random import choices


def int_input(text="", is_request=False, is_natural=False):
    slesh_n = '\n'
    print(text, end=f'{slesh_n if text != "" else ""}')
    while True:
        try:
            n = input()
            if is_request:
                if n != '1' and n != '2' and n != 'exit':
                    n = int('error')
                return n
            n = int(n)
            if is_natural:
                if n > 0:
                    return n
                n = int('error')
            return int(n)
        except ValueError:
            print('не правильний ввід, спробуйте йще раз')
        except KeyboardInterrupt:
            print('Програма завершила свою роботу')
            exit()


def cin_array(n: int):
    print(f'Введіть масив з {n} чисел(розділених пробілами)')
    while True:
        try:
            list_ = list(map(float, input().split()[:n]))
            if len(list_) < n:
                int('error')
            return list_
        except ValueError:
            print('Не правильний ввід, спробуйте йще раз')
        except KeyboardInterrupt:
            print('Програма завершила свою роботу')
            exit()


def generate_array(n: int):
    a = int_input('Введіть ліву межу генерації')
    b = int_input('Введіть праву межу генерації')
    list_ = choices(range(a, b), k=n)
    print('Згенерований масив: ', end='')
    print(list_)
    return list_


def cin():
    n = int_input(is_request=True, text='Ведіть(без лапок):\n"1" - ввести масив для сортування\n"2" - згенерувати масив для сортування\n'
          '"exit" - вихід з програми')
    if n == 'exit':
        print('програма завершила свою роботу')
        exit()
    n = int(n)
    m = int_input('Введіть ціле число - розмір масиву', is_natural=True)
    k = int_input('Введіть порядок сортування(без лапок): \n"1" - по зростанню\n"2" - по спаданню', is_request=True)
    if k == 'exit':
        print('програма завершила свою роботу')
        exit()
    k = int(k)
    if n == 1:
        return [k, cin_array(m)]
    if n == 2:
        return [k, generate_array(m)]


def comp_1(a, b):
    return a > b


def comp_2(a, b):
    return a < b


def merge(list_1, list_2, sort_type, ans):
    new_list = []
    left_pointer = 0
    right_pointer = 0
    comp = None
    if sort_type == 1:
        comp = comp_1
    else:
        comp = comp_2
    while left_pointer < len(list_1) or right_pointer < len(list_2):
        if left_pointer == len(list_1) or right_pointer != len(list_2) and comp(list_1[left_pointer], list_2[right_pointer]):
            new_list.append(list_2[right_pointer])
            right_pointer += 1
            continue
        new_list.append(list_1[left_pointer])
        left_pointer += 1

    return [ans + len(new_list), new_list]


def merge_sort(sort_type:int, array: []):
    sz = len(array)
    if sz == 1:
        return [0, array]
    ans = 0
    list_1 = merge_sort(sort_type, array[:sz // 2])
    list_2 = merge_sort(sort_type, array[sz//2:])
    ans += list_1[0] + list_2[0]
    return merge(list_1[1], list_2[1], sort_type, ans)


while True:
    input_value = cin()
    sorted_array = merge_sort(input_value[0], input_value[1])
    print(f'\nПосортований масив - {sorted_array[1]}\nКількість оперцій - {sorted_array[0]}')
    print('\n\n__________________________________________\n')