def read_diagnostics():
    diagnostics = []
    with open('day/3/input.txt') as fv:
        values = []
        digits = 0
        for row in fv:
            bias = ord('0')
            digits = len(row) -1  # don't count endline
            value = int(0)
            for i in range(0, digits):
                value = value << 1
                value = value | (ord(row[i]) - bias)
            values.append(value)
        return values, digits


def day03a():
    values, digits = read_diagnostics()
    ones = []
    for i in range(0, digits):
        acc = 0
        for j in values:
            if j & (1 << i) != 0:
                acc = acc + 1
        ones.append(acc)

    gamma_rate = 0
    epsilon_rate = 0
    for i in ones:
        gamma_rate = gamma_rate << 1
        epsilon_rate = epsilon_rate << 1
        if 2*i > len(values):
            gamma_rate = gamma_rate | 1
        else:
            epsilon_rate = epsilon_rate | 1

    chk = gamma_rate ^ epsilon_rate

    return gamma_rate * epsilon_rate


def filter_bit(values, index, invert_condition):
    filtered_values = []
    ones = 0

    # count ones at position index
    for v in values:
        if ((v >> index) & 1) != 0:
            ones = ones + 1

    if 2*ones >= len(values):
        condition = 1
    else:
        condition = 0
    if invert_condition:
        condition = condition ^ 1

    for v in values:
        if ((v >> index) & 1) == condition:
            filtered_values.append(v)

    if len(filtered_values) == 1:
        return filtered_values.pop()
    elif index == 0:
        raise RecursionError

    return filter_bit(filtered_values, index-1, invert_condition)


def day03b():
    values, digits = read_diagnostics()
    oxygen_generator_rating = 0
    co2_scrubber_rating = 0

    oxygen_generator_rating = filter_bit(values=values, index=digits - 1, invert_condition=False)
    co2_scrubber_rating = filter_bit(values=values, index=digits - 1, invert_condition=True)

    return oxygen_generator_rating * co2_scrubber_rating


if __name__ == '__main__':
    print('%d is the power consumption' % (day03a()))
    print('%d is the life support rating' % (day03b()))
