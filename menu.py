import menu_functions
import validation
from LinkedList import LinkedList
from menu_functions import exit_, back_, write_menu, generator, iterator, add_to_list, remove_from_list


def menu(list_, text, pages):
    while True:
        n = validation.input_validation(validation.is_menu, pages.keys(), text=text)
        list__ = pages[n](list_)
        if list__ is None:
            return [None, list_]
        if len(list__) == 0 or not list__[0] is None:
            return list__
        list_ = list__[1]


def main_menu(list_):
    pages = {'new': new_menu, 'edit':change_menu, 'exit': exit_}
    text = 'Ведіть:\n' \
           'new - новий масив\n' \
           'edit - змінити масив\n' \
           'exit - вихід з програми'
    list_ = menu(list_, text, pages)
    return menu_functions.get_answer(list_)


def change_menu(list_):
    pages = {'add': add_to_list, 'remove': remove_from_list, 'back': back_, 'exit': exit_}
    text = 'Ведіть:\n' \
           'add - додати елемент\n' \
           'remove - згенерувати масив\n' \
           'back - до попередньго меню\n' \
           'exit - вихід з програми'
    return menu(list_, text, pages)


def new_menu(list_):
    pages = {'write': write_menu, 'generate': generate_menu, 'back': back_, 'exit': exit_}
    text = 'Ведіть:\n' \
           'write - ввести масив\n' \
           'generate - згенерувати масив\n' \
           'back - до попередньго меню\n' \
           'exit - вихід з програми'
    return menu(list_, text, pages)


def generate_menu(list_):
    pages = {'iterator': iterator, 'generator': generator, 'back': back_, 'exit': exit_}
    text = 'Ведіть:\n' \
           'iterator - ввести масив\n' \
           'generator - згенерувати масив\n' \
           'back - до попередньго меню\n' \
           'exit - вихід з програми'
    return menu(list_, text, pages)