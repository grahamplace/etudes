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
                if curr.data == node.data: return  # don't allow dupes
                curr = curr.next
            curr.next = node

        self.length += 1


    def append_to_head(self, node):
        if self.found(node): return  # don't allow dupes
        node.next = self.head
        self.head = node
        self.length += 1


    def delete(self, node):
        if self.head.data == node.data:
            self.head = self.head.next
            self.length -= 1

        trailer = self.head
        runner = trailer.next
        while(runner):
            if runner.data == node.data:
                trailer.next = runner.next  # goodbye runner
                self.length -= 1
                return
            runner = runner.next
            trailer = trailer.next


    def found(self, node):
        if self.length == 0: return False
        curr = self.head
        while (curr):
            if curr.data == node.data: return True
            curr = curr.next

        return False


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
