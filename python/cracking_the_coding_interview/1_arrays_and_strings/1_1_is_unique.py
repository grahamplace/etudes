# 1.1 Is Unique
# Implement an algorithm to determine if a string has all unique characters.
def is_unique(s):
    seen_chars = []
    for c in list(s):
        if c in seen_chars:
            return False
        else:
            seen_chars.append(c)

    return True


# What if you cannot use additional data structures?
def is_unique2(s):
    for c in list(s):
        old_len = len(s)
        s.replace(c, '')
        # If string is unique, every such replace will remove only one character from s
        if old_len - 1 != len(s):
            return False

    return True


if __name__ == '__main__':
    # Test is_unique, which does use additional data structures
    assert is_unique('abc')
    assert is_unique('')
    assert is_unique('abc 123!')
    assert not is_unique('aaaaaa')
    assert not is_unique('ababaca')
    assert not is_unique(' a ')
    assert not is_unique('!.!?a')

    # Test is_unique2, which uses no additional data structures
    assert is_unique('abc')
    assert is_unique('')
    assert is_unique('abc 123!')
    assert not is_unique('aaaaaa')
    assert not is_unique('ababaca')
    assert not is_unique(' a ')
    assert not is_unique('!.!?a')
