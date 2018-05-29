# A super simple implementation of a hash table in python
# Uses list-of-lists approach w/ closed addressing

class MyHashTable(object):

    def __init__(self, table_length: int):
        self.table_length = table_length
        self.table = [[] for i in range(table_length)]


    # for given key, create a hash code using python's built-in hash()
    # note: this hash code is independent of length of table
    def get_hash_code(self, key) -> int:
        return hash(str(key))


    # for given hash code, return the corresponding index of the "table" list
    def h(self, hash_code) -> int:
        return hash_code % self.table_length


    # lookup and return the value using the given key
    def get(self, key):
        hash_code = self.get_hash_code(key)
        index = self.h(hash_code)
        for t in self.table[index]:
            if t[0] == key:
                return t[1]

        return None


    # check to see if a given key exists in hash table
    def find(self, key):
        hash_code = self.get_hash_code(key)
        index = self.h(hash_code)
        for t in self.table[index]:
            if t[0] == key:
                return True

        return False


    # insert a new (key, value) pair into the hash table
    def insert(self, key, value):
        hash_code = self.get_hash_code(key)
        index = self.h(hash_code)

        # if key already exists in table, error
        for t in self.table[index]:
            assert t[0] != key, "Key already present in hash table; try update(key, value) instead."

        self.table[index].append((key, value))


    # change the value in table of key to given new_
    def update(self, key, new_value):
        hash_code = self.get_hash_code(key)
        index = self.h(hash_code)

        for t in self.table[index]:
            if t[0] == key:
                t[1] = value
                return

        assert False, "Key not present in hash table; try insert(key, value) instead."


    # remove element with given key from the hash table
    def remove(self, key):
        hash_code = self.get_hash_code(key)
        index = self.h(hash_code)
        for t in self.table[index]:
            if t[0] == key:
                self.table[index].remove(t)

        assert False, "Key not present in hash table; could not delete"


    # convert hash table to string and return
    def to_string(self):
        ht = ''
        for row in self.table:
            ht += (str(row) + "\n")

        return ht
