def check_neighbors(lamp, query):
    lamp_x = lamp[0]
    lamp_y = lamp[1]
    query_x = query[0]
    query_y = query[1]

    return abs(lamp_x - query_x) <= 1 and abs(lamp_y - query_y) <= 1


def check_diag_one(n, lamp, query):
    # move up and right
    i = lamp[0]
    j = lamp[1]
    while i <= n and j <= n:
        if i == query[0] and j == query[1]:
            return True
        i += 1
        j += 1

    # move down and left
    i = lamp[0]
    j = lamp[1]
    while i > 0 and j > 0:
        if i == query[0] and j == query[1]:
            return True
        i += -1
        j += -1


def check_diag_two(n, lamp, query):
    # move down and right
    i = lamp[0]
    j = lamp[1]
    while i <= n and j > 0:
        if i == query[0] and j == query[1]:
            return True
        i += 1
        j += -1

    # move up and left
    i = lamp[0]
    j = lamp[1]
    while i > 0 and j <= n:
        if i == query[0] and j == query[1]:
            return True
        i += -1
        j += 1


def compare_two_points(n, lamp, query):
    # given two points:

    # if they are neighbors, lamp is shut off and doesn't illuminate point:
    if check_neighbors(lamp, query):
        return False

    # is point A in the vertical of B?
    if lamp[0] == query[0]:
        return True

    # is point A in the horizontal of B
    if lamp[1] == query[1]:
        return True

    # is point A in the / diag of B?
    if check_diag_one(n, lamp, query):
        return True

    # is point A in the \ diag of B?
    if check_diag_two(n, lamp, query):
        return True


def run_query(n, lamps, query_point):
    comparisons = [compare_two_points(n, l, query_point) for l in lamps]
    return True in comparisons


def run_queries(n, lamps, queries):
    return [run_query(n, lamps, query) for query in queries]


def test_case1():
# x o o o o o
# o o o o o o
# o o o o o o
# o o o o o o
# o o o o o o
# o o o o o o

    n = 6
    lamps = [(1,5)]
    queries = [(5,5)]
    expected = [True]
    assert expected == run_queries(5, lamps, queries)


def test_case2():
# x o o o o o
# o o x o o o
# o o ? x o o
# o o o o o o
# o o o o o o
# o o o o o o

    n = 6
    lamps = [(1,5), (3,4), (4,3)]
    queries = [(3,3)]
    expected = [True]
    assert expected == run_queries(5, lamps, queries)


def test_case3():
# o o o o o o
# o o x o o o
# o o ? x o o
# o o o o o o
# o o o o o o
# o o o o o o

    n = 6
    lamps = [(3,4), (4,3)]
    queries = [(3,3)]
    expected = [False]
    assert expected == run_queries(5, lamps, queries)


def test_case4():
# o o o o o o
# o o x o o o
# o o x x o o
# o o o o o o
# ? o o o o ?
# o o o o o o

    n = 6
    lamps = [(3,3), (3,4), (4,3)]
    queries = [(5, 2), (1,1), (4,4)]
    expected = [True, True, False]
    assert expected == run_queries(5, lamps, queries)


def test_neighbors():
    assert check_neighbors((1,1), (2,2))
    assert not check_neighbors((1,5), (2,2))
    assert check_neighbors((1,5), (2,5))


test_case1()
test_case2()
test_case3()
test_case4()
