import numpy as np
import sys


def read_pos():
    positions = []
    with open('day/7/input.txt') as fv:
        for row in fv:
            positions = list(map(int, row.split(',')))
    return np.array(positions)


def day07a():
    positions = read_pos()
    min_pos = min(positions)
    max_pos = max(positions)
    least_fuel_required = sys.maxsize
    least_fuel_required_index = -1
    for i in range(min_pos, max_pos + 1):
        fuel_required = np.sum(np.abs(positions - i))
        if fuel_required < least_fuel_required:
            least_fuel_required_index = i
            least_fuel_required = fuel_required
    return least_fuel_required


if __name__ == '__main__':
    print(day07a())
