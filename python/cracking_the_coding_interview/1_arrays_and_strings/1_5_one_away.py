# 1.5 One Away:
# There are three types of edits that can be performed on strings:
#   a. insert a character
#   b. remove a character
#   c. replace a character
# Given two strings, write a function to check if they are one edit (or zero edits) away.

def edit_distance(a: str, b: str, m: int, n: int) -> int:
    # a is empty, we would have to insert all n chars of b into a
    if m == 0:
        return n

    # b is empty, we would have to remove all m chars of a to get a, b = ''
    if n == 0:
        return m

    # last chars match, nothing to do here -- move right along
    if a[m - 1] == b[n - 1]:
        return edit_distance(a, b, m - 1, n - 1)

    # last chars don't match, this is the tricky part
    # we can do one of our three operations to a,
    #   each of which requires 1 edit + edit distance of modified a, b
    # try all three, and use the min edit distance
    # Example:
    # abc|d, abe|d: uh-oh, c != e
    # insert: abc|ed,  ab|ed
    # remove:  ab|d,  abe|d
    # replace: ab|ed,  ab|ed 
    if a[m - 1] != b[n - 1]:
        return 1 + min(edit_distance(a, b, m, n - 1),      # insert char into a
                       edit_distance(a, b, m - 1, n),      # remove char from a
                       edit_distance(a, b, m - 1, n - 1))  # replace a char in a



def one_away(a: str, b: str) -> bool:
    return edit_distance(a, b, len(a), len(b)) <= 1


if __name__ == '__main__':
    assert one_away('same', 'same')
    assert one_away('a', 'b')
    assert one_away('a', '')
    assert one_away('ab', 'a')
    assert one_away('ab', 'abc')
    assert one_away('cat', 'bat')

    assert not one_away('abc', '')
    assert not one_away('', 'abc')
    assert not one_away('nope', 'yepp')
    assert not one_away('.!?', 'abc')
    assert not one_away('abcd', 'ab')
