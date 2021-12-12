import copy

import numpy as np

def read_energy_map():
    rows = []
    with open('day/11/input.txt') as fv:
        for row in fv:
            rows.append(np.array(list(row[:-1]), dtype=np.uint8))

    return np.stack(rows)

def add_border_to_map(start_map, border_size):
    shape = start_map.shape
    new_map = []
    h_border = np.zeros([1, start_map.shape[1]], dtype=start_map.dtype)
    v_border = np.zeros([start_map.shape[0]+2 * border_size, 1], dtype=start_map.dtype)

    start_map = np.append(h_border, start_map, axis=0)
    start_map = np.append(start_map, h_border, axis=0)
    start_map = np.append(v_border, start_map, axis=1)
    start_map = np.append(start_map, v_border, axis=1)


    return start_map

def day11a():
    border_size = 1
    start_map = add_border_to_map(read_energy_map(), border_size)
    flash_counter = 0
    for i in range(0, 100):
        flashed_in_this_cycle = np.zeros(start_map.shape, dtype=bool)
        start_map += 1
        cycle_not_done = True
        while cycle_not_done:
            cycle_not_done = False
            for yi in range(border_size, len(start_map)-border_size):
                for xi in range(border_size, len(start_map[0])-border_size):
                    if start_map[yi][xi] > 9 and not flashed_in_this_cycle[yi][xi]:
                        flashed_in_this_cycle[yi][xi] = True
                        start_map[yi-1:yi+2, xi-1:xi+2] += 1
                        cycle_not_done = True
                        flash_counter += 1
        start_map *= np.invert(flashed_in_this_cycle)

    return flash_counter


if __name__ == '__main__':
    print(day11a())
