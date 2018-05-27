# 1.2 Check Permutation:
# Given two strings, write a method to decide if one is a permutation of the other.

def check_permutation(a, b):
    first = list(a)
    first.sort()
    second = list(b)
    second.sort()
    return first == second


if __name__ == '__main__':
    assert check_permutation('abc', 'acb')
    assert check_permutation('a', 'a')
    assert check_permutation('321', '123')
    assert check_permutation('aaa', 'aaa')
    assert check_permutation('hello', 'lehlo')
    assert check_permutation('1.ao!', 'o.a!1')
    assert check_permutation('same', 'same')

    assert not check_permutation('a', 'differnt length strings')
    assert not check_permutation('a', 'b')
    assert not check_permutation('aaa', 'bbb')
    assert not check_permutation('nope', 'no')
    assert not check_permutation('abcdef', 'abc')
