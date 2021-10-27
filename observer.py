import copy

import inspect

class event:
    event_name = ''
    event_info_format = None

    def __init__(self, name = '', decorate = None):
        self.event_name = name
        self.event_info_format = decorate


class eventManager:
    funct = {}

    def add_func(self, name, event_name, event_decorate):
        print(event_decorate)
        event_ = event(event_name, event_decorate)
        if self.funct.get(name, None) is None:
            self.funct[name] = []

        if self.funct[name].count(event_) == 0:
            self.funct[name].append(event_)
            return True
        return False

    def remove_func(self, name, event_name, event_decorate):
        event_ = event(event_name, event_decorate)
        if self.funct[name].count(event_) != 0:
            self.funct[name].remove(event_)
            return True
        return False

    def get_event_decorate(self, name, event_name):
        for i in self.funct[name]:
            if i.event_name == event_name:
                return i.event_info_format


class observer:
    event_name = ''
    observer_function = None

    def __init__(self, name='', observer_function=None):
        self.event_name = name
        self.observer_function = observer_function


class observerManager:
    members = {}
    event_manager = eventManager()

    def __init__(self, new_event_manager):
        self.event_manager = new_event_manager

    def add_member(self, name, event_name, func):
        obj = observer(event_name, func)
        if self.members.get(name, None) is None:
            self.members[name] = []
        if self.members[name].count(obj) == 0:
            self.members[name].append(obj)
            return True
        return False

    def remove_member(self, name, obj):
        if self.members[name].count(obj) != 0:
            self.members[name].remove(obj)
            return True
        return False

    def update(self, name, values):
        for i in self.members[name]:
            input_ = self.event_manager.get_event_decorate(name, i.event_name)(values)
            i.observer_function(*input_)


def is_event(func):
    def decorator(*vars, **kwargs):
        observer = kwargs.pop('event_observer', None)
        name = kwargs.pop('func_name', None)
        name = func.__name__ if name is None else name
        return_ = func(*vars, **kwargs)
        if observer is None:
            return return_
        values = {}
        keys = inspect.getfullargspec(func).args
        i = 0
        for j in range(min(len(vars) + len(kwargs), len(keys))):
            if keys[j] in kwargs.keys():
                values[keys[j]] = kwargs.pop(keys[j])
            else:
                values[keys[j]] = vars[i]
                i += 1
        if inspect.getfullargspec(func).varargs != '':
            values[inspect.getfullargspec(func).varargs] = vars[i:]

        if inspect.getfullargspec(func).varkw != '':
            values[inspect.getfullargspec(func).varkw] = kwargs
        values['return_data'] = return_
        observer.update(name, values)
        return return_

    return decorator