# 1.4 Palindrome Permutation:
# Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards.
# A permutation is a rearrangement of letters.
# The palindrome does not need to be limited to just dictionary words.


def check_palindrom_permutation(s):
    # clean up the string
    s = s.lower()
    s = s.replace(' ', '')

    # palindromes must have a "center" character that doesn't have a "partner" reflected
    # thus, at most 1 character can have an odd occurrence count
    char_counts = {}
    for c in list(s):
        char_counts[c] = char_counts.get(c, 0) + 1

    odd_count = 0
    for count in char_counts.values():
        if not count % 2 == 0:
            odd_count += 1
        if odd_count > 1:
            return False

    return True


if __name__ == '__main__':
    assert check_palindrom_permutation('a')
    assert check_palindrom_permutation('Tact Coa')  # "taco cat", "atco eta", etc.)
    assert check_palindrom_permutation('aba')
    assert check_palindrom_permutation('racecar')
    assert check_palindrom_permutation('carrace')
    assert check_palindrom_permutation('A Santa Lived As a Devil At NASA')

    assert not check_palindrom_permutation('graham')
    assert not check_palindrom_permutation('abc')
    assert not check_palindrom_permutation('!?')
