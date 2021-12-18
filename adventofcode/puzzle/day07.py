# Day 7: The Treachery of Whales

import numpy as np
import sys
from functools import partial


def read_pos():
    positions = []
    with open('day/7/input.txt') as fv:
        for row in fv:
            positions = list(map(int, row.split(',')))
    sorted_positions = np.sort(np.array(positions))
    unique, counts = np.unique(sorted_positions, return_counts=True)
    return np.array(unique), np.array(counts)


def calc_linear_costs(x):
    return x


def calc_nonlinear_costs(x):
    return np.array([xi*(xi+1)//2 for xi in x])


def calc_costs(cost_func, all_pos, weigth, target_pos):
    diff = all_pos - target_pos
    diff_abs = np.abs(diff)
    costs = cost_func(diff_abs)
    costs_weighted = weigth * costs
    sum = np.sum(costs_weighted)
    return sum


def dx(f, target_pos):
    return f(target_pos+1) - f(target_pos)


def calc_fuel(cost_func):
    pos, pos_weight = read_pos()

    min_index = 0
    max_index = len(pos)
    f = partial(calc_costs, cost_func, pos, pos_weight)
    f_dx = partial(dx, f)

    least_fuel_required = sys.maxsize
    least_fuel_required_index = -1

    left_index = min_index
    right_index = max_index-1
    mid_index = (left_index + right_index) // 2
    i = 0
    fl = f_dx(pos[left_index])
    fr = f_dx(pos[right_index])
    fm = f_dx(pos[mid_index])
    while True:
        #print('p: %4d %4d %4d dx: %7d %7d %7d' % (pos[left_index], pos[mid_index], pos[right_index], fl, fm, fr))
        assert(fl*fr <= 0)

        if fl*fm < 0:
            right_index = mid_index
            fr = fm
        else:
            left_index = mid_index
            fl = fm
        i += 1

        mid_new_index = (left_index + right_index) // 2
        fm = f_dx(pos[mid_new_index])
        if mid_new_index != mid_index:
            mid_index = mid_new_index
        else:
            if fm > 0:
                #print('i %d f %d' % (i, pos[mid_index]))
                return f(pos[mid_index])
            else:
                #print('i %d f %d' % (i, pos[mid_index+1]))
                return f(pos[mid_index+1])


def day07a():
    return calc_fuel(calc_linear_costs)


def day07b():
    return calc_fuel(calc_nonlinear_costs)


if __name__ == '__main__':
    print(day07a())
    print(day07b())
