import sys

from data.ColorSequence import ColorSequence


def __construct_file_name(file_name: str) -> str:
    return f"tests/{file_name}"


def __read_file(file_name: str) -> str:
    name = __construct_file_name(file_name)
    curr_file = open(name, 'r')
    content = curr_file.read()
    curr_file.close()
    return content


def __get_all_lines_from_file(file_content: str) -> list[str]:
    return file_content.split('\n')


def __get_elements_from_row(all_rows: list[str], row_index: int, separator: str, elements_count: int) -> list[str]:
    return all_rows[row_index].split(separator)[:elements_count]


def __create_color_sequence(file_name: str) -> ColorSequence:
    lines = __get_all_lines_from_file(__read_file(file_name))
    size = tuple([int(x) for x in lines.pop(0).split(' ')])
    elements = [__get_elements_from_row(lines, row, ' ', size[1]) for row in range(size[0])]
    return ColorSequence(size, elements)


def __get_max_color_sequence_for_file(file_name: str) -> int:
    color_sequence = __create_color_sequence(file_name)
    return color_sequence.max_sequence()


if __name__ == '__main__':
    for test_case in sys.argv[1:]:
        print(__get_max_color_sequence_for_file(test_case))
