# 3.1 Three in One:
# Describe how you could use a single array to implement three stacks

# I'll only implement Approach 1 here (fixed stack size)
# The other option is to allow flexible stack size
# This requires shifting stacks (chunks of the array) when an earlier stack "hits" the start of a later one
# Additionally, we would want to implement a circular buffer to allow the last stack to wrap around and use the start of the array if needed

class MultiStack():
    def __init__(self, size, names):
        self.array = [None] * (size * len(names))
        self.names = names
        self.start_map = {name: (len(self.array) * i) // len(names) for i, name in enumerate(names)}
        self.stop_map = {name: ((len(self.array) * (i + 1)) // len(names)) - 1 for i, name in enumerate(names)}
        self.size_map = {name: 0 for i, name in enumerate(names)}

    def pop(self, name):
        self._validate(name)
        assert not self.is_empty(name), f'{name} is empty! Can\'t pop from empty stack.'
        curr = self._get_current_index(name)
        element = self.array[curr]
        self.array[curr] = None
        self.size_map[name] -= 1
        return element

    def push(self, item, name):
        self._validate(name)
        curr = self._get_current_index(name)
        assert curr + 1 <= self.stop_map[name], f'Pushing another element to {name} would exceed available space allocated for {name}'
        self.array[curr + 1] = item
        self.size_map[name] += 1
        return True

    def peek(self, name):
        self._validate(name)
        index = self._get_current_index(name)
        return self.array[index]

    def is_empty(self, name):
        self._validate(name)
        return self.size_map[name] == 0

    def _validate(self, name):
        error_str = f'{name} is not a valid stack in this MultiStack! Valid stack names: {self.names}'
        assert name in self.names, error_str

    def _get_current_index(self, name):
        start = self.start_map[name]
        size = self.size_map[name]
        index = start + size
        return index


# Quick Tests
s = MultiStack(10, ['a', 'b'])

assert s.is_empty('a')
assert s.is_empty('b')

test_element = 1
s.push(test_element, 'b')
assert s.is_empty('a')
assert not s.is_empty('b')

assert s.peek('b') == test_element
assert not s.is_empty('b')
assert s.pop('b') == test_element
assert s.is_empty('b')
