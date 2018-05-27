# 1.8 Zero Matrix:
# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.

def get_zeroes(m):
    zeroes = []
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 0:
                zeroes.append((i, j))

    return zeroes

def zero_matrix(m):
    for cell in get_zeroes(m):
        row = cell[0]
        col = cell[1]
        # zero out the row
        m[row] = [0] * (len(m[row]))
        # zero out the col
        for i in range(len(m)):
            m[i][col] = 0

    return m


if __name__ == '__main__':
    # test 0x0
    assert zero_matrix([[]]) == [[]]

    # test 1x1
    assert zero_matrix([[1]]) == [[1]]
    assert zero_matrix([[0]]) == [[0]]

    # test 2x2
    m = [[1, 0],
         [3, 4]]
    m_zero = [[0, 0],
              [3, 0]]
    assert zero_matrix(m) == m_zero

    # test 3x3 - 1
    m = [[1, 2, 4],
         [4, 0, 6],
         [7, 8, 9]]
    m_zero = [[1, 0, 4],
              [0, 0, 0],
              [7, 0, 9]]
    assert zero_matrix(m) == m_zero

    # test 3x3 - 2
    m = [[1, 2, 4],
         [0, 0, 6],
         [7, 8, 9]]
    m_zero = [[0, 0, 4],
              [0, 0, 0],
              [0, 0, 9]]
    assert zero_matrix(m) == m_zero

    # test 3x3 - 3
    m = [[0, 2, 4],
         [4, 0, 6],
         [7, 8, 0]]
    m_zero = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    assert zero_matrix(m) == m_zero
