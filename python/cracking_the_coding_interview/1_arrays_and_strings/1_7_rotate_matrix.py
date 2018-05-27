# 1.7 Rotate Matrix:
# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes,
#    write a method to rotate the image by 90 degrees.
# Can you do this in place?

def rotate_matrix(m):

    if len(m[0]) == 0: return [[]]

    # init empty matrix to fill and return
    m_90 = []
    for i in range(len(m)): m_90.append([None] * len(m))

    # to rotate 90 degrees, rows become cols, built in reverse order
    # e.g. row 1 becomes column length - 1
    # iterate over each row
    for i in range(len(m)):
        # insert row i into correct col position (across row lists):
        for j in range(len(m)):
            m_90[j][len(m) - i - 1] = m[i][j]

    return m_90

if __name__ == '__main__':
    # test 0x0
    assert rotate_matrix([[]]) == [[]]

    # test 1x1
    assert rotate_matrix([[1]]) == [[1]]

    # test 2x2
    m = [[1, 2],
         [3, 4]]
    m_90 = [[3, 1],
            [4, 2]]
    assert rotate_matrix(m) == m_90

    # test 3x3
    m = [[1, 2, 4],
         [4, 5, 6],
         [7, 8, 9]]
    m_90 = [[7, 4, 1],
            [8, 5, 2],
            [9, 6, 4]]
    assert rotate_matrix(m) == m_90
