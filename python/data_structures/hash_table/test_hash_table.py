from hash_table import MyHashTable

def test_building():
    h = MyHashTable(5)
    assert type(h) == MyHashTable
    assert h.table_length == 5


def test_insert_and_get():
    h = MyHashTable(5)
    h.insert('abc', 123)
    assert h.get('abc') == 123


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


def test_to_string():
    h = MyHashTable(5)
    h.insert('abc', 123)
    h.insert('123', 0)
    h.insert('testing', 42)
    assert h.to_string() == "[('testing', 42)]\n[]\n[('abc', 123), ('123', 0)]\n[]\n[]\n"


def run_tests():
    test_building()
    test_insert_and_get()


if __name__ == '__main__':
    run_tests()
