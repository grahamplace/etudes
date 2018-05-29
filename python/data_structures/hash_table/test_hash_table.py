from hash_table import MyHashTable
import random

def test_building():
    h = MyHashTable(5)
    assert h.table_length == 5
    assert len(h.table) == 5
    assert h.table[0] == []


def test_insert_and_get():
    d = {}
    h = MyHashTable(100)
    for i in range(1000):
        d[i] = random.randint(0, 1000)
        h.insert(i, d[i])

    for i in range(1000): assert h.get(i) == d[i]



def test_find():
    h = MyHashTable(5)
    h.insert('test key', 123)
    assert h.find('test key')
    assert not h.find('not a key')


def test_update():
    h = MyHashTable(5)

    h.insert('test key', 123)
    assert h.get('test key') == 123

    h.update('test key', 321)
    assert h.get('test key') == 321


def test_remove():
    h = MyHashTable(5)

    h.insert('test key', 123)
    assert h.find('test key')

    h.remove('test key')
    assert not h.find('test key')


def test_visual():
    h = MyHashTable(5)
    print(f"Making a new hash table of length: {h.table_length}...")
    print("Current state of hash table:")
    print(h.to_string())
    print("Inserting ('abc', 123)...")
    h.insert('abc', 123)
    print("Inserting ('123', 0)...")
    h.insert('123', 0)
    print("Inserting ('testing', 42)...")
    h.insert('testing', 42)
    print("Inserting ('yet another key', 999)...")
    h.insert('yet another key', 999)
    print("Inserting ('foo', 123)...")
    h.insert('foo', 123)
    print("Inserting ('bar', 123)...")
    h.insert('bar', 123)
    print("Inserting ('baz', 123)...")
    h.insert('baz', 123)
    print("Current state of hash table:")
    print(h.to_string())


def run_tests():
    test_building()
    test_insert_and_get()
    test_find()
    test_update()
    test_remove()
    test_visual()


if __name__ == '__main__':
    run_tests()
