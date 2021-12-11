import numpy as np
import colorama


def read_map():
    height_map = []
    with open('day/9/input.txt') as fv:
        for row in fv:
            row_str_list = list(row[:-1])
            row_int_list = list(map(int, row_str_list))
            heights_in_row = np.array(row_int_list, dtype=np.int8)
            height_map.append(heights_in_row)

    return np.stack(height_map, axis=0)


def calc_diff_maps(height_map):
    len_y = len(height_map)
    len_x = len(height_map[0])
    diff_map_x = np.zeros([len_y, len_x - 1], dtype=height_map.dtype)
    diff_map_y = np.zeros([len_y - 1, len_x], dtype=height_map.dtype)

    for y in range(0, len_y):
        for x in range(0, len_x - 1):
            diff_map_x[y][x] = height_map[y][x + 1] - height_map[y][x]

    for y in range(0, len_y - 1):
        for x in range(0, len_x):
            diff_map_y[y][x] = height_map[y + 1][x] - height_map[y][x]

    return [diff_map_x, diff_map_y]


def color_number(local_mins, y, x, real_value):
    modifiers = []

    if local_mins[y][x]:
        modifiers.append(colorama.Fore.RED)
        modifiers.append(colorama.Fore.RESET)

    if len(modifiers) == 0:
        return f'{real_value:2}'
    if len(modifiers) == 2:
        return f'{modifiers[0]}{real_value:2}{modifiers[-1]}'


def day09a():
    height_map = read_map()
    #height_map = height_map[:10]

    diff_map_x, diff_map_y = calc_diff_maps(height_map)
    local_mins = np.zeros([len(height_map), len(height_map[0])], dtype=bool)

    for yi in range(1, len(height_map) - 1):
        for xi in range(1, len(height_map[0]) - 1):
            if (diff_map_x[yi][xi - 1] < 0) and \
                    (diff_map_x[yi][xi] > 0) and \
                    (diff_map_y[yi - 1][xi] < 0) and \
                    (diff_map_y[yi][xi] > 0):
                local_mins[yi][xi] = 1

        # edge case left
        xi = 0
        if (diff_map_x[yi][xi] > 0) and \
                (diff_map_y[yi - 1][xi] < 0) and \
                (diff_map_y[yi][xi] > 0):
            local_mins[yi][xi] = 1

        # edge case right
        xi = len(height_map[0])-1
        if (diff_map_x[yi][xi - 1] < 0) and \
                (diff_map_y[yi - 1][xi] <= 0) and \
                (diff_map_y[yi][xi] > 0):
            local_mins[yi][xi] = 1

    # edge case top row
    yi = 0
    for xi in range(1, len(height_map[0]) - 2):
        if (diff_map_x[yi][xi - 1] < 0) and \
                (diff_map_x[yi][xi] > 0) and \
                (diff_map_y[yi][xi] > 0):
            local_mins[yi][xi] = 1

    # edge case top row + left
    xi = 0
    if (diff_map_x[yi][xi] > 0) and \
            (diff_map_y[yi][xi] > 0):
        local_mins[yi][xi] = 1

    # edge case top row + right
    if (diff_map_x[yi][xi] > 0) and \
            (diff_map_y[yi][xi] > 0):
        local_mins[yi][xi] = 1

    # edge case bottom row
    yi = len(height_map) - 1
    for xi in range(1, len(height_map[0]) - 1):
        if (diff_map_x[yi][xi - 1] < 0) and \
                (diff_map_x[yi][xi] > 0) and \
                (diff_map_y[yi - 1][xi] < 0):
            local_mins[yi][xi] = 1

    # edge case bottom row + left
    xi = 0
    if (diff_map_x[yi][xi] > 0) and \
            (diff_map_y[yi - 1][xi] < 0):
        local_mins[yi][xi] = 1

    # edge case bottom row +  right
    xi = len(height_map[0]) - 1
    if (diff_map_x[yi][xi - 1] < 0) and \
            (diff_map_y[yi - 1][xi] < 0):
        local_mins[yi][xi] = 1

    risk_map = ((height_map + 1) * local_mins)
    print('%d mins found, sum of risk of  all values' % sum(sum(local_mins)), sum(sum(risk_map)))

    map_str = ''
    for yi in range(0, len(height_map)):
        row_str = ''.join(['{}'] * len(height_map[0])).format(*[color_number(local_mins, yi, xi, height_map[yi][xi]) for xi in range(0, len(height_map[yi]))])
        map_str = map_str + row_str + '\n'

    return sum(sum(risk_map)), map_str

def day09b():
    pass


if __name__ == '__main__':
    r, m = day09a()
    print(r)
    print(m)
    print(day09b())
