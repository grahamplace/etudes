# 1.3 URLify:
# Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end to hold the additional characters,
# and that you are given the "true" length of the string.

def urlify(s):
    return s.replace(' ', '%20')


if __name__ == '__main__':
    assert urlify('Mr John Smith') == 'Mr%20John%20Smith'
    assert urlify(' ') == '%20'
