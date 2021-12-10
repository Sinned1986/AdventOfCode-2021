import numpy as np

def read_segments(mapping):
    all_lines = []
    with open('day/8/input.txt') as fv:
        for row in fv:
            val = row[:-1].split('|')
            all_symbols = list(map(mapping, val[0][:-1].split(' ')))
            current_symbols = list(map(mapping, (val[1][1:].split(' '))))
            all_lines.append([all_symbols, current_symbols])
    return all_lines


def no_mapping(x):
    return x


def symbol_to_bitfield_mapping(symbol):
    bitfield = 0
    symbol_list = list(symbol)

    for segment in symbol_list:
        segment = ord(segment) - ord('a')
        bitfield |= 1 << segment

    return bitfield


def day08a():
    lines = read_segments(no_mapping)
    histogram = np.zeros(10, dtype=int)

    for line in lines:
        for symbol in line[1]:
            l = len(symbol)
            if l == 2:
                histogram[1] += 1
            if l == 4:
                histogram[4] += 1
            if l == 3:
                histogram[7] += 1
            if l == 7:
                histogram[8] += 1
    return sum(histogram)


def day08b():
    lines = read_segments(no_mapping)
    sum_of_displayed_values = 0

    for line in lines:
        mapping_sn = {}
        classes = {k: [] for k in range(2, 8)}

        for symbol in line[0]:
            classes[len(symbol)].append(symbol_to_bitfield_mapping(symbol))

        mapping_sn[classes[2][0]] = 1
        mapping_sn[classes[3][0]] = 7
        mapping_sn[classes[4][0]] = 4
        mapping_sn[classes[7][0]] = 8

        # get 0 with the common segmets of class 5, 9 and 6 contain all, 0 contains one less
        classes_5_common = -1
        for digit in classes[5]:
            classes_5_common &= digit

        for digit in classes[6]:
            if (digit & classes_5_common) != classes_5_common:
                mapping_sn[digit] = 0
                break

        # get 9, it contains 1 and is not 0
        mapping_ns = {value: key for key, value in mapping_sn.items()}
        for digit in classes[6]:
            if (digit != mapping_ns[0]) and ((digit & mapping_ns[1]) == mapping_ns[1]):
                mapping_sn[digit] = 9
                break

        # last remaining is 6
        mapping_ns = {value: key for key, value in mapping_sn.items()}
        for digit in classes[6]:
            if (digit != mapping_ns[0]) and (digit != mapping_ns[9]):
                mapping_sn[digit] = 6


        # get 3, it contains 1
        mapping_ns = {value: key for key, value in mapping_sn.items()}
        for digit in classes[5]:
            if (digit & mapping_ns[1]) == mapping_ns[1]:
                mapping_sn[digit] = 3
                break

        # get 5, 9 contains 5 and 3
        mapping_ns = {value: key for key, value in mapping_sn.items()}
        for digit in classes[5]:
            if (digit != mapping_ns[3]) and (digit & mapping_ns[9]) == digit:
                mapping_sn[digit] = 5
                break

        # get 2 , last remaining of class 5
        mapping_ns = {value: key for key, value in mapping_sn.items()}
        for digit in classes[5]:
            if (digit != mapping_ns[3]) and (digit != mapping_ns[5]):
                mapping_sn[digit] = 2

        displayed_value = 0
        for digit in line[1]:
            displayed_value *= 10
            displayed_value += mapping_sn[symbol_to_bitfield_mapping(digit)]

        sum_of_displayed_values += displayed_value
    return sum_of_displayed_values


if __name__ == '__main__':
    print(day08a())
    print(day08b())
