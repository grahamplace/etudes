from linked_list import *

def test_building():
    l = LinkedList()
    assert l.length == 0
    assert l.head == None

    n = Node('test')
    assert n.data == 'test'

    n = Node([1,2])
    assert n.data == [1,2]


def test_append_to_tail():
    l = LinkedList()
    n = Node('this is a test node')
    l.append_to_tail(n)
    assert l.head.data == n.data
    assert l.length == 1

    n2 = Node('this is a second test')
    l.append_to_tail(n2)
    assert l.head.next.data == n2.data
    assert l.length == 2


def test_append_to_head():
    l = LinkedList()
    n = Node('this is a test node')
    l.append_to_head(n)
    assert l.head.data == n.data
    assert l.length == 1

    n2 = Node('this is the new head')
    l.append_to_head(n2)
    assert l.head.data == n2.data
    assert l.head.next.data == n.data
    assert l.length == 2

    n3 = Node('this is the new head')  # don't allow dupes
    l.append_to_head(n3)
    assert l.head.data == n2.data
    assert l.head.next.data == n.data
    assert l.length == 2


def test_found():
    l = LinkedList()
    n = Node('this is a test node')
    l.append_to_head(n)
    assert l.found(n)

    n = Node('this node is not in list')
    assert not l.found(n)


def test_delete():
    l = LinkedList()
    n1 = Node(1)
    l.append_to_tail(n1)
    n2 = Node(2)
    l.append_to_tail(n2)
    n3 = Node(3)
    l.append_to_tail(n3)

    l.delete(n3)
    assert not l.found(n3)
    assert l.length == 2

    l.delete(n1)
    assert not l.found(n1)
    assert l.length == 1
    assert l.head.data == 2

    l.append_to_head(n1)
    l.append_to_tail(n3)
    l.delete(n2)
    assert not l.found(n2)
    assert l.length == 2
    assert l.head.data == 1
    assert l.head.next.data == 3


def test_to_string():
    l = LinkedList()
    n1 = Node('test string node')
    l.append_to_tail(n1)
    n2 = Node(2)
    l.append_to_tail(n2)
    n3 = Node([1,2,3])
    l.append_to_tail(n3)

    assert l.to_string() == '[0] test string node\n[1] 2\n[2] [1, 2, 3]\n'
    # print(l.to_string())


def run_tests():
    test_building()
    test_append_to_tail()
    test_append_to_head()
    test_found()
    test_delete()
    test_to_string()


if __name__ == '__main__':
    run_tests()
