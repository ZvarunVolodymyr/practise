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

    def __init__(self, arr=None, func=lambda x: x):
        if arr is None:
            return
        self.copy_from(arr)

    def __getitem__(self, key):
        return self.get_node(key).val

    def __setitem__(self, key, value):
        this = self.get_node(key)
        this.val = value

    def __iter__(self):
        return ListIter(self.start)

    def __str__(self):
        s = '[' + ', '.join(str(i) for i in self) + ']'
        if self.length == 0:
            s = '[]'
        return s

    def __repr__(self):
        return str(self)

    def __len__(self):
        return self.length

    def copy_from(self, list_=None):
        self.clear()
        if list_ is None:
            return
        for i in list_:
            self.push_back(i)

    def get_node(self, key):
        if not (0 <= key < self.length):
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

    def __add__(self, val):
        for i in val:
            self.push_back(i)

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
        if not (0 <= pos <= self.length):
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
        if not (0 <= pos < self.length):
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

    def input(self, text='', size=0, additional_condition=None, split_symbol=' ', input_size=False):
        if input_size:
            size = validation.is_natural_number(text='Введіть розмір масиву', function='input')
        self.copy_from(validation.is_valid_array(additional_condition, size, split_symbol, text=text, function='input'))

    def use_func(self, func):
        if self.start is None:
            return None
        val = self.start.val
        for i in self:
            val = func(val, i)
        return val

    def get_answer_for_task(self):
        if self.length == 0:
            return 'масив пустий'
        max_ = self.use_func(lambda a, b: max(a, b))
        min_ = self.use_func(lambda a, b: min(a, b))

        coefficient = 0
        if self[0] >= 0:
            coefficient = min_ * min_
        else:
            coefficient = max_ * max_
        ans = LinkedList(self[i] * coefficient for i in range(self.length))
        return ans
