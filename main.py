print('Введіть 2 натуральні числа через пробіл')
flag = True
while(flag):
    try:
        n, m = map(int, input().split())
        if n <= 0 or m <= 0:
            int('error')
        flag = False
    except ValueError:
        print('Неправильний ввід, спробуйте йще раз')
        continue

if n > m:
    n, m = m, n

if n == 1:
    print(m * 4)
    exit()

answer = 2 * (n * (m + 1) + m)
additional = 0

if n % 2 != 0:
    additional += m

if m % 2 != 0:
    additional += n

if additional != 0:
    additional -= 2

answer += additional

print(answer)