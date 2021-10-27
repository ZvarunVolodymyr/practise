import copy

import event_info_format
import help_function
from observer import observerManager, eventManager

import menu
import LinkedList

list_ = LinkedList.LinkedList()
# list_.remove(1, 3)
# print(list_)

events = eventManager()
events.add_func('insert', 'insert_log', event_info_format.add_log_info)
events.add_func('remove', 'remove_log', event_info_format.remove_log_info)
observer = observerManager(events)
observer.add_member('insert', 'insert_log', help_function.insert_logging)
observer.add_member('remove', 'remove_log', help_function.remove_logging)

file = open('output.txt', 'w')
file.write('')
file.close()

while True:
    menu.main_menu(list_, observer)

