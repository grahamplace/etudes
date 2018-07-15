# 2.2 Return Kth to Last:
# Implement an algorithm to  nd the kth to last element of a singly linked list.

class LinkedList(object):

    def __init__(self):
        self.length = 0
        self.head = None


    def append_to_tail(self, node):
        if self.length == 0:
            self.head = node
        else:
            curr = self.head
            while(curr.next):
                curr = curr.next
            curr.next = node

        self.length += 1


    def kth_to_last(self, k):
        # length is already known
        stop_at_index = self.length - k - 1
        curr = self.head
        for i in range(stop_at_index):
            curr = curr.next

        return curr.data


    def to_string(self):
        list_str = ""
        curr = self.head
        i = 0
        while(curr):
            list_str += f'[{i}] {curr.data}' + '\n'
            curr = curr.next
            i += 1

        return list_str


class Node(object):

    def __init__(self, data = None):
        self.data = data
        self.next = None


if __name__ == '__main__':
    my_list = LinkedList()

    my_list.append_to_tail(Node(1))
    my_list.append_to_tail(Node(2))
    my_list.append_to_tail(Node(3))

    assert my_list.kth_to_last(0) == 3
    assert my_list.kth_to_last(1) == 2
    assert my_list.kth_to_last(2) == 1
