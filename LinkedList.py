from random import choice
import validation

class Node:
    def __init__(self, val=None, previous=None, next=None):
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

    def __init__(self, arr=None, func=None):
        if arr is None:
            return
        for val in arr:
            if func is not None:
                val = func(val)
            self.push_back(val)

    def __getitem__(self, key):
        if key >= self.length or key < 0:
            raise IndexError

        for i, val in enumerate(self):
            if i == key:
                return val

    def __setitem__(self, key, value):
        if key >= self.length or key < 0:
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
        if self.length == 0:
            s = '[]'
        return s

    def __repr__(self):
        return str(self)

    def __len__(self):
        return self.length

    def __iter__(self):
        return ListIter(self.start)

    def copy_from(self, list=None):
        self.clear()
        if list is None:
            return
        for i in list:
            self.push_back(i)

    def get_node(self, key):
        if key < 0 or key >= self.length:
            raise IndexError
        this = self.start
        for i in range(self.length):
            if i == key:
                return this
            this = this.next

    def push_back(self, new_val):
        self.length += 1
        if self.start is None:
            self.start = self.end = Node(val=new_val)
            return
        self.end.next = Node(val=new_val, previous=self.end)
        self.end = self.end.next

    def pop_back(self):
        if self.length == 0:
            return
        self.length -= 1
        self.end = self.end.previous
        if self.length == 0:
            self.start = self.end
            return
        self.end.next = None

    def push_front(self, new_val):
        self.length += 1
        if self.start is None:
            self.start = self.end = Node(val=new_val)
            return
        self.start.previous = Node(val=new_val, next=self.start)
        self.start = self.start.previous

    def pop_front(self):
        if self.length == 0:
            return
        self.length -= 1
        self.start = self.start.next
        if self.length == 0:
            self.end = self.start
            return
        self.start.previous = None

    def insert(self, pos, new_val):
        if pos > self.length or pos < 0:
            raise IndexError
        if pos == self.length:
            self.push_back(new_val)
            return
        if pos == 0:
            self.push_front(new_val)
            return
        this = self.get_node(pos)
        this.previous.next = Node(new_val, this.previous, this)
        this.previous = this.previous.next
        self.length += 1

    def remove(self, pos):
        print(pos, self.length)
        if pos >= self.length or pos < 0:
            raise IndexError
        if pos == self.length - 1:
            self.pop_back()
            return
        if pos == 0:
            self.pop_front()
            return
        this = self.get_node(pos)
        this.previous.next = this.next
        this.next.previous = this.previous
        self.length -= 1

    def clear(self):
        for i in range(self.length):
            self.pop_back()

    def generate(self, size, left, right):
        self.clear()
        for i in range(size):
            self.push_back(choice(range(left, right)))

    def input(self, text='', size=0, type=str, additional_condition=None, split_symbol=' ', input_size=False):
        if input_size:
            size = int(validation.input_validation('Введіть розмір масиву', additional_condition=validation.is_natural_number))
        self.copy_from(validation.array_input(text, size, additional_condition, type, split_symbol))

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

    def get_answer_for_task(self):
        max_ = self.max_element()
        min_ = self.min_element()

        coefficient = 0
        if self[0] >= 0:
            coefficient = min_ * min_
        else:
            coefficient = max_ * max_

        for i in range(self.length):
            self[i] *= coefficient
