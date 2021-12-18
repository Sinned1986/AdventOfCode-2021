#  Day 13: Transparent Origami

import numpy
import numpy as np


def read_points_and_operations(file_name):
    points = []  # points
    ops = []  # operations
    with open(file_name) as fv:
        while True:
            row = fv.readline()
            if row[0] == '\n':
                break
            points.append(list(map(int, row[:-1].split(','))))

        while True:
            row = fv.readline()
            if len(row) == 0:
                break
            tmp = row[:-1].split('=')
            ops.append([tmp[0][-1], int(tmp[1])])

    return points, ops


def create_page(points):
    x_max = 0
    y_max = 0
    for p in points:
        x_max = max(x_max, p[0])
        y_max = max(y_max, p[1])

    page = np.zeros([y_max+1, x_max+1], dtype=bool)
    for p in points:
        page[p[1], p[0]] = True

    return page


def fold_page(page, ops):
    if ops is None or len(ops) == 0:
        return page

    op = ops.pop(0)
    if op[0] == 'x':
        len_row = len(page[0])
        len_left = op[1]
        len_right = len_row - op[1] - 1
        if len_left >= len_right:
            for x in range(1, 1 + len_right):
                a = page[:, op[1] - x]
                b = page[:, op[1] + x]
                c = a | b
                page[:, op[1] - x] = c
            return fold_page(page[:, 0:op[1]], ops)
        else:
            for x in range(1, 1 + len_left):
                a = page[:, op[1] + x]
                b = page[:, op[1] - x]
                c = a | b
                page[:, op[1] + x] = c
            return fold_page(page[:, op[1] + 1:len(page[0])], ops)
    elif op[0] == 'y':
        len_column = len(page)
        len_top = op[1]
        len_bottom = len_column - op[1] - 1
        if len_top >= len_bottom:
            for y in range(1, 1 + len_bottom):
                a = page[op[1] - y, :]
                b = page[op[1] + y, :]
                c = a | b
                page[op[1] - y, :] = c
            return fold_page(page[0:op[1], :], ops)
        else:
            for y in range(1, 1 + len_top):
                a = page[op[1] - y, :]
                b = page[op[1] + y, :]
                c = a | b
                page[op[1] + y, :] = c
            return fold_page(page[op[1] + 1:len(page), :], ops)


def setup(input_file):
    points, ops = read_points_and_operations(input_file)
    page = create_page(points)

    return page, ops


def find_spaces(page):
    spaces = []

    for x in range(0, len(page[0])):
        if not numpy.any(page[:, x]):
            spaces.append(x)

    return spaces

pattern = {
    'A': np.array(
        [
             [0, 1, 1, 0],
             [1, 0, 0, 1],
             [1, 0, 0, 1],
             [1, 1, 1, 1],
             [1, 0, 0, 1],
             [1, 0, 0, 1],
        ], dtype=bool
    ),
    'E': np.array(
        [
             [1, 1, 1, 1],
             [1, 0, 0, 0],
             [1, 1, 1, 0],
             [1, 0, 0, 0],
             [1, 0, 0, 0],
             [1, 1, 1, 1],
        ], dtype=bool
    ),
    'F': np.array(
        [
            [1, 1, 1, 1],
            [1, 0, 0, 0],
            [1, 1, 1, 0],
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [1, 0, 0, 0],
        ], dtype=bool
    ),
    'G': np.array(
        [
            [0, 1, 1, 0],
            [1, 0, 0, 1],
            [1, 0, 0, 0],
            [1, 0, 1, 1],
            [1, 0, 0, 1],
            [0, 1, 1, 1],
        ], dtype=bool
    ),
    'J': np.array(
        [
            [0, 0, 1, 1],
            [0, 0, 0, 1],
            [0, 0, 0, 1],
            [0, 0, 0, 1],
            [1, 0, 0, 1],
            [0, 1, 1, 0],
        ], dtype=bool
    ),
    'K': np.array(
        [
            [1, 0, 0, 1],
            [1, 0, 1, 0],
            [1, 1, 0, 0],
            [1, 0, 1, 0],
            [1, 0, 1, 0],
            [1, 0, 0, 1],
        ], dtype=bool
    ),
    'U': np.array(
        [
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [0, 1, 1, 0],
        ], dtype=bool
    )
}


def convert_pattern_to_char(unknown_char):
    for k, v in pattern.items():
        if np.array_equal(v, unknown_char):
            return k

    raise Exception('unknown pattern')


def day13b(input_file):
    page, ops = setup(input_file)

    folded_page = fold_page(page, ops)
    spaces = find_spaces(folded_page)
    spaces.insert(0, -1)

    chars = []
    for x in range(0, len(spaces)-1):
        #print(folded_page[:, spaces[x]+1:spaces[x+1]].astype(int))  # print char and add char manually to the pattern array if a new char appears in the input.txt
        char = convert_pattern_to_char(folded_page[:, spaces[x]+1:spaces[x+1]])
        chars.append(char)
    return ''.join(chars)


def day13a(input_file):
    page, ops = setup(input_file)
    page = fold_page(page, ops[0:1])

    return sum(sum(page))


if __name__ == '__main__':
    print(day13a('day/13/input.txt'))
    print(day13b('day/13/input.txt'))
