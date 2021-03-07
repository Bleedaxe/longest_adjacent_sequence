__steps = (
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
)


def __is_valid_position(size: (int, int), row: int, col: int):
    return 0 <= row < size[0] and 0 <= col < size[1]


def find_longest_sequence(elements: list[list[str]], size: (int, int), row: int, col: int) -> int:
    if not __is_valid_position(size, row, col):
        return 0

    element = elements[row][col]
    elements_copy = [row[:] for row in elements[:]]
    elements_copy[row][col] = ''

    max_sequence = 0
    for step in __steps:
        curr_row = row + step[0]
        curr_col = col + step[1]
        if __is_valid_position(size, curr_row, curr_col) and elements_copy[curr_row][curr_col] == element:
            max_sequence = max(max_sequence, find_longest_sequence(elements_copy, size, curr_row, curr_col))

    return max_sequence + 1


class ColorSequence:

    def __init__(self, size: (int, int), elements: list[list[str]]):
        self.size = size
        self.elements = elements

    def max_sequence(self) -> int:
        if self.__are_all_elements_equal():
            return self.size[0] * self.size[1]

        max_sequence = max(
            [find_longest_sequence(self.elements, self.size, row, col)
             for row in range(0, self.size[0]) for col in range(0, self.size[1])] + [0]
        )

        return max_sequence

    def __are_all_elements_equal(self) -> bool:
        return len(set([element for row in self.elements for element in row])) == 1
