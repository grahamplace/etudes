class Conway:
    def __init__(self, start, iterations):
        self.state = start
        self.iterations = iterations

    def run_iteration(self):
        temp = [[None for i in self.state[0]] for i in self.state]
        for row in xrange(len(self.state)):
            for col in xrange(len(self.state[0])):
                neighbors = self.get_neighbors(row, col)
                if self.state[row][col] and neighbors < 2:
                    temp[row][col] = False
                elif self.state[row][col] and neighbors < 4:
                    temp[row][col] = True
                elif self.state[row][col]:
                    temp[row][col] = False
                elif neighbors == 3:
                    temp[row][col] = True
                else:
                    temp[row][col] = False
        for row in temp:
            print row
        print
        self.state = temp

    def run_iterations(self):
        for i in xrange(self.iterations):
            self.run_iteration()

    def get_neighbors(self, row, col):
        neighbors = 0
        for r in xrange(row - 1, row + 2):
            for c in xrange(col - 1, col + 2):
                if ((not (r == row and c == col)) and
                    r >= 0 and r < len(self.state) and
                    c >= 0 and c < len(self.state[0]) and
                    self.state[r][c]):
                    neighbors += 1
        return neighbors


def setup_game():
    # board = [  # blinkers
    #     [False, False, False, False, False, False, False, False, False, False],
    #     [False, False, True, False, False, False, False, False, False, False],
    #     [False, False, True, False, False, False, True, True, True, False],
    #     [False, False, True, False, False, False, False, False, False, False],
    #     [False, False, False, False, False, False, False, False, False, False],
    #     [False, False, False, False, False, False, False, False, False, False],
    #     [False, False, False, False, False, False, False, True, False, False],
    #     [False, True, True, True, False, False, False, True, False, False],
    #     [False, False, False, False, False, False, False, True, False, False],
    #     [False, False, False, False, False, False, False, False, False, False]
    # ]
    board = [  # glider
        [False, True, False, False, False, False, False, False, False, False],
        [False, False, True, False, False, False, False, False, False, False],
        [True, True, True, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False]
    ]
    return Conway(board, 0)

# config things here, always use variables below
CELL_SIZE = 20
CELL_COUNT = 10
background_color = 0
LIGHT_GREY = 105
LIVE_COLOR_TUPLE = (50, 205, 50)
FRAME_RATE = 2
THICK = 2
THIN = 1
game = setup_game()


def draw_cells(board):
    stroke(LIGHT_GREY)
    strokeWeight(THICK)
    for i in range(CELL_COUNT):
        for j in range(CELL_COUNT):
            if board[i][j]:
                fill(*LIVE_COLOR_TUPLE)
            else:
                fill(background_color)
            rect(i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE)

    reset_colors()


def setup():
    frameRate(FRAME_RATE)
    size(CELL_SIZE * CELL_COUNT, CELL_SIZE * CELL_COUNT)
    background(background_color)
    reset_colors()


def reset_colors():
    stroke(background_color)
    fill(background_color)
    strokeWeight(THIN)


def draw():
    draw_cells(game.state)
    reset_colors()
    game.run_iteration()
