from random import random, randint

class Conway:
    def __init__(self, initial_cells, board_size):
        self.cells = initial_cells
        self.previous_state = {}
        self.board_size = board_size
        self.is_locked = False

    def run_iteration(self):
        next_gen = {}

        for cell in self.cells:
            new_cells = self.evolve(cell)
            for cell in new_cells:
                next_gen[cell] = True

        self.is_locked = (self.previous_state == next_gen)

        self.previous_state = self.cells
        self.cells = next_gen

    def evolve(self, cell):
        next_gen = []
        n = self.get_neighbors(cell)

        # Any live cell with fewer than two live neighbors dies, as if by underpopulation.
        # Any live cell with more than three live neighbors dies, as if by overpopulation.
        if len(n) < 2 or len(n) > 3:
            pass

        # Any live cell with two or three live neighbors lives on to the next generation.
        if len(n) in [2, 3]:
            next_gen.append(cell)

        # Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
        # Any one of the neighboring positions of our currently considered live cell is a candidate for reproduction
        # Check for 3 neighbor case for all 8 neighboring positions:
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):
                loc = ((i + self.board_size) % self.board_size, (j + self.board_size) % self.board_size)
                if loc != cell and not self.cells.get(loc, False) and len(self.get_neighbors(loc)) == 3:
                    next_gen.append(loc)

        return next_gen

    def get_neighbors(self, cell):
        neighbors = []
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):
                loc = ((i + self.board_size) % self.board_size, (j + self.board_size) % self.board_size)
                if loc != cell and self.cells.get(loc, False):
                    neighbors.append(loc)

        return neighbors

    def get_circular_position(x):
        if x < 0:
            return self.board_size


def setup_game(board_size, rand_init=False):
    # single blinker
    initial_cells = {(2,1): True, (2,2): True, (2,3): True}

    # single blinker - on edge to test sphere board
    # initial_cells = {(0,1): True, (0,2): True, (0,3): True}

    # many blinkers
    # initial_cells = {(2,1): True, (2,2): True, (2,3): True,
    #                  (1,7): True, (2,7): True, (3,7): True,
    #                  (7,5): True, (7,6): True, (7,7): True,
    #                  (6,2): True, (7,2): True, (8,2): True,}

    # single glider
    # initial_cells = {(1,0): True, (2,1): True, (0,2): True,
    #                  (1,2): True, (2,2): True}

    # a whole mess of things
    # initial_cells = {
    #     # glider 1
    #     (1,0): True, (2,1): True, (0,2): True,(1,2): True, (2,2): True,
    #
    #     # blinker 2
    #     (10,5): True, (10,6): True, (10,7): True, (10,8): True
    # }

    if rand_init:
        initial_cells = get_random_cells(board_size)

    return Conway(initial_cells, board_size)


def get_random_cells(board_size):
    initial_cells = {}
    for i in range(0, board_size):
        for j in range(0, board_size):
            if random() > 0.5:
                initial_cells[(i,j)] = True
    return initial_cells

# config things here, always use variables below
CELL_SIZE = 8
CELL_COUNT = 100
BACKGROUND_COLOR = 0
LIGHT_GREY = 105
LIVE_COLOR_TUPLE = (50, 205, 50)
LOCKED_LIVE_COLOR_TUPLE = (165, 242, 243)
FRAME_RATE = 25
THICK = 2
THIN = 1
board_is_locked = False
pause_if_locked = False
game = setup_game(CELL_COUNT, True)


def draw_board():
    stroke(BACKGROUND_COLOR)
    strokeWeight(THICK)
    for i in range(CELL_COUNT):
        for j in range(CELL_COUNT):
            rect(i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    reset_colors()


def draw_cells(cells, board_is_locked):
    stroke(BACKGROUND_COLOR)
    strokeWeight(THICK)
    if board_is_locked:
        fill(*LOCKED_LIVE_COLOR_TUPLE)
    else:
        fill(*LIVE_COLOR_TUPLE)

    for cell in cells:
        rect(cell[0] * CELL_SIZE, cell[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    reset_colors()


def setup():
    frameRate(FRAME_RATE)
    size(CELL_SIZE * CELL_COUNT, CELL_SIZE * CELL_COUNT)
    background(BACKGROUND_COLOR)
    reset_colors()


def reset_colors():
    stroke(BACKGROUND_COLOR)
    fill(BACKGROUND_COLOR)
    strokeWeight(THIN)


def draw():
    global board_is_locked
    draw_board()
    draw_cells(game.cells, board_is_locked)
    reset_colors()
    if not board_is_locked:
        game.run_iteration()
        board_is_locked = game.is_locked and pause_if_locked


def mouseDragged():
    game.cells[(mouseX / CELL_SIZE, mouseY / CELL_SIZE)] = True


def mousePressed():
    game.cells[(mouseX / CELL_SIZE, mouseY / CELL_SIZE)] = True

def keyPressed():
    global board_is_locked, LIVE_COLOR_TUPLE

    if key == CODED:
        print('coded key pressed')
        if keyCode == UP:
            frameRate(frameRate + 2)
        elif keyCode == DOWN:
            frameRate(frameRate - 2)
    elif key in [' ', '\n']:
        board_is_locked = not board_is_locked
    elif key == 'q':
        quit()
    elif key in ['r', 'i']:
        game.cells = get_random_cells(CELL_COUNT)
    elif key == 'd':
        game.cells = {}
    elif key == 'c':
        LIVE_COLOR_TUPLE = (randint(0, 255), randint(0, 255), randint(0, 255))
