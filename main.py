def main_function(n: int, m: int):
    if n > m:
        n, m = m, n

    if n == 1:
        return m * 4

    answer = 2 * (n * (m + 1) + m)

    return answer


def input_int_number(name=''):
    print(f"Введіть натуральне число {name}(без зайвих символів)")
    while True:
        try:
            new_nam = int(input())
            if new_nam <= 0:
                int('error')
            return new_nam
        except ValueError:
            print('Неправильний ввід, спробуйте йще раз')
            continue


def cin():
    return [input_int_number('n'), input_int_number('m')]


input_value = cin()
print(main_function(input_value[0], input_value[1]))
