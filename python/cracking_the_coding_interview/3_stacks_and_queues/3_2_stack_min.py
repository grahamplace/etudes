# 3.2 Stack Min:
# How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element?
# Push, pop and min should all operate in 0(1) time.

# Approach:
# Every node also stores the min of its substack (inclusive of itself)
# min() returns the substack_min of the top element
# pop() is unchanged
# push() checks the substack_min of the previous top element to determine what the new top's substack_min should be

class Node():
    def __init__(self, element, prev, substack_min):
        self.element = element
        self.prev = prev
        self.substack_min = substack_min


class Stack():
    def __init__(self):
        self.size = 0
        self.top = None

    def pop(self):
        assert not self.is_empty(), f'Can\'t pop from an empty stack!'
        old_top = self.top
        self.top = old_top.prev
        self.size -= 1
        return old_top.element

    def peek(self):
        assert not self.is_empty(), f'Can\'t peek an empty stack!'
        return self.top.element

    def push(self, item):
        if self.is_empty():
            self.top = Node(item, None, item)
        else:
            old_top = self.top
            self.top = Node(item, old_top, min(item, old_top.substack_min))

        self.size += 1

    def is_empty(self):
        return self.size == 0

    def min(self):
        assert not self.is_empty(), f'An empty stack has no min!'
        return self.top.substack_min


# Quick Tests
s = Stack()
assert s.is_empty()

test_element = 1
s.push(test_element)
assert s.size == 1
assert not s.is_empty()
assert s.peek() == test_element
assert s.min() == test_element
assert s.size == 1

test_min = -1000
s.push(test_min)
assert s.size == 2

assert s.peek() == test_min
assert s.min() == test_min

not_min = 100
s.push(not_min)
assert s.size == 3
assert s.peek() == not_min
assert s.min() == test_min

assert s.pop() == not_min
assert s.min() == test_min
assert s.pop() == test_min
assert s.min() == test_element
