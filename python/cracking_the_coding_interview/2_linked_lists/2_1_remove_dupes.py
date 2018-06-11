# 2.1 Remove Dupes:
# Write code to remove duplicates from an unsorted linked list.
# Follow Up:
# How would you solve this problem if a temporary buffer is not allowed?

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


    def num_occurrences(self, node):
        if self.length == 0: return 0
        curr = self.head
        count = 0
        while (curr):
            if curr.data == node.data: count += 1
            curr = curr.next

        return count


    def remove_dupes(self):
        if self.length <= 1: return
        seen = set()
        curr = self.head
        seen.add(curr.data)
        while(curr.next):
            if curr.next.data in seen:
                curr.next = curr.next.next  # if we've already seen curr.next.data, remove curr.next from list
            else:
                seen.add(curr.next.data)
                curr = curr.next


    # Follow up: remove dupes with no buffer
    # O(1) space, yay
    # O(n^2) time, boo
    def remove_dupes_no_buffer(self):
        if self.length <= 1: return

        curr = self.head
        while curr:
            curr2 = curr
            while curr2.next:
                if curr2.next.data == curr.data:
                    curr2.next = curr2.next.next
                else:
                    curr2 = curr2.next
            curr = curr.next


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
    my_list.append_to_tail(Node(2))
    my_list.append_to_tail(Node(1))
    my_list.append_to_tail(Node(1))
    my_list.append_to_tail(Node(3))
    my_list.append_to_tail(Node(1))

    assert my_list.num_occurrences(Node(3)) == 1
    assert my_list.num_occurrences(Node(2)) == 2
    assert my_list.num_occurrences(Node(1)) == 4
    assert my_list.num_occurrences(Node(0)) == 0

    my_list.remove_dupes()

    assert my_list.num_occurrences(Node(3)) == 1
    assert my_list.num_occurrences(Node(2)) == 1
    assert my_list.num_occurrences(Node(1)) == 1
    assert my_list.num_occurrences(Node(0)) == 0


    # Do it all again, but with no buffer version
    my_list = LinkedList()

    my_list.append_to_tail(Node(1))
    my_list.append_to_tail(Node(2))
    my_list.append_to_tail(Node(2))
    my_list.append_to_tail(Node(1))
    my_list.append_to_tail(Node(1))
    my_list.append_to_tail(Node(3))
    my_list.append_to_tail(Node(1))

    my_list.remove_dupes_no_buffer()

    assert my_list.num_occurrences(Node(3)) == 1
    assert my_list.num_occurrences(Node(2)) == 1
    assert my_list.num_occurrences(Node(1)) == 1
    assert my_list.num_occurrences(Node(0)) == 0
