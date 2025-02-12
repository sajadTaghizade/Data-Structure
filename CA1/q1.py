import sys
import re


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def empty(self):
        if len(self.queue) == 0:
            return True
        return False
            
    def one_line_str(self):
        return " ".join(map(str, self.queue))


class Stack:
    def __init__(self, capacity=10):
        self.satck = []
        self.capa = capacity
    def push(self, value):
        self.satck.append(value)

    def pop(self):
        return self.satck.pop()

    def put(self, value):
        self.satck.pop()
        self.satck.append(value)
    def peek(self):
        return self.satck[-1]

    def expand(self):
        self.capa = self.capa * 2

    def capacity(self):
        return self.capa

    def size(self):
        return len(self.satck)

    def empty(self):
        if len(self.satck) == 0:
            return True
        return False

    def one_line_str(self):
        return " ".join(map(str, self.satck))


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, value):
        current_node = Node(value)
        current_node.next = self.head
        self.head = current_node

    def insert_back(self, value):
        current_node = Node(value)
        if self.head is None:
            self.head = current_node
        else:
            start = self.head
            while start.next:
                start = start.next
            start.next = current_node

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def one_line_str(self):
        return ' '.join(str(value) for value in self)



class Runner:
    ds_map = {'stack': Stack, 'queue': Queue, 'linked_list': LinkedList}
    call_regex = re.compile(r'^(\w+)\.(\w+)\(([\w, ]*)\)$')

    def __init__(self, input_src):
        self.input = input_src
        self.items = {}

    def run(self):
        for line in self.input:
            line = line.strip()
            action, _, param = line.partition(' ')
            action_method = getattr(self, action, None)
            if action_method is None:
                return
            action_method(param)

    def make(self, params):
        item_type, item_name = params.split()
        self.items[item_name] = self.ds_map[item_type]()

    def call(self, params):
        regex_res = self.call_regex.match(params)
        item_name, func_name, args_list = regex_res.groups()
        args = args_list.split(',') if args_list != '' else []

        method = getattr(self.items[item_name], func_name)
        result = method(*args)
        if result is not None:
            print(result)


def main():
    runner = Runner(sys.stdin)
    runner.run()


if __name__ == "__main__":
    main()
