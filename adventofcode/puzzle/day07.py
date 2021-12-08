import numpy as np
import sys
from functools import partial


def read_pos():
    positions = []
    with open('day/7/input.txt') as fv:
        for row in fv:
            positions = list(map(int, row.split(',')))
    return np.array(positions)


def calc_linear_costs(x):
    return x


def calc_nonlinear_costs(x):
    return np.array([xi*(xi+1)//2 for xi in x])


def calc_costs(cost_func, all_pos, target_pos):
    return np.sum(cost_func(np.abs(all_pos - target_pos)))


def dx(f, target_pos):
    return f(target_pos+1) - f(target_pos)


def calc_fuel(cost_func):
    positions = read_pos()
    min_pos = min(positions)
    max_pos = max(positions)
    f = partial(calc_costs, cost_func, positions)
    f_dx = partial(dx, f)

    least_fuel_required = sys.maxsize
    least_fuel_required_index = -1

    left = min_pos
    right = max_pos-1
    mid = (left + right) // 2
    i = 0
    fl = f_dx(left)
    fr = f_dx(right)
    fm = f_dx(mid)
    while True:
        # print('p: %d %d %d' % (left, mid, right))
        # print('dx: %d %d %d' % (fl, fm, fr))
        assert(fl*fr <= 0)

        if fl*fm < 0:
            right = mid
            fr = fm
        else:
            left = mid
            fl = fm
        i += 1

        mid_new = (left + right) // 2
        fm = f_dx(mid)
        if mid_new != mid:
            mid = mid_new
        else:
            print('i %d f %d' % (i, mid))
            if fm > 0:
                return f(mid)
            else:
                return f(mid+1)


def day07a():
    return calc_fuel(calc_linear_costs)


def day07b():
    return calc_fuel(calc_nonlinear_costs)


if __name__ == '__main__':
    print(day07a())
    print(day07b())
