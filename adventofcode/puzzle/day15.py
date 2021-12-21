# Day 15: Chiton

import numpy as np
from enum import Enum
import sys

def read_map(file_name):
    cavern_map_rows = []
    with open(file_name) as fv:
        for row in fv:
            if row != '':
                cavern_map_rows.append(np.array(list(map(int, list(row[:-1]))), dtype=np.uint8))
    return np.stack(cavern_map_rows)


def add_border_to_cavern_map(cavern_map):
    new_row = np.array([9]*len(cavern_map[0]))
    new_column = np.array([[9], ]*(len(cavern_map)+2), )
    tmp_array = np.vstack((new_row, cavern_map, new_row))
    cavern_map_with_border = np.hstack((new_column, tmp_array, new_column))
    return cavern_map_with_border


class Prev(Enum):
    NONE = 0
    LEFT = 1
    RIGHT = 2
    TOP = 3
    BOTTOM = 4
    START = 5
    END = 6


def calc_cost(cavern_array, cost_array, prev_array, y, x):
    cost = cost_array[y, x]
    if y > 0:
        if cavern_array[y - 1, x] + cost < cost_array[y - 1, x]:
            cost_array[y - 1, x] = cavern_array[y - 1, x] + cost
            prev_array[y - 1, x] = Prev.BOTTOM.value
            calc_cost(cavern_array, cost_array, prev_array, y - 1, x)
    if x > 0:
        if cavern_array[y, x - 1] + cost < cost_array[y, x - 1]:
            cost_array[y, x - 1] = cavern_array[y, x - 1] + cost
            prev_array[y, x - 1] = Prev.RIGHT.value
            calc_cost(cavern_array, cost_array, prev_array, y, x - 1)
    if y < len(cavern_array) - 1:
        if cavern_array[y + 1, x] + cost < cost_array[y + 1, x]:
            cost_array[y + 1, x] = cavern_array[y + 1, x] + cost
            prev_array[y + 1, x] = Prev.TOP.value
            calc_cost(cavern_array, cost_array, prev_array, y + 1, x)
    if x < len(cavern_array[0]) - 1:
        if cavern_array[y, x + 1] + cost < cost_array[y, x + 1]:
            cost_array[y, x + 1] = cavern_array[y, x + 1] + cost
            prev_array[y, x + 1] = Prev.LEFT.value
            calc_cost(cavern_array, cost_array, prev_array, y, x + 1)


def mask_shortest_path(prev_array):
    is_in_shortest_path_array = np.zeros(prev_array.shape, dtype=bool)
    x = 0
    y = 0
    abort_cond = len(prev_array) * len(prev_array[0])
    i = 0
    while x != len(prev_array[0]) - 1 and y != len(prev_array) - 1:
        is_in_shortest_path_array[y, x] = True
        prev = prev_array[y, x]
        if prev == Prev.BOTTOM.value:
            y = y + 1
        elif prev == Prev.RIGHT.value:
            x = x + 1
        elif prev == Prev.TOP.value:
            y = y - 1
        elif prev == Prev.LEFT.value:
            x = x - 1
        i += 1
        if i > abort_cond:
            raise Exception('invalid prev path')

    return is_in_shortest_path_array


def day15a(input_file_name):
    cavern_array = read_map(input_file_name)
    prev_array = np.zeros(cavern_array.shape, dtype=np.uint8)
    cost_array = np.full(shape=cavern_array.shape, fill_value=np.iinfo(int).max, dtype=int)
    prev_array[-1, -1] = Prev.END.value
    cost_array[-1, -1] = cavern_array[-1, -1]

    sys.setrecursionlimit(cavern_array.size*10)

    for y in range(len(cavern_array) - 1, 0, -1):
        for x in range(len(cavern_array[0]) - 1, 0, -1):
            #cavern_array, cost_array, prev_array = calc_cost(cavern_array, cost_array, prev_array, y, x)
            calc_cost(cavern_array, cost_array, prev_array, y, x)
    masked_path = 1*mask_shortest_path(prev_array)

    return cost_array[0, 0] - cavern_array[0, 0]


if __name__ == '__main__':
    print(day15a('day/15/example.txt'))
    print(day15a('day/15/input.txt'))

