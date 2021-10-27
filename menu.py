import menu_functions
import validation
from LinkedList import LinkedList
from menu_functions import exit_, back_, get_answer, write, update, remove_from_list, remove_in_range, print_list, \
                            iterator, generator


def menu(list_, observer, text, pages):
    while True:
        n = validation.is_menu(pages.keys(), text=text, function='input')
        is_break = pages[n](list_, observer)
        if is_break is None:
            return True
        if not is_break:
            return False
        return


def main_menu(list_, observer):
    pages = {'generate': generate_menu, 'exit': exit_, 'task': get_answer, 'write': write,
             'update': update, 'remove': remove_from_list, 'remove_in_range': remove_in_range,
             'print': print_list}
    text = '\nВедіть:\n' \
           'generate - обрати метод "генерація" \n' \
           'write - обрати метод "ввід"\n' \
           'update - виконати обраний метод\n' \
           'remove - видалити 1 змінну\n' \
           'remove_in_range - видалити декілька змінних [start, end)\n' \
           'task - дати відповідь на завдання\n' \
           'print - вивести масив\n' \
           'exit - вихід з програми'
    return menu(list_, observer, text, pages)


def generate_menu(list_):
    pages = {'iterator': iterator, 'generator': generator, 'back': back_, 'exit': exit_}
    text = '\nВедіть:\n' \
           'iterator - обрати генерацію ітератором\n' \
           'generator - обрати генерацію генератором\n' \
           'back - до попередньго меню\n' \
           'exit - вихід з програми'
    return menu(list_, text, pages)