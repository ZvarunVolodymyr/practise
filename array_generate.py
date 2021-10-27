import random

import LinkedList


def generator_generate(size, left, right, func=random.randint):
    for i in range(size):
        yield func(left, right)


class iter_generate_class:
    size = 0
    i = 0
    left = 0
    right = 0
    func = None

    def __init__(self, size, left, right, func=random.randint):
        self.func = func
        self.left = left
        self.right = right
        self.size = size

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.size - 1:
            raise StopIteration
        self.i += 1
        return self.func(self.left, self.right)


def iter_generate(size, left, right, func=random.randint):
    list_ = LinkedList.LinkedList()
    for i in iter_generate_class(size, left, right, func):
        list_.push_back(i)
    list_ = list_
    return list_
