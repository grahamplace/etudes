# 1.8 String Rotation:
# Assume you have a method isSubstring, which checks if one word is a substring of another.
# Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one call to isSubstring
# e.g. "waterbottle" is a rotation of "erbottlewat"

def is_substring(a, b):
    return a in b


def is_rotation(a, b):
    if len(a) != len(b):
        return False

    concat = b + b
    return is_substring(a, concat)


if __name__ == '__main__':
    assert is_rotation('waterbottle', 'erbottlewat')
    assert is_rotation('waterbottle', 'ewaterbottl')
    assert is_rotation('waterbottle', 'lewaterbott')
    assert is_rotation('waterbottle', 'waterbottle')
    assert is_rotation('ababac', 'abacab')

    assert not is_rotation('no', 'ye')
    assert not is_rotation('waterbottle', 'bottleretaw')  # permutation != rotation
    assert not is_rotation('different', 'length')
    assert not is_rotation('ababac', 'abbaca')
    assert not is_rotation('waterbottle', 'bottlewdgdf')
    assert not is_rotation('no', 'nonono')
