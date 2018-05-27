# 1.6 String Compression:
# Implement a method to perform basic string compression using the counts of repeated characters.
# For example, the string aabcccccaaa would become a2b1c5a3.
# If the "compressed" string would not become smaller than the original string, your method should return the original string.
# You can assume the string has only uppercase and lowercase letters (a - z).

def compress(s: str) -> str:

    if len(s) <= 1:
        return s

    first_char = s[0]
    occurrences = 1
    for c in list(s)[1:]:
        if c != first_char: break
        occurrences += 1

    compressed = first_char + str(occurrences)
    uncompressed = ''.join((list(s)[occurrences:]))
    return compressed + compress(uncompressed)


def compress_string(s: str) -> str:
    compressed = compress(s)
    if len(compressed) > len(s): return s
    return compressed


if __name__ == '__main__':
    assert compress_string('abc') == 'abc'
    assert compress_string('aaa') == 'a3'
    assert compress_string('aabcccccaaa') == 'a2b1c5a3'
    assert compress_string('aAbcccccaaa') == 'a1A1b1c5a3'
    assert compress_string('') == ''
