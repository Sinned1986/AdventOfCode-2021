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

if __name__ == '__main__':
    print('%d is the power consumption' % (day03a()))
