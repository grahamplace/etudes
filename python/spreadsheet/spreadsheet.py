import re

class Sheet:
    def __init__(self, initial_cells={}):
        self.cells = initial_cells  # cells = dict, keys like 'A1'

    def get_display_value(self, cell_key):
        if self.cells.get(cell_key, False):
            return (self.cells[cell_key]).compute_value()

    def set_cell(self, cell_key, input_str):
        parsed_cell = self.parse_input(cell_key, input_str)
        self.cells[cell_key] = parsed_cell
        return True

    def parse_input(self, cell_key, input_str):
        if input_str.startswith('='):
            return self.parse_formula_str(cell_key, input_str)
        else:
            return self.parse_int_str(cell_key, input_str)

    def parse_int_str(self, cell_key, str):
        try:
            int_val = int(str)
            return IntCell(cell_key, self, int_val)
        except:
            return ErrorCell(cell_key, self, 'Could not parse cell')

    def parse_formula_str(self, cell_key, str):
        str = str.replace('=', '')  # TODO: make this smarter to allow '=' in elsewhere
        split = str.split('+')
        if len(split) != 2 or not (self.check_key_validity(split[0]) and self.check_key_validity(split[1])):
            return ErrorCell(cell_key, self, 'Could not parse formula cell')

        for key in split:
            if not self.cells.get(key, False):
                self.set_cell(key, '0')

        return FormulaCell(cell_key, self, split[0], split[1])

    def check_key_validity(self, cell_key):
        if re.search('\A[A-Z].*[0-9].*', cell_key):
            return True
        else:
            return False

class Cell:
    def __init__(self, key, parent_ss):
        self.key = key
        self.parent_ss = parent_ss

    def compute_value(self):
        return None

class FormulaCell(Cell):
    def __init__(self, key, parent_ss, left, right):
        Cell.__init__(self, key, parent_ss)
        self.left_key = left
        self.right_key = right

    def compute_value(self):
        left = self.parent_ss.cells[self.left_key]
        right = self.parent_ss.cells[self.right_key]
        return left.compute_value() + right.compute_value()


class IntCell(Cell):
    def __init__(self, key, parent_ss, value):
        Cell.__init__(self, key, parent_ss)
        self.value = value

    def compute_value(self):
        return self.value

class ErrorCell(Cell):
    def __init__(self, key, parent_ss, value='Broken Cell'):
        Cell.__init__(self, key, parent_ss)
        self.error_code = value


# python tests - OO wrapper
ss = Sheet()
def get_display_value(cell):
  return ss.get_display_value(cell)

def set_cell(cell, value):
  ss.set_cell(cell, value)

# python tests
def assert_get_value(cell, expected_value):
  assert get_display_value(cell) == expected_value, f'Expected: {expected_value}; Got: {get_display_value(cell)}'


# Graham custom test cases
assert ss.check_key_validity('A1')
assert ss.check_key_validity('AZ1')
assert ss.check_key_validity('AZ112')
assert not ss.check_key_validity('1')
assert not ss.check_key_validity('A')
assert not ss.check_key_validity('AA')
assert isinstance(ss.parse_input('A1', '1'), IntCell)
assert isinstance(ss.parse_input('A1', '=A1+B1'), FormulaCell)
assert isinstance(ss.parse_input('A1', '=B1+C1'), FormulaCell)
assert isinstance(ss.parse_input('A1', '=B1*C1'), ErrorCell)
assert isinstance(ss.parse_input('A1', 'B1+C1'), ErrorCell)
assert isinstance(ss.parse_input('A1', '1+1'), ErrorCell)
assert isinstance(ss.parse_input('A1', '=1+1'), ErrorCell)
assert isinstance(ss.parse_input('A1', '=1+A1'), ErrorCell)
assert isinstance(ss.parse_input('A1', '='), ErrorCell)


# Sheet Test Cases
set_cell("A1", "1")
assert_get_value("A1", 1)

set_cell("B1", "2")
set_cell("C1", "=A1+B1")
assert_get_value("C1", 3)

set_cell("A1", "4")
assert_get_value("C1", 6)

set_cell("AAA9999", "7")
assert_get_value("AAA9999", 7)

set_cell("AAA9998", "777")
assert_get_value("AAA9999", 7)

set_cell("C2", "=AAA9999+C1")
assert_get_value("C2", 13)

set_cell("A1", "14")
assert_get_value("C2", 23)

set_cell("C2", "0")
assert_get_value("C2", 0)

print("All tests pass!")
