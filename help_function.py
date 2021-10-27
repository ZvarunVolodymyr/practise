def insert_logging(return_data, pos, new_val, file_='output.txt'):
    file = open(file_, 'a')
    text = f'Додані данні:\n' \
           f'позиція додавання = {pos}\n' \
           f'масив, що додано = {new_val}\n' \
           f'кінцевий масив = {return_data}\n' \
           f'---------------------------------------\n'
    file.write(text)
    file.close()


def remove_logging(return_data, pos1, pos2, file_='output.txt'):
    file = open(file_, 'a')
    text = f'Видалені данні:\n' \
           f'початкова позиція = {pos1}\n' \
           f'кінцева позиція = {pos2}\n' \
           f'кінцевий масив = {return_data}\n'\
           f'---------------------------------------\n'
    file.write(text)
    file.close()