# Day 1: Sonar Sweep

import numpy


def read_measurements():
    measurements = []
    with open('day/1/input.txt') as fv:
        for row in fv:
            measurements.append(int(row))
    return measurements


def day01a():
    measurements = read_measurements()
    entries = len(measurements)
    diff_ops = list(zip(measurements[1:entries], measurements[0:entries - 1]))
    incr = 0
    for op in diff_ops:
        if op[0] > op[1]:
            incr = incr + 1

    return incr


def day01b():
    measurements = numpy.array(read_measurements())
    l = len(measurements)  # raw measurements
    w = 3  # filter window
    filtered_measurement = measurements[0:l - (w - 1)] + measurements[1:l - (w - 2)] + measurements[2:l - (w - 3)]

    l = len(filtered_measurement)
    incr = 0
    diff = filtered_measurement[1:l] - filtered_measurement[0:l - 1]
    for x in diff:
        if x > 0:
            incr = incr + 1

    return incr


if __name__ == "__main__":
    print('%d measurements are larger then the previous ones' % day01a())
    print('%d sums are larger than the previous' % day01b())
