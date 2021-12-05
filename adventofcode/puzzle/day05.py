import numpy as np
from sys import maxsize

def read_lines():
    with open('day/5/input.txt') as fv:
        lines = []
        for row in fv:
            row = row[:-1]
            coordinate_as_string = row.split('->')
            line = []
            for c in coordinate_as_string:
                xy = c.split(',')
                p = np.array([int(xy[0]), int(xy[1])], dtype=int)
                line.append(p)
            lines.append(line)
        return lines


def day05a():
    return calc(skip_diagonal_lines=True)


def day05b():
    return calc(skip_diagonal_lines=False)


def calc(skip_diagonal_lines):
    lines = read_lines()
    print(lines)

    oceans_floor = np.zeros([1000, 1000], dtype=np.uint)

    for l in lines:
        p0 = l[0]
        p1 = l[1]
        d = p0
        if skip_diagonal_lines:
            if (p0[0] != p1[0]) and (p0[1] != p1[1]):
                continue
        oceans_floor[d[1], d[0]] += 1
        while (d-p1).any():
            if d[0] > p1[0]:
                d[0] -= 1
            elif d[0] < p1[0]:
                d[0] += 1

            if d[1] > p1[1]:
                d[1] -= 1
            elif d[1] < p1[1]:
                d[1] += 1
            oceans_floor[d[1], d[0]] += 1

    np.set_printoptions(formatter=None, linewidth=5000, threshold=maxsize)
    return np.sum(oceans_floor > 1)


if __name__ == '__main__':
    print(day05a())
    print(day05b())
