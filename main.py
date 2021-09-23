import validation


class Node:
    def __init__(self, previous=None, next=None, val=None):
        self.previous = previous
        self.next = next
        self.val = val


class ListIter:
    def __init__(self, node: Node):
        self.node = node

    def __next__(self):
        if self.node is None:
            raise StopIteration
        value = self.node.val
        self.node = self.node.next
        return value


class LinkedList:
    start: Node = None
    end: Node = None
    length = 0

    def push_back(self, new_val):
        self.length += 1
        if self.start is None:
            self.start = self.end = Node(val=new_val)
            return
        self.end.next = Node(val=new_val, previous=self.end)
        self.end = self.end.next

    def push_front(self, new_val):
        self.length += 1
        if self.start is None:
            self.start = self.end = Node(val=new_val)
            return
        self.start.previous = Node(val=new_val, next=self.start)
        self.start = self.start.previous

    def __getitem__(self, item):
        if item >= self.length:
            raise IndexError

        for i, val in enumerate(self):
            if i == item:
                return val

    def __setitem__(self, key, value):
        if key >= self.length:
            raise IndexError
        this = self.start
        for i in range(self.length):
            if i == key:
                this.val = value
                return
            this = this.next



    def __str__(self):
        s = '['
        this = self.start
        for val in self:
            s += str(val) + ', '
        s = s[:-2] + ']'
        return s

    def __repr__(self):
        return str(self)

    def __len__(self):
        return self.length

    def __iter__(self):
        return ListIter(self.start)

    def max_element(self):
        if self.start is None:
            return None
        max_ = self.start.val
        for i in self:
            max_ = max(i, max_)
        return max_

    def min_element(self):
        if self.start is None:
            return None
        min_ = self.start.val
        for i in self:
            min_ = min(i, min_)
        return min_


def main_function(n, elements_list: LinkedList):
    max_ = elements_list.max_element()
    min_ = elements_list.min_element()

    coefficient = 0
    if elements_list[0] >= 0:
        coefficient = min_ * min_
    else:
        coefficient = max_ * max_

    for i in range(n):
        elements_list[i] *= coefficient

    return elements_list


def cin():
    list_ = LinkedList()
    n = int(validation.input_validation('Введіть розмір масиву', validation.is_natural_number))
    print(f'Введіть {n} елементів, кожен елемент в новому рядку')
    for i in range(n):
        list_.push_back(float(validation.input_validation(additional_condition=validation.is_float_number)))

    return list_


list_ = cin()
n = len(list_)
print(main_function(n, list_))
