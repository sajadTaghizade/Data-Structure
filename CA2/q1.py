import sys
import re

INVALID_INDEX = 'invalid index'
OUT_OF_RANGE_INDEX = 'out of range index'
EMPTY = 'empty'

class MinHeap:
    class Node:
        def __init__(self, value):
            self.val = value

    def __init__(self):
        self.tree = []
    def bubble_up(self, index):
        if not isinstance(index, (int, float)):
            raise Exception(INVALID_INDEX)
        if index < 0 or index >= len(self.tree):
            raise Exception(OUT_OF_RANGE_INDEX)
        while index > 0:
            p_index = (index - 1) // 2
            if self.tree[index].val >= self.tree[p_index].val:
                break
            self.tree[index], self.tree[p_index] = self.tree[p_index], self.tree[index]
            index = p_index

    def bubble_down(self, index):
        if not isinstance(index, (int, float)):
            raise Exception(INVALID_INDEX)
        if index < 0 or index >= len(self.tree):
            raise Exception(OUT_OF_RANGE_INDEX)
        while index < len(self.tree):
            min_index = self.find_min_child(index)
            if min_index == -1:
                break
            if self.tree[index].val <= self.tree[min_index].val:
                break
            self.tree[index], self.tree[min_index] = self.tree[min_index], self.tree[index]
            index = min_index

    def heap_push(self, val):
        if not isinstance(val, (int, float)):
            raise Exception(INVALID_INDEX)
        self.tree.append(self.Node(val))
        self.bubble_up(len(self.tree) - 1)
 
    def heap_pop(self):
        if not self.tree:
            raise Exception(EMPTY)
        root_val = self.tree[0].val
        if len(self.tree) > 1:
            self.tree[0] = self.tree.pop()
            self.bubble_down(0)
        else:
            self.tree.pop()
        return root_val

    def find_min_child(self, index):
        if not isinstance(index, int):
            raise Exception(INVALID_INDEX)
        if index < 0 or index >= len(self.tree):
            raise Exception(OUT_OF_RANGE_INDEX)
        
        left = 2 * index + 1
        right = 2 * index + 2

        if left >= len(self.tree):
            return -1
        if right >= len(self.tree):
            return left

        if self.tree[left].val < self.tree[right].val:
            return left
        else:
            return right

    def heapify(self, *args):
        self.tree = []
        for v in args:
            self.tree.append(self.Node(v))
        n = len(self.tree)
        i = n // 2 - 1
        while i >= 0:
            self.bubble_down(i)
            i -= 1

class HuffmanTree:
    class Node:
        def __init__(self, frequency, char=None, left=None, right=None):
            self.frequency = frequency
            self.char = char
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None
        self.text = None

    def set_letters(self, *args):
        self.letters = args

    def set_repetitions(self, *args):
        self.frequencies = args

    def set_text(self, text):
        self.text = text

    def build_tree(self):
        if self.text:
            frequencies = {}
            for char in self.text:
                if char in frequencies:
                    frequencies[char] += 1
                else:
                    frequencies[char] = 1
            nodes = []
            for char, fr in frequencies.items():
                nodes.append(self.Node(fr, char))
        elif hasattr(self, 'letters') and hasattr(self, 'frequencies'):
            nodes = []
            for char, fr in zip(self.letters, self.frequencies):
                nodes.append(self.Node(fr, char))
        else:
            raise Exception(EMPTY)

        while len(nodes) > 1:
            for i in range(len(nodes) - 1):
                for j in range(len(nodes) - i - 1):
                    if nodes[j].frequency > nodes[j + 1].frequency:
                        nodes[j], nodes[j + 1] = nodes[j + 1], nodes[j]

            left = nodes.pop(0)
            right = nodes.pop(0)
            merging = self.Node(left.frequency + right.frequency, left=left, right=right)
            nodes.append(merging)

        self.root = nodes[0]

    def get_compressed_length(self):
        if not self.root:
            raise Exception(EMPTY)

        def traversing(node, code=""):
            if not node.left and not node.right:
                self.codes[node.char] = code
            else:
                if node.left:
                    traversing(node.left, code + "0")
                if node.right:
                    traversing(node.right, code + "1")

        self.codes = {}
        traversing(self.root)

        compressed_length = 0
        if self.text:
            for char in self.text:
                compressed_length += len(self.codes[char])
        else:
            for char, fr in zip(self.letters, self.frequencies):
                compressed_length += len(self.codes[char]) * fr

        return compressed_length

class Bst:
    class Node:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = self.Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return self.Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    def preorder(self):
        ans = []
        self.traversing(self.root, ans, 'pre')
        return ' '.join(map(str, ans))

    def inorder(self):
        ans = []
        self.traversing(self.root, ans, 'in')
        return ' '.join(map(str, ans))

    def postorder(self):
        ans = []
        self.traversing(self.root, ans, 'post')
        return ' '.join(map(str, ans))

    def traversing(self, node, ans, order):
        if node:
            if order == 'pre':
                ans.append(node.key)
            self.traversing(node.left, ans, order)
            if order == 'in':
                ans.append(node.key)
            self.traversing(node.right, ans, order)
            if order == 'post':
                ans.append(node.key)

class Runner:
    ds_map = {'min_heap': MinHeap, 'bst': Bst, 'huffman_tree': HuffmanTree}
    call_regex = re.compile(r'^(\w+)\.(\w+)\(([\w, \-"\']*)\)$')

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

        args = [x.strip() for x in args_list.split(',')] if args_list != '' else []
        args = [x[1:-1] if x[0] in ('"', "'") else int(x) for x in args]

        method = getattr(self.items[item_name], func_name)
        try:
            result = method(*args)
        except Exception as ex:
            print(ex)
        else:
            if result is not None:
                print(result)

def main():
    runner = Runner(sys.stdin)
    runner.run()

if __name__ == "__main__":
    main()