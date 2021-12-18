# Day 9: Smoke Basin

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


def color_number2(local_mins, y, x, real_value, class_value):
    modifiers = []
    color_codes = [
        colorama.Back.BLACK,
        colorama.Back.RED,
        colorama.Back.GREEN,
        colorama.Back.YELLOW,
        colorama.Back.BLUE,
        colorama.Back.MAGENTA,
        colorama.Back.CYAN,
        colorama.Back.WHITE,
    ]

    if local_mins[y][x]:
        modifiers.append(colorama.Fore.RED)
        modifiers.append(colorama.Fore.RESET)

    if class_value != 0:
        color_code = (class_value % len(color_codes))
        modifiers.append(color_codes[color_code])
        modifiers.append(colorama.Back.RESET)

    if len(modifiers) == 0:
        return f'{real_value:2}'
    if len(modifiers) == 2:
        return f'{modifiers[0]}{real_value:2}{modifiers[-1]}'
    if len(modifiers) == 4:
        return f'{modifiers[0]}{modifiers[2]}{real_value:2}{modifiers[1]}{modifiers[3]}'


def day09a():
    height_map = read_map()

    local_mins = calc_local_mins_array(height_map)

    risk_map = ((height_map + 1) * local_mins)

    map_str = ''
    for yi in range(0, len(height_map)):
        row_str = ''.join(['{}'] * len(height_map[0])).format(*[color_number(local_mins, yi, xi, height_map[yi][xi]) for xi in range(0, len(height_map[yi]))])
        map_str = map_str + row_str + '\n'

    return sum(sum(risk_map)), map_str


def calc_local_mins_array(height_map):
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
        xi = len(height_map[0]) - 1
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

    return local_mins

def get_local_mins_to_list(local_mins):
    local_mins_list = []
    for y in range(0,len(local_mins)):
        for x in range(0, len(local_mins[0])):
            if local_mins[y][x] == 1:
                local_mins_list.append([y, x],)

    return local_mins_list


def find_basin(height_map, visited_fields, current_pos):
    if (current_pos[0] < 0) or (current_pos[0] >= len(height_map)) or (current_pos[1] < 0) or (current_pos[1] >= len(height_map[0])):
        return visited_fields

    if visited_fields[current_pos[0]][current_pos[1]]:
        return visited_fields

    if height_map[current_pos[0]][current_pos[1]] == 9:
        return visited_fields


    visited_fields[current_pos[0]][current_pos[1]] = True
    visited_fields = find_basin(height_map, visited_fields, [current_pos[0], current_pos[1] + 1])
    visited_fields = find_basin(height_map, visited_fields, [current_pos[0], current_pos[1] - 1])
    visited_fields = find_basin(height_map, visited_fields, [current_pos[0] + 1, current_pos[1]])
    visited_fields = find_basin(height_map, visited_fields, [current_pos[0] - 1, current_pos[1]])

    return visited_fields


def day09b():
    height_map = read_map()

    local_mins = calc_local_mins_array(height_map)
    local_mins_list = get_local_mins_to_list(local_mins)

    class_map = np.zeros([len(height_map), len(height_map[0])], dtype=np.uint8)
    largest_fields = []

    for i, p_local_min in enumerate(local_mins_list):
        visited_fields = np.zeros([len(local_mins), len(local_mins[0])], dtype=bool)
        visited_fields = find_basin(height_map, visited_fields, p_local_min)
        class_map = class_map + (visited_fields*(i+1)) #  i want to generate a colored map with each basin with an unique identifier
        largest_fields.append(sum(sum(visited_fields)))


    # fancy map
    map_str = ''
    for yi in range(0, len(class_map)):
        row_str = ''.join(['{}'] * len(class_map[0])).format(*[color_number2(local_mins, yi, xi, height_map[yi][xi], class_map[yi][xi]) for xi in range(0, len(class_map[yi]))])
        map_str = map_str + row_str + '\n'

    largest_fields.sort()
    answer = largest_fields[-3] * largest_fields[-2] * largest_fields[-1]

    return answer, map_str


if __name__ == '__main__':
    r, m = day09a()
    print(r)
    #print(m)
    r, m = day09b()
    print(r)
    #print(m)
